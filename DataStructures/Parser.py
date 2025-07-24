from LocalLib.antlr4 import *

from DataStructures.AST_muFHML import AST
from LocalLib.antlr4.InputStream import InputStream
from logic_parser.LogicLexer import LogicLexer
from logic_parser.LogicParser import LogicParser
from logic_parser.LogicVisitor import LogicVisitor
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

if __name__ == '__main__':
    formula1 = '(μX(x2, y2, z2). ⟨42⟩ ⋁x. ([0 = z2] ∨ [z = x]))(42, 41, 40)'
    ast = AST(parse_formula(formula1))
    print(ast)

    formula2 = ("Иk."
       "(μX(x2, y2, z2). "
       "⟨42⟩ ⋁x. ("
           "("
               "("
                   "⟨*,x⟩ (X(x2, 1, x2) ∨ [0 = z2]) ∨ ⋁z. [z = x]"
               ") ∨ ("
                   "⟨*,x⟩ (X(x2, 1, x2) ∨ [0 = z2]) ∨ ⋁z. [z = x]"
               ")"
           ") ∨ [0 = z2]"
       "))"
       "(42, 41, 40)"
    )
    ast = AST(parse_formula(formula2))
    print(ast)
