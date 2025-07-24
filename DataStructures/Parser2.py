from LocalLib.antlr4 import *

from DataStructures.AST_muFHML import AST
from DataStructures.Configuration import Configuration
from DataStructures.Environment import Environment
from DataStructures.FRA import FRA
from DataStructures.Formulas import Formula
from DataStructures.ParityGames import FRAParity
from logic_parser.LogicLexer import LogicLexer
from logic_parser.LogicParser import LogicParser
from logic_parser.MyLogicVisitor import MyLogicVisitor

def parse_formula(input_str: str):
    input_stream = InputStream(input_str)
    lexer = LogicLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = LogicParser(token_stream)

    tree = parser.formula()  # entry rule
    visitor = MyLogicVisitor()
    result = visitor.visit(tree)
    return result


# Examples from paper
if __name__ == '__main__':

    # Example 7

    # FRA accepting words a1 a2 ... such that ai != aj if i != j
    r = 1; n = 1
    mu = [[]]
    delta = [(0,(0,"GFresh"),0)]
    A1 = FRA(r,n,mu,delta,[])

    # FRA accepting words a1 a2 ... such that ai != a(i+1)
    r = 1; n =2
    mu = [[], [0]]
    delta = [(0,(0,"LFresh"),1),(1,(0,"LFresh"),1)]
    A2 = FRA(r,n,mu,delta,[])

    # FRA equivalent to A1 with locally fresh at the start
    r = 1; n =2
    mu = [[], [0]]
    delta = [(0,(0,"LFresh"),1),(1,(0,"GFresh"),1)]
    A3 = FRA(r,n,mu,delta,[])

    # Example 8
    r = 1; n =2
    Sig = ["S", "U", "T"]
    mu = [[], [0]]
    delta = [(0,("S",0,"LFresh"),1),(1,("U",0,"Stored"),1),(1,("T",0,"Stored"),0)]
    A4 = FRA(r,n,mu,delta,[],Sig)

    # For reference
    # Symbols & brackets: "≠", "=", "∨", "∧", "⋁", "⋀", "◇", "☐", "μ", "ν", "И", ⟨⟩, []

    FRA.resetAll()

    # phi_ALLFresh = '(μX(). ⋀x. [x](X() ∧ (νY(). ⋀y. [y](Y() ∧ [x≠y]))()))()' # \mu at start for testing
    phi_ALLFresh = '(ν X().⋁ x. ⟨ PUSH,x ⟩ ((⟨ POP,x ⟩ X()) ∨ (ν Y(y). ⋁ z. ([ z ≠ y ] ∧ ⟨ PUSH,z ⟩ ⟨ POP,z ⟩ Y(x)))(x)))()' # \mu at start for testing
    t = parse_formula(phi_ALLFresh)
    print(t)
    t = AST(t)
    print(t)
    env = Environment()
    f = Formula.fromAST(t, env)
    print(f,"\n")
    depths = env.alternationDepths()
    print(depths,"\n")
    c = Configuration(0,1)
    A1.check_configuration(c)

    G = FRAParity.build(A1,c,f,depths)
    L = G.getLines(False)
    for l in L: print(*l)
    # L = G.parity_game_lines() 
    # print(L)
    
