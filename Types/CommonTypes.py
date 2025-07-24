from typing import Literal, Callable

State = int
Register = int
Name = int # These are actually natural numbers
NameOrHash = int # These are actually natural numbers or -1
Modifier = Literal["Stored", "LFresh", "GFresh"]
Tag = str
Action = tuple[Register, Modifier] | tuple[Tag, Register, Modifier] # TODO: hacky
Input = Name | tuple[Tag, Name]                                     # TODO: hacky
Transition = tuple[int, Action, int]
Scheduler = Callable[[],int]
Bijection = dict[Name, Name]
Var = int  # these are actually negative integers
Value = Name | Var  # and these are all the integers
NMap = dict[str, Value]
VMap = dict[str, "Formula"]
Symbols = ["•", "≠", "=", "∨", "∧", "⋁", "⋀", "◇", "☐", "μ", "ν", "И"]
Kinds = ["Var", "Neq", "Eq", "Or", "And", "BigOr", "BigAnd", "Diamond", "Box", "Mu", "Nu", "Fresh"]
KindSymb = dict([(Kinds[i], Symbols[i]) for i in range(len(Kinds))])
