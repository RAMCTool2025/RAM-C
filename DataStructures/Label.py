from Types.CommonTypes import *

# labels are immutable
class Label:
    def __init__(self, v: Value, t: Tag = None):
        self.value = v
        self.tag = t
        self._input = None
        self._serialised = None

    def __str__(self) -> str:
        return str(self.value) if self.tag == None else f"{self.tag},{self.value}"

    def substitute(self, xs: tuple[Var, ...], vs: tuple[Value, ...]):
        return Label(vs[xs.index(self.value)], self.tag) if self.value in xs else self

    def serialise(self):
        if self._serialised == None:
            self._serialised = (self.value,) if self.tag == None else (self.tag, self.value)
        return self._serialised

    def toInput(self):
        if self._input != None: return self._input
        if self.value < 0: raise Exception("Cannot get a valid input from formula label")
        return self.value if self.tag == None else (self.tag, self.value)