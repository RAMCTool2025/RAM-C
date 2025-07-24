# A muFHML implementation addressing variable binding by assigning 
# to each binder the next negative integer not used in its body

from Types.CommonTypes import *
from typing import Literal, TypedDict

Var = int # these are actually negative integers
Value = Name | Var # and these are all the integers
NMap = dict[str, Value]
VMap = dict[str, "Formula"]
Symbols = ["•", "≠", "=", "∨", "∧", "⋁", "⋀", "◇", "☐", "μ", "ν", "И"]
Kinds = ["Var", "Neq", "Eq", "Or", "And", "BigOr", "BigAnd", "Diamond", "Box", "Mu", "Nu", "Fresh"]
KindSymb = dict([(Kinds[i],Symbols[i]) for i in range(len(Kinds))])

class pre_AST_Var(TypedDict):
    kind: tuple[Literal["Var"], str, tuple[str, ...]]

class pre_AST_Neq(TypedDict):
    kind: Literal["Neq"]
    left: str
    right: str
    
class pre_AST_Eq(TypedDict):
    kind: Literal["Eq"]
    left: str
    right: str

class pre_AST_Or(TypedDict):
    kind: Literal["Or"]
    left: "pre_AST"
    right: "pre_AST"

class pre_AST_And(TypedDict):
    kind: Literal["And"]
    left: "pre_AST"
    right: "pre_AST"

class pre_AST_BigOr(TypedDict):
    kind: Literal["BigOr"]
    left: str
    right: "pre_AST"

class pre_AST_BigAnd(TypedDict):
    kind: Literal["BigAnd"]
    left: str
    right: "pre_AST"

class pre_AST_Fresh(TypedDict):
    kind: Literal["Fresh"]
    left: str
    right: "pre_AST"
    
class pre_AST_Diamond(TypedDict):
    kind: Literal["Diamond"]
    left: str | tuple[str, str]
    right: "pre_AST"
    
class pre_AST_Box(TypedDict):
    kind: Literal["Box"]
    left: str | tuple[str, str]
    right: "pre_AST"

class pre_AST_Mu(TypedDict):
    kind: tuple[Literal["Mu"], str, tuple[str, ...]]
    left: "pre_AST"
    right: tuple[str]
    
class pre_AST_Nu(TypedDict):
    kind: tuple[Literal["Nu"], str, tuple[str, ...]]
    left: "pre_AST"
    right: tuple[str]

pre_AST = pre_AST_Var | pre_AST_Neq | pre_AST_Eq | pre_AST_Or | pre_AST_And | pre_AST_BigOr | pre_AST_BigAnd | pre_AST_Fresh | pre_AST_Diamond | pre_AST_Box | pre_AST_Mu | pre_AST_Nu

# AST's are abstract syntax trees with a bmin variable storing the min binder value
# env = (stack of binders in scope, alternation graph), initialised ([], {}) 
class AST():
    def __init__(self, ast: pre_AST):
        if ast["kind"] in Kinds:
            self.kind = ast["kind"]
        else:
            self.kind, self.X, self.Xargs = ast["kind"]
        self.bmin = 0
        match self.kind:
            case "Var":
                self.left = self.right = None
            case "Eq" | "Neq":
                self.left, self.right = ast["left"], ast["right"]
            case "Or" | "And":
                self.left = AST(ast["left"])
                self.right = AST(ast["right"])
                self.bmin = min(self.left.bmin, self.right.bmin)
            case "BigOr" | "BigAnd" | "Fresh":
                self.left = ast["left"]
                self.right = AST(ast["right"])
                self.bmin = self.right.bmin - 1
            case "Diamond" | "Box":
                self.left = ast["left"]
                self.right = AST(ast["right"])
                self.bmin = self.right.bmin
            case "Mu" | "Nu":
                self.left = AST(ast["left"])
                self.right = ast["right"]
                if len(self.right) != len(self.Xargs):
                    raise Exception("Number mismatch in abstracted vars and values ")
                self.bmin = self.left.bmin - len(self.Xargs)
            case _:
                raise Exception(f"AST pattern unmatched {self.kind}")
                
    def __str__(self) -> str:
        return self._ascii_tree()

    def _ascii_tree(self, prefix: str = "", is_left: bool = True) -> str:
        S = ["├","─","└","│"]
        angle = S[2]+S[1]+" "
        vdash = S[0]+S[1]+" "
        
        def inRec(ptr: AST|str|tuple, acc: str, pre: str):
            if isinstance(ptr, str): return acc+pre+ptr
            if isinstance(ptr, tuple): return acc+pre+f"({(",".join(ptr))})"
            if ptr.kind in ("Var","Mu","Nu"):
                val = "" if ptr.kind=="Var" else KindSymb[ptr.kind]
                val = f"{val}{ptr.X}({",".join(ptr.Xargs)})"
            else:
                val = f"{KindSymb[ptr.kind]}" 
            if ptr.left==ptr.right==None:
                return acc+pre+val
            if ptr.kind in ("Eq","Neq"):
                return acc+pre+f"[{ptr.left} {val} {ptr.right}]"
            if pre == vdash: pre2 = S[3]+"  "
            elif pre == angle: pre2 = "   "
            else: pre2 = ""
            left = inRec(ptr.left,acc+pre2,angle)
            right = inRec(ptr.right,acc+pre2,vdash)
            return acc+pre+val+"\n"+right+"\n"+left        
            
        return inRec(self,"","")
