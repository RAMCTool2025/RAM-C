from Types.CommonTypes import *


class Configuration:
    def __init__(self, state: State, r: Register):
        self.state = state
        self.rho = [-1 for _ in range(r)]
        self.H = set()
        self._serialised = None

    def update(self, r: Register, v: Name):
        for i in range(len(self.rho)):
            if i == r:
                self.rho[i] = v
            elif self.rho[i] == v:
                raise Exception("update error")
        self.H.add(v)
        self._serialised = None

    def restrict(self, dom: list[Register]):
        for i in range(len(self.rho)):
            if i not in dom: self.rho[i] = -1
        self._serialised = None

    # clones configuration and updates state
    def clone(self, q: State = None):
        if q == None: q = self.state
        c = Configuration(q, len(self.rho))
        c.rho = self.rho[:]
        c.H = set(self.H)
        return c

    def getBijection(self, other: "Configuration") -> Bijection:
        if self.state != other.state: return None
        return dict([(self.rho[i], other.rho[i]) for i in range(len(self.rho)) if self.rho[i] != -1])

    def __str__(self):
        return f"({self.state}, {self.rho}, {self.H})"

    # it actually returns a tuple
    def serialise(self):
        if self._serialised == None:
            H = list(self.H);
            H.sort()
            self._serialised = (self.state, "-", *tuple(self.rho), "-", *tuple(H))
        return self._serialised

    def __eq__(self, other):
        return self.serialise() == other.serialise()

    def __hash__(self):
        return hash(self.serialise())