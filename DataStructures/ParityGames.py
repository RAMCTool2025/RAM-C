# FRA-muFHML parity games
from DataStructures.FRA import FRA
from DataStructures.Formulas import Formula
from Types.CommonTypes import *
from DataStructures.Configuration import Configuration

# These types are for PGSolver format, each line contains
# a node, its priority, its owner, its successors, and a label
Priority = int
Player = Literal[0, 1]
Line = tuple[int, Priority, Player, list[int], str]


class BoundedConfiguration(Configuration):
    def __init__(self, state: State, r: Register, N: int):
        if r > N: raise Exception("BoundedConfiguration cannot have more registers than the bound")
        super().__init__(state, r)
        self.N = N

    # restricts the history from N+1+k to N+1 names
    # so that it contains all names in rho and fromphi
    def sanitise(self, fromphi: set[Name]):
        if len(self.H) <= self.N + 1: return
        copy = list(self.H)
        for n in copy:
            if n not in self.rho and n not in fromphi:
                self.H.remove(n)
                self._serialised = None
                if len(self.H) == self.N + 1: return
        raise Exception(f"Was not able to sanitise {self}")

    def update(self, r: Register, v: Name, fromphi: set[Name]):
        super().update(r, v)
        self.sanitise(fromphi)

    # clones configuration and updates state
    def clone(self, q: State = None) -> "BoundedConfiguration":
        c = super().clone(q)
        c.N = self.N
        return c

    @staticmethod
    def fromConfiguration(c: Configuration, fromphi: set[Name], N: int):
        bc = BoundedConfiguration(c.state, len(c.rho), N)
        bc.rho = c.rho[:]
        bc.H = set(c.H)
        bc.sanitise(fromphi)
        return bc


class Node:
    def __init__(self, bc: BoundedConfiguration, phi: Formula, depths: dict[str, int]):
        self.configuration = bc
        self.phi = phi
        self.N = self.configuration.N
        self.owner = self.phi.owner
        self._hashed = None
        self.support = self.configuration.H - self.phi.getSupport()
        self.criticalH = len(self.support)
        self.support.update(self.phi.getSupport())
        match self.phi.kind:  # set the owner
            case "Neq" | "Eq":
                b = self.phi.evaluate()
                if b == None: raise Exception("Trying to create node with open formula")
                self.owner = 1 if b else 0
            case "Or" | "BigOr" | "Diamond":
                self.owner = 0
            case _:
                self.owner = 1
        match self.phi.kind:  # set the priority 
            case "Mu": self.priority = (2*depths[self.phi.X]//2)+1
            case "Nu": self.priority = (2*depths[self.phi.X]//2)
            case _   : self.priority =  0
            

    def step(self, A: FRA, depths: dict[str, int]) -> list["Node"]:
        def convert(c: Configuration, psi: Formula) -> "Node":
            return Node(BoundedConfiguration.fromConfiguration(c, psi.getSupport(), self.N), psi, depths)

        match self.phi.kind:
            case "Var" | "Neq" | "Eq" | "Or" | "And" | "Mu" | "Nu":
                return [Node(self.configuration, psi, depths) for psi in self.phi.step()]
            case "Diamond" | "Box":
                return [convert(c, self.phi.body) for c in A.read_input(self.configuration, self.phi.label.toInput())]
            case "BigOr" | "BigAnd":
                names = list(self.support) + [FRA.nextFresh(self.support)]
                return [convert(self.configuration, psi) for psi in self.phi.step(names)]
            case "Fresh":
                names = [FRA.nextFresh(self.support)]
                return [convert(self.configuration, psi) for psi in self.phi.step(names)]
            case _:
                raise Exception("Case missing")

    # equality is under permutation
    def __eq__(self, other: "Node") -> bool:
        if not isinstance(other,Node): return False
        pi = self.configuration.getBijection(other.configuration)
        if pi == None: return False
        if len(self.configuration.H) != len(other.configuration.H): return False
        # We need to check that |H1 \ supp(rho1,phi1)| = |H2 \ supp(rho2,phi2)|
        # assuming that |H1| = |H2|. For this, and given that we also check that 
        # (rho1,phi1) ~nom (rho2,phi2), it suffices (TODO?) to compare |Hj \ supp(phij)|
        if self.criticalH != other.criticalH: return False
        if self.phi.extendBijection(pi, other.phi): return True
        return False

    def __str__(self) -> str:
        return f"⟨{self.configuration}, {self.phi}⟩"

    # naive hash, not equal under permutation
    def __hash__(self) -> int:
        if self._hashed == None:
            self._hashed = hash((hash(self.configuration), hash(self.phi)))
        return self._hashed


class FRAParity():
    def __init__(self, S: list[Node], T: dict[Node, set[Node]]):
        self.T = T
        self.S = S
        self.Sinv = dict([(S[i], i) for i in range(len(self.S))])

    # Build a parity game for A starting from (c,phi)
    @staticmethod
    def build(A: FRA, c: Configuration, phi: Formula, depths: dict[str, int]):
        def calculateN(A: FRA, phi: Formula):
            r_i = max([len(S) for S in A.mu])
            return len(phi.getSupport()) + phi.bDepth + r_i

        N = calculateN(A, phi)
        bc = BoundedConfiguration.fromConfiguration(c, phi.getSupport(), N)
        S = [Node(bc, phi, depths)]  # stores all nodes in a list, so that we can check equality with Node.eq
        Q = {S[0]}
        T = {}
        while len(Q) > 0:
            nd = Q.pop()
            if nd in T: continue
            T[nd] = set()
            nexts = nd.step(A, depths)
            for x in nexts:
                # print("next:", x)
                if x not in S:
                    S.append(x)
                else:
                    x = S[S.index(x)]  # x replaced by its representative
                T[nd].add(x)
                Q.add(x)
        return FRAParity(S, T)

    # Line = tuple[int, Priority, Player, list[int], str?]
    def getLines(self, ignore_labels=True):
        L = []
        for i in range(len(self.S)):
            nd = self.S[i]
            nds = sorted([self.Sinv[x] for x in self.T[nd]])
            if ignore_labels: line = (i, nd.priority, nd.owner, nds)
            else: line = (i, nd.priority, nd.owner, nds, str(nd))
            L.append(line)
        return L

    # # Creates the line in the parity game format as expected by oink
    # def parity_game_lines(self) -> str:
    #     pg_lines = []
    #     for (i, prio, player, successors, label) in self.getLines():
    #         succ_str = ",".join(map(str, successors))
    #         line = f'{i} {prio} {player} {succ_str} "{label}"'
    #         pg_lines.append(line)
    #     return "\n".join(pg_lines)

    def parity_game_lines(self, ignore_labels=True) -> str:
        lines = self.getLines(ignore_labels)
        lenlines = len(lines)
        pg_lines = [f"parity {lenlines+2};"]
        sinks = [f"{lenlines} 1 0 {lenlines};", f"{lenlines+1} 0 0 {lenlines+1};"]
        for l in lines:
            if ignore_labels:
                (i, prio, player, successors) = l
                label = "" # assumes that a space before ; at end of line is ok
            else:
                (i, prio, player, successors, label) = l
                label = f'"{label}"'
            if successors:
                succ_str = ",".join(map(str, successors))
                line = f'{i} {prio} {player} {succ_str} {label};'
            else:
                line = f'{i} {prio} {player} {lenlines+player} {label};' 
            pg_lines.append(line)
        pg_lines += sinks
        return "\n".join(pg_lines)

