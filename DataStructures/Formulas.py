from DataStructures.AST_muFHML import AST
from DataStructures.Label import Label
from DataStructures.Environment import Environment
from Types.CommonTypes import *
from abc import ABC, abstractmethod

# Notes:    
# support = names - bound names
# hash = string representation
# Formulas are immutable
class Formula(ABC):
    def __init__(self):
        self.strForm = None
        self.bDepth = 0 # binding depth
        self._serialised = None
        self.owner = None # 0 is Defender, 1 is Attacker
        self.kind = None 
        self.values = None

    def __str__(self) -> str:
        if self.strForm == None: setupStrForm()
        return self.strForm

    @abstractmethod
    def setupStrForm(self):
        pass
    
    @abstractmethod
    def setupValues(self):
        pass
    
    def getSupport(self) -> set[Name]:
        return set([v for v in self.values if v >= 0])
    
    # Destructive, it changes pi. Returns True/False on whether pi can be extended
    # so that pi.self == other 
    # It uses the serialisation of formulas. Check if Polish notation used resolves ambiguity
    def extendBijection(self, pi: Bijection, other: "Formula") -> bool:
        def isConstant(x):
            return x=="-" or x in Symbols or isinstance(x,str) or x < 0
        
        t_self, t_other = self.serialise(), other.serialise()
        if len(t_self)!=len(t_other): return False
        for i in range(len(t_self)):
            x_self, x_other = t_self[i], t_other[i]
            if isConstant(x_self): # if x_self not a name
                if x_self != x_other: return False
            elif isConstant(x_other): # if only x_self a name
                return False
            elif x_self in pi: # if both names and x_self already matched 
                    if pi[x_self]!=x_other: return False
            else: # if both names and x_self a new name
                if x_other in pi.values(): return False
                pi[x_self] = x_other
        return True
        
    @abstractmethod
    def serialise(self) -> tuple:
        pass
    
    @abstractmethod
    def step(self, S: set[Name]) -> list["Formula"]:
        pass
    
    # A bit of a hack, this calls expandX with Nones for X and phi
    def substitute(self, xs: tuple[Var,...], ns: tuple[Name,...]) -> "Formula":
        return self.expandX(None, None, xs, ns)
    
    # Use an auxiliary method to calculate a "pre-Formula" where binder discipline may not be good
    # because of substitutio phi/X
    # Then do a top-down pass to fix binders (destructive)
    def expandX(self, X: str, phi: "Formula", xs: tuple[Var,...], ns: tuple[Name,...]) -> "Formula":
        phi = self._pre_expandX(X, phi, xs, ns)
        if X != None: 
            phi._fix_binders(X, (), ())
        return phi
    
    @abstractmethod
    def _pre_expandX(self, X: str, phi: "Formula", xs: tuple[Var,...], ns: tuple[Name,...]) -> "Formula":
        pass
    
    @abstractmethod
    def _fix_binders(self, X: str, xs: tuple[Var,...], ys: tuple[Var,...]):
        pass
    
    def hash(self):
        return hash(str(self))
    
    @staticmethod
    def fromAST(ast: AST, env: Environment) -> "Formula":
        def nmap_update(x:str, nmap: NMap):
            if x not in nmap:
                v = int(x)
                if v < 0: raise Exception("fromAST found negative (free) name")
                nmap[x] = v
            
        nmap = env.nmap
        pair = (ast.left, ast.right)
        match ast.kind:
            case "Var":
                for x in ast.Xargs: nmap_update(x,nmap)
                return Formula_Var.fromAST(ast.X, ast.Xargs, env)
            case "Neq" | "Eq":
                for x in pair: nmap_update(x,nmap)
                return Formula_NeqEq.fromAST(ast.kind, *pair, env)
            case "Or" | "And":
                return Formula_OrAnd.fromAST(ast.kind, *pair, env)
            case "BigOr" | "BigAnd" | "Fresh":
                nmap[ast.left] = ast.bmin
                return Formula_Quantifier.fromAST(ast.kind, *pair, env)
            case "Diamond" | "Box":
                x = pair[0] if isinstance(pair[0],str) else pair[0][1]
                nmap_update(x,nmap)
                return Formula_Modal.fromAST(ast.kind, *pair, env)
            case "Mu" | "Nu":
                for i in range(len(ast.Xargs)):
                    nmap[ast.Xargs[i]] = ast.bmin+i
                for x in ast.right: nmap_update(x,nmap)
                return Formula_Rec.fromAST(ast.kind, ast.X, ast.Xargs, *pair, env)
            case _:
                raise Exception(f"fromAST pattern {ast.kind} unmatched")
        
# the subclasses feature two kinds of constructors, both of which are bottom-up:     
# 1. One that is using the internal ints-for-names representation
# 2. One that uses the external strs-for-names representation and a NameMap environment
# 
class Formula_Var(Formula):
    def __init__(self, X: str, vs: tuple[Value,...], pol: Literal["Mu", "Nu"]):
        super().__init__()
        self.kind = "Var"
        self.X, self.vs, self.masterpol = X, vs, pol
        self.setupValues()
        self.setupStrForm()

    def setupStrForm(self):
        self.strForm = f"{self.X}{self.vs}"

    def setupValues(self):
        self.values = set(self.vs)
        
    def serialise(self):
        if self._serialised == None: 
            self._serialised = (KindSymb[self.kind],self.X,*self.vs)
        return self._serialised
    
    def step(self, S: set[Name]=None) -> list[Formula]:
        raise Exception("Cannot step an open recursion variable")
    
    def _pre_expandX(self, X: str, phi: Formula, xs: tuple[Var,...], ns: tuple[Name,...]) -> Formula:
        us = list(self.vs)
        for i in range(len(us)):
            if us[i] in xs: us[i] = ns[xs.index(us[i])]
        if X!=self.X: 
            return Formula_Var(self.X,tuple(us),self.masterpol)
        elif phi.kind == "Mu":
            return Formula_Mu(X,phi.xs,phi.body,tuple(us))
        elif phi.kind == "Nu":
            return Formula_Nu(X,phi.xs,phi.body,tuple(us))
        else: 
            raise Exception("Sublass kind-matching error")
            
    def _fix_binders(self, X: str, xs: tuple[Var,...], ys: tuple[Var,...]):
        us = list(self.vs)
        for i in range(len(us)):
            if us[i] in xs: 
                us[i] = ys[xs.index(us[i])]
        self.vs = tuple(us)
        self.setupValues(); self.setupStrForm()        
        
    @staticmethod
    def fromAST(X: str, xs: tuple[str], env: Environment) -> "Formula_Var":
        nmap = env.nmap
        vs = tuple([nmap[x] for x in xs])
        if X not in env.graph: raise Exception("Recursion variable hit but not in environment!")
        masterpol, index, E = env.graph[X] # binder polarity, stack index and edges for X
        for i in range(index, len(env.stack)): # add as edges all binder vars of the other polarity
            Y, pol = env.stack[i]
            if masterpol != pol: E.add(Y)
        return Formula_Var(X,vs,masterpol)    

class Formula_NeqEq(Formula):
    def __init__(self, v1: Value, v2: Value):
        super().__init__()
        self.v1, self.v2 = v1, v2
        self.setupValues()

    def setupStrForm(self):
        self.strForm = f"[{self.v1} {KindSymb[self.kind]} {self.v2}]"

    def setupValues(self):
        self.values = set([self.v1,self.v2])
        
    def serialise(self):
        if self._serialised == None: 
            self._serialised = (KindSymb[self.kind],self.v1,self.v2)
        return self._serialised
    
    def step(self, S: set[Name]=None) -> list[Formula]:
        return []
                                                       
    def _pre_expandX(self, X: str, phi: Formula, xs: tuple[Var,...], ns: tuple[Name,...]) -> "Formula_NeqEq":
        u1 = ns[xs.index(self.v1)] if (self.v1 in xs) else self.v1
        u2 = ns[xs.index(self.v2)] if (self.v2 in xs) else self.v2
        if self.kind == "Neq":
            return Formula_Neq(u1,u2)
        if self.kind == "Eq":
            return Formula_Eq(u1,u2)
        raise Exception("Subclass kind-matching error")

    def _fix_binders(self, X: str, xs: tuple[Var,...], ys: tuple[Var,...]):
        self.v1 = ys[xs.index(self.v1)] if (self.v1 in xs) else self.v1
        self.v2 = ys[xs.index(self.v2)] if (self.v2 in xs) else self.v2  
        self.setupValues(); self.setupStrForm()
        
    @staticmethod
    def fromAST(kind: str, x: str, y: str, env: Environment) -> "Formula_NeqEq":
        nmap = env.nmap
        if kind == "Neq":    
            return Formula_Neq(nmap[x],nmap[y])    
        if kind == "Eq":    
            return Formula_Eq(nmap[x],nmap[y])    
        raise Exception("Subclass kind-matching error")
        
class Formula_Neq(Formula_NeqEq):
    def __init__(self, v1: Value, v2: Value):
        super().__init__(v1,v2)
        self.kind = "Neq"
        self.setupStrForm()        

    def evaluate(self):
        return self.v1 != self.v2 
        
class Formula_Eq(Formula_NeqEq):
    def __init__(self, v1: Value, v2: Value):
        super().__init__(v1,v2)
        self.kind = "Eq"
        self.setupStrForm()        

    def evaluate(self):
        return self.v1 == self.v2 
                
class Formula_OrAnd(Formula):
    def __init__(self, left: Formula, right: Formula):
        super().__init__()
        self.left, self.right = left, right
        self.bDepth = max(left.bDepth,right.bDepth)
        self.setupValues()
            
    def setupStrForm(self):
        self.strForm = f"({self.left} {KindSymb[self.kind]} {self.right})"   

    def setupValues(self):
        self.values = self.left.values | self.right.values
        
    def serialise(self):
        if self._serialised == None: 
            self._serialised = (KindSymb[self.kind],*self.left.serialise(),"-",*self.right.serialise())
        return self._serialised
        
    def step(self, S: set[Name]=None) -> list[Formula]:
        return [self.left,self.right]
        
    def _pre_expandX(self, X: str, phi: Formula, xs: tuple[Var,...], ns: tuple[Name,...]) -> "Formula_OrAnd":
        if self.kind == "Or":
            return Formula_Or(self.left._pre_expandX(X,phi,xs,ns),self.right._pre_expandX(X,phi,xs,ns))
        if self.kind == "And":                                               
            return Formula_And(self.left._pre_expandX(X,phi,xs,ns),self.right._pre_expandX(X,phi,xs,ns))
        raise Exception("Subclass kind-matching error")

    def _fix_binders(self, X: str, xs: tuple[Var,...], ys: tuple[Var,...]):
        self.left._fix_binders(X, xs, ys)
        self.right._fix_binders(X, xs, ys)
        self.setupValues(); self.setupStrForm()
        
    @staticmethod
    def fromAST(kind: str, left: AST, right: AST, env: Environment) -> "Formula_OrAnd":
        left = Formula.fromAST(left, env.copy())
        right = Formula.fromAST(right, env)
        if kind == "Or": return Formula_Or(left, right)
        if kind == "And": return Formula_And(left, right)
        raise Exception("Subclass kind-matching error")
    
class Formula_Or(Formula_OrAnd):
    def __init__(self, left: Formula, right: Formula):
        super().__init__(left,right)
        self.kind = "Or"
        self.setupStrForm()        
    
class Formula_And(Formula_OrAnd):
    def __init__(self, left: Formula, right: Formula):
        super().__init__(left,right)
        self.kind = "And"
        self.setupStrForm()        
    
class Formula_Quantifier(Formula):
    def __init__(self, binder: Var, body: Formula):
        super().__init__()
        self.binder = binder
        self.body = body # TODO? this gets a tuple
        self.bDepth = body.bDepth + 1
        self.setupValues()

    def setupStrForm(self):
        self.strForm = f"{KindSymb[self.kind]}{self.binder}. {self.body}"

    def setupValues(self):
        self.values = self.body.values - {self.binder}
        
    def serialise(self):
        if self._serialised == None: 
            self._serialised = (KindSymb[self.kind],self.binder,"-",*self.body.serialise())
        return self._serialised
    
    # Note: step here simply selects names from S; the selection of (the right) names needs
    # to be done externally
    def step(self, S: list[Name]) -> list[Formula]:
        return [self.body.substitute((self.binder,), (n,)) for n in S]

    def _pre_expandX(self, X: str, phi: Formula, xs: tuple[Var,...], ns: tuple[Name,...]) -> "Formula_Quantifier":
        if self.binder in xs: 
            raise Exception("Trying to substitute a bound variable")
        if self.kind == "BigOr":
            return Formula_BigOr(self.binder,self.body._pre_expandX(X,phi,xs,ns))
        if self.kind == "BigAnd":
            return Formula_BigAnd(self.binder,self.body._pre_expandX(X,phi,xs,ns))
        if self.kind == "Fresh":
            return Formula_Fresh(self.binder,self.body._pre_expandX(X,phi,xs,ns))
        raise Exception("Subclass kind-matching error")

    def _fix_binders(self, X: str, xs: tuple[Var,...], ys: tuple[Var,...]):
        if self.binder != -self.bDepth:
            xs, ys = (*xs,self.binder), (*ys,-self.bDepth)
            self.binder = -self.bDepth
        self.body._fix_binders(X, xs, ys)
        self.setupValues(); self.setupStrForm()
        
    @staticmethod
    def fromAST(kind: str, binder: str, body: AST, env: Environment) -> "Formula_BigOrAnd":
        nmap = env.nmap
        if kind == "BigOr": return Formula_BigOr(nmap[binder], Formula.fromAST(body, env))    
        if kind == "BigAnd": return Formula_BigAnd(nmap[binder], Formula.fromAST(body, env))    
        if kind == "Fresh": return Formula_Fresh(nmap[binder], Formula.fromAST(body, env))    
        raise Exception("Subclass kind-matching error")
    
class Formula_BigOr(Formula_Quantifier):
    def __init__(self, binder: Var, body: Formula):
        super().__init__(binder,body)
        self.kind = "BigOr"
        self.setupStrForm()        
            
class Formula_BigAnd(Formula_Quantifier):
    def __init__(self, binder: Var, body: Formula):
        super().__init__(binder,body)
        self.kind = "BigAnd"
        self.setupStrForm()        

class Formula_Fresh(Formula_Quantifier):
    def __init__(self, binder: Var, body: Formula):
        super().__init__(binder,body)
        self.kind = "Fresh"
        self.setupStrForm()        
        
class Formula_Modal(Formula):
    def __init__(self, label: Label, body: Formula):
        super().__init__()
        self.label = label
        self.body = body
        self.bDepth = body.bDepth 
        self.brackets = (None, None)
        self.setupValues()
        
    def setupStrForm(self):
        self.strForm = f"{self.brackets[0]}{self.label}{self.brackets[1]} {self.body}"

    def setupValues(self):
        self.values = self.body.values | {self.label.value}
        
    def serialise(self) -> tuple:
        if self._serialised == None: 
            self._serialised = (KindSymb[self.kind],*self.label.serialise(),"-",*self.body.serialise())
        return self._serialised
    
    def step(self, S: set[Name]=None) -> list[Formula]:
        return [self.body]

    def _pre_expandX(self, X: str, phi: Formula, xs: tuple[Var,...], ns: tuple[Name,...]) -> "Formula_Modal":
        if self.kind == "Diamond":
            return Formula_Diamond(self.label.substitute(xs,ns),self.body._pre_expandX(X,phi,xs,ns))
        if self.kind == "Box":
            return Formula_Box(self.label.substitute(xs,ns),self.body._pre_expandX(X,phi,xs,ns))
        raise Exception("Subclass kind-matching error")

    def _fix_binders(self, X: str, xs: tuple[Var,...], ys: tuple[Var,...]):
        self.label = self.label.substitute(xs,ys)
        self.body._fix_binders(X, xs,ys)
        self.setupValues(); self.setupStrForm()
       
    @staticmethod
    def fromAST(kind: str, label: str | tuple[str, str], body: AST, env: Environment) -> "Formula_Modal":
        nmap = env.nmap
        label = Label(nmap[label]) if isinstance(label,str) else Label(nmap[label[1]],label[0]) 
        body = Formula.fromAST(body, env)
        if kind == "Diamond":
            return Formula_Diamond(label, body)
        if kind == "Box":
            return Formula_Box(label, body)
        raise Exception("Subclass kind-matching error")
    
class Formula_Diamond(Formula_Modal):
    def __init__(self, label: Label, body: Formula):
        super().__init__(label, body)
        self.brackets = ("⟨","⟩")
        self.kind = "Diamond"
        self.setupStrForm()        
    
class Formula_Box(Formula_Modal):
    def __init__(self, label: Label, body: Formula):
        super().__init__(label, body)
        self.brackets = ("[","]")
        self.kind = "Box"
        self.setupStrForm()        
    
class Formula_Rec(Formula):
    def __init__(self, X: str, xs: tuple[Var,...], body: Formula, vs: tuple[Value,...]):
        super().__init__()
        self.X = X
        self.xs = xs
        self.body = body
        self.vs = vs
        self.bDepth = body.bDepth + len(self.xs)
        self.setupValues()

    def setupStrForm(self):
        # fix xs and vs if singleton tuples
        xs = self.xs if len(self.xs)!=1 else f"({self.xs[0]})"
        vs = self.vs if len(self.vs)!=1 else f"({self.vs[0]})"
        self.strForm = f"({KindSymb[self.kind]}{self.X}{xs}. {self.body}){vs}"
        
    def setupValues(self):
        self.values = self.body.values - set(self.xs)
        self.values.update(self.vs)
        
    def serialise(self):
        if self._serialised == None: 
            self._serialised = (KindSymb[self.kind],self.X,*self.xs,"-",*self.body.serialise(),"-",*self.vs)
        return self._serialised
    
    def step(self, S: list[Name]=None) -> list[Formula]:
        return [self.body.expandX(self.X, self, self.xs, self.vs)]

    def _pre_expandX(self, X: str, phi: Formula, xs: tuple[Var,...], ns: tuple[Name,...]) -> "Formula_Rec":
        if X==self.X:
            print(f"Nested binders for {X} noted in expandX")
            return self  # does not create new Formula, assumes Formulas are immutable
        if len(set(self.xs)&set(xs))>0: 
            raise Exception("Nested bound value variables")
        us = list(self.vs)
        for i in range(len(us)):
            if us[i] in xs: us[i] = ns[xs.index(us[i])]        
        if self.kind == "Mu":
            return Formula_Mu(self.X, self.xs, self.body._pre_expandX(X,phi,xs,ns), tuple(us))
        if self.kind == "Nu":
            return Formula_Nu(self.X, self.xs, self.body._pre_expandX(X,phi,xs,ns), tuple(us))
        raise Exception("Subclass kind-matching error")
        
    def _fix_binders(self, X: str, zs: tuple[Var,...], ys: tuple[Var,...]):
        if X==self.X: return # no need to fix
        if len(self.xs) > 0 and self.xs[0] != -self.bDepth:
            xs2 = [-self.bDepth+i for i in range(len(self.xs))]
            zs, ys = (*zs, *self.xs), (*ys, *xs2)
            self.xs = tuple(xs2)
        self.body._fix_binders(X, zs, ys)
        self.setupValues(); self.setupStrForm()
        
    @staticmethod
    def fromAST(kind: str, X: str, xs: tuple[str], body: AST, vs: tuple[str], env: Environment) -> "Formula_Rec":
        nmap = env.nmap
        xs = tuple([nmap[x] for x in xs])                
        vs = tuple([nmap[x] for x in vs])    
        env.stack.append((X, kind))
        env.graph[X] = (kind, len(env.stack), set())
        if kind == "Mu": 
            res = Formula_Mu(X, xs, Formula.fromAST(body, env), vs)
        elif kind == "Nu": 
            res = Formula_Nu(X, xs, Formula.fromAST(body, env), vs)
        else: raise Exception("Subclass kind-matching error")
        env.stack.pop()        
        return res

class Formula_Mu(Formula_Rec):
    def __init__(self, X: str, xs: tuple[Var], body: Formula, vs: tuple[Value]):
        super().__init__(X,xs,body,vs)
        self.kind = "Mu"
        self.setupStrForm()        
        
class Formula_Nu(Formula_Rec):
    def __init__(self, X: str, xs: tuple[Var], body: Formula, vs: tuple[Value]):
        super().__init__(X,xs,body,vs)
        self.kind = "Nu"
        self.setupStrForm()        
        

if __name__ == '__main__':
    from FRA import FRA
    def printA(A):
        print("[")
        for x in A: print(" ",x,",")
        print("]")

    varX = {"kind": ("Var", "X", ("x2","1","x2"))}    
    varQ = {"kind": ("Var", "Q", ())}    
    varZ = {"kind": ("Var", "Z", ("12","23"))}    
    orXQ = {"kind": "Or", "left": varX, "right": varQ}
    var = {"kind": ("Var", "X", ("x2","1","x2"))}    
    eq1 = {"kind": "Eq", "left": "0", "right": "z2"}
    nuQ = {"kind": ("Nu", "Q", ()), "left": orXQ, "right": ()}
    or0 = {"kind": "Or", "left": var, "right": nuQ}
    d1 = {"kind": "Diamond", "left": ("*","x"), "right": or0}
    eq2 = {"kind": "Eq", "left": "z", "right": "x"}
    or42 = {"kind": "Or", "left": eq2, "right": varZ}
    big_or = {"kind": "BigOr", "left": "z", "right": or42}
    or1 = {"kind": "Or", "left": d1, "right": big_or}
    or2 = {"kind": "Or", "left": or1, "right": or1}
    or3 = {"kind": "Or", "left": or2, "right": eq1}
    t0 = {"kind": "BigOr", "left": "x", "right": or3}
    t1 = {"kind": "Diamond", "left": "42", "right": t0 }
    t2 = {"kind": ("Mu", "X", ("x2","y2","z2")), "left": t1, "right": ("42","41","k")}
    t3 = {"kind": "Fresh", "left": "k", "right": t2}
    t4 = {"kind": ("Mu", "Z", ("q","p")), "left": t3, "right": ("10","11")}
    t5 = {"kind": ("Nu", "W", ("x3",)), "left": t4, "right": ("100",)}

    FRA.resetAll()
    t = AST(t5)
    print(t)
    env = Environment()
    f = Formula.fromAST(t, env)
    print(f)
    print(env)
    print("Alternation depths:",env.alternationDepths())
    S = set([555])
    Fs = [f]
    for i in range(5):
        Gs = []
        for f in Fs:
            Gs += f.step(S)
        print("Step",i,"(",S,")")
        printA(Gs)
        S = set([i+1 for i in S])
        Fs = Gs
