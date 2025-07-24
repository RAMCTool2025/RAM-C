from Types.CommonTypes import *
from DataStructures.Configuration import Configuration


class FRA:
    # Definition of an FRA:
    # - states are [0,...,n-1], state q_init = 0 is initial
    # - registers are [0,...,r-1]
    # - q_fin is a sublist of states
    # - delta is the transition relation, i.e. a list of Transitions
    # - mu is the availability relation, it specifies what registers are available at each state
    # - Sig is the set of tags, if degenerate (e.g. {*}) it is omitted, and tags are omitted everywhere
    def __init__(self, r: int, n: int, mu: list[list[Register]], delta: list[Transition], q_fin: list[State] = [],
                 Sig: list[Tag] = None):
        self.Sig = Sig
        self.states = [i for i in range(n)]
        self.registers = [i for i in range(r)]
        self.mu = mu
        self.delta = delta
        self.q_init = 0
        self.q_fin = q_fin

        self.check_validity()

        self.tr_function = [[] for _ in range(len(self.states))]
        for (q1, l, q2) in self.delta:
            self.tr_function[q1].append((l, q2))

    # validity checks for a built FRA
    def check_validity(self):
        # 0. initial state must have no available registers
        if self.mu[self.q_init] != []: raise Exception(0)
        # 1. initial and final states must be in the set of states
        for q in self.q_fin + [self.q_init]:
            if q not in self.states: raise Exception(1)
        # 2. availability function should be valid:
        for q in self.states:
            for r in self.mu[q]:
                if r not in self.registers: raise Exception(2)
        # 3. each transition should be valid:
        for (q1, l, q2) in self.delta:
            # 3.0. Actions are a union type, depending on whether Sig is None or not
            if (len(l) == 2) != (self.Sig == None): raise Exception(3.0)
            t, r, m = FRA.unpackThis(l, 3)
            # 3.1. the source and target should be in the set of states
            if q1 not in self.states or q2 not in self.states: raise Exception(3.1)
            # 3.2 and the resgister in the set of registers
            if r not in self.registers: raise Exception(3.2)
            # 3.3 local availability conditions:
            # 3.3.1 a known transition can only be taken at an available register
            if r not in self.mu[q1] and m == "Stored": raise Exception(3.31)
            # 3.3.2 only r can be made newly available, and only if this is a fresh transition
            for r2 in self.mu[q2]:
                if r2 not in self.mu[q1]:
                    if m not in ["LFresh", "GFresh"] or r != r2: raise Exception(3.32)

                    # check whether c is valid for this FRA

    def check_configuration(self, c: Configuration):
        q, r = c.state, c.rho
        if q not in self.states: raise Exception(f"invalid state in configuration {c}")
        if len(c.rho) != len(self.registers): raise Exception(f"invalid rho length in configuration {c}")
        for i in range(len(c.rho)):
            if (c.rho[i] == -1) ^ (i not in self.mu[q]): raise Exception(f"wrong empty registers in configuration {c}")

    # step function uses a source c, a Action l, a target state q2, and a scheduler nd for
    # resolving non-determinism when a fresh name needs to be chosen
    def step(self, c1: Configuration, l: Action, q2: State, nd: Scheduler = lambda: -1) -> tuple[Name, Configuration]:
        t, r, m = FRA.unpackThis(l, 3)
        c2 = c1.clone(q2)
        if m == "Stored":
            v = c1.rho[r]
            if v == -1: raise Exception("reading from empty register in step")
        else:
            v = nd()
            if v == -1: raise Exception("reading -1 instead of fresh name in step")
            if v in c2.H and m == "GFresh": raise Exception("reading old name as fresh in step")
            c2.update(r, v)
        c2.restrict(self.mu[q2])

        return (v, c2)

    # returns list of configurations reached from c1 with name v or pair (t,v)
    def read_input(self, c1: Configuration, p: Input) -> list[Configuration]:
        q1 = c1.state
        c2 = []
        t, v = FRA.unpackThis(p, 2)
        for (l, q2) in self.tr_function[q1]:
            t, r, m = FRA.unpackThis(l, 3)
            if m == "Stored" and c1.rho[r] == v:
                c2.append(self.step(c1, l, q2)[1])
            elif m == "LFresh" and v not in c1.rho:
                c2.append(self.step(c1, l, q2, (lambda: v))[1])
            elif m == "GFresh" and v not in c1.H:
                c2.append(self.step(c1, l, q2, (lambda: v))[1])
        return c2

    def checkWord(self, w: list[Input]):
        for p in w:
            if isinstance(p, Name) != (self.Sig == None):
                raise Exception("Wrong word type for this FRA")

    # returns list of configurations reached from c1 with word w
    def read_word(self, c: Configuration, w: list[Input]):
        self.checkWord(w)
        front = [c]
        for p in w:
            if len(front) == 0: break
            new_f = set()
            for c in front:
                new_f.update(self.read_input(c, p))
            front = list(new_f)
        return front

    # when x can be:
    # - a value or a pair (to_len=2)
    # - a tuple of to_len or to_len-1
    # expand it to a tuple of length to_len adding
    # a None at front if needed
    @staticmethod
    def unpackThis(x, to_len: int) -> tuple:
        if to_len == 2:
            return x if isinstance(x, tuple) else (None, x)
        if to_len > 2:
            return x if len(x) == to_len else (None, *x)
        raise Exception("wrong unpackThis call")

    nameCounter = 0

    # deterministic fresh name choice
    @classmethod
    def nextFresh(cls, S: set[Name]):
        while cls.nameCounter in S: cls.nameCounter += 1
        cls.nameCounter += 1
        return cls.nameCounter - 1

    @classmethod
    def resetAll(cls):
        cls.nameCounter = 0

    # String formatting
    def __str__(self):
        return f"FRA with:\nQ = {self.states},\nr = {self.registers},\nq0 = {self.q_init},\nmu = {self.mu},\ndelta = {self.delta},\nF = {self.q_fin}"


# Testing Code for FRAs
if __name__ == '__main__':
    # FRA accepting words a1 a2 ... such that ai != a(i+1)

    r = 1;
    n = 2
    mu = [[], [0]]
    q_init = 0
    q_fin = [0, 1]
    delta = [(0, (0, "LFresh"), 1), (1, (0, "LFresh"), 1)]
    A = FRA(r, n, mu, delta, q_fin)

    test = [0, 1, 2, 3, 4, 5, 6, 7, 0, 1, 2, 3, 4, 5, 6, 7]
    c0 = Configuration(q_init, 1)
    A.check_configuration(c0)

    X = A.read_word(c0, test)
    print("1:", end=" ")
    for c in X: print(c)

    test = [0, 1, 2, 3, 4, 5, 6, 7, 7, 1, 2, 3, 4, 5, 6, 7]

    X = A.read_word(c0, test)
    print("2:", end=" ")
    for c in X: print(c)



    # FRA accepting words a1 a2 ... such that ai != aj if i != j

    r = 1; n = 1
    mu = [[]]
    q_init = 0
    q_fin = [0]
    delta = [(0,(0,"GFresh"),0)]
    A = FRA(r,n,mu,delta,q_fin)

    test = [0,1,2,3,4,5,6,7]
    c0 = Configuration(q_init,1)
    A.check_configuration(c0)

    X = A.read_word(c0,test)
    print("1:", end=" ")
    for c in X: print(c)

    test = [0,1,2,3,4,5,6,7,0,1,2,3,4,5,6,7]

    X = A.read_word(c0,test)
    print("2:", end=" ")
    for c in X: print(c)

    # FRA accepting words where some name is repeated

    r = 2
    n = 3
    mu = [[], [0], []]
    q_init = 0
    q_fin = [2]
    delta = [(0, (0, "LFresh"), 0), (0, (0, "LFresh"), 1), (1, (1, "LFresh"), 1), (1, (0, "Stored"), 2),
             (2, (0, "LFresh"), 2)]
    A = FRA(r, n, mu, delta, q_fin)

    test = [0, 1, 2, 3, 4, 5, 6, 7, 0, 1, 2, 3, 4, 5, 6, 7]
    c0 = Configuration(q_init, 2)
    A.check_configuration(c0)

    X = A.read_word(c0, test)
    print("1:", end=" ")
    for c in X: print(c)

    test = [0, 1, 2, 3, 4, 5, 6, 7]

    X = A.read_word(c0, test)
    print("2:", end=" ")
    for c in X: print(c)


