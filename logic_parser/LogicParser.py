# Generated from logic_parser/Logic.g4 by ANTLR 4.9.2
# encoding: utf-8
from LocalLib.antlr4 import *
from io import StringIO
import sys

from LocalLib.antlr4 import ATNDeserializer, DFA, PredictionContextCache, ParserATNSimulator, RecognitionException
from LocalLib.antlr4.BufferedTokenStream import TokenStream
from LocalLib.antlr4.ParserRuleContext import ParserRuleContext
from LocalLib.antlr4.Token import Token
from LocalLib.antlr4.tree.Tree import ParseTreeListener, ParseTreeVisitor

if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3 ")
        buf.write("\u009f\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2\u0085\n\2")
        buf.write("\3\3\3\3\3\3\3\3\3\3\5\3\u008c\n\3\3\4\3\4\3\4\7\4\u0091")
        buf.write("\n\4\f\4\16\4\u0094\13\4\5\4\u0096\n\4\3\5\3\5\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\2\2\7\2\4\6\b\n\2\3\3\2\35\37\2\u00b0")
        buf.write("\2\u0084\3\2\2\2\4\u008b\3\2\2\2\6\u0095\3\2\2\2\b\u0097")
        buf.write("\3\2\2\2\n\u0099\3\2\2\2\f\r\7\3\2\2\r\16\5\2\2\2\16\17")
        buf.write("\7\4\2\2\17\u0085\3\2\2\2\20\21\7\5\2\2\21\22\5\b\5\2")
        buf.write("\22\23\7\6\2\2\23\24\5\b\5\2\24\25\7\7\2\2\25\u0085\3")
        buf.write("\2\2\2\26\27\7\5\2\2\27\30\5\b\5\2\30\31\7\b\2\2\31\32")
        buf.write("\5\b\5\2\32\33\7\7\2\2\33\u0085\3\2\2\2\34\35\7\t\2\2")
        buf.write("\35\36\5\4\3\2\36\37\7\n\2\2\37 \5\2\2\2 \u0085\3\2\2")
        buf.write("\2!\"\7\13\2\2\"#\5\4\3\2#$\7\f\2\2$%\5\2\2\2%\u0085\3")
        buf.write("\2\2\2&\'\7\5\2\2\'(\5\4\3\2()\7\7\2\2)*\5\2\2\2*\u0085")
        buf.write("\3\2\2\2+,\7\r\2\2,-\7\36\2\2-.\7\16\2\2.\u0085\5\2\2")
        buf.write("\2/\60\7\17\2\2\60\61\7\36\2\2\61\62\7\16\2\2\62\u0085")
        buf.write("\5\2\2\2\63\64\7\20\2\2\64\65\7\36\2\2\65\66\7\16\2\2")
        buf.write("\66\u0085\5\2\2\2\678\7\21\2\289\7\36\2\29:\7\16\2\2:")
        buf.write("\u0085\5\2\2\2;<\7\22\2\2<=\7\36\2\2=>\7\16\2\2>\u0085")
        buf.write("\5\2\2\2?@\7\23\2\2@A\7\36\2\2AB\7\16\2\2B\u0085\5\2\2")
        buf.write("\2C\u0085\5\n\6\2DE\7\3\2\2EF\5\2\2\2FG\7\24\2\2GH\5\2")
        buf.write("\2\2HI\7\4\2\2I\u0085\3\2\2\2JK\7\3\2\2KL\5\2\2\2LM\7")
        buf.write("\25\2\2MN\5\2\2\2NO\7\4\2\2O\u0085\3\2\2\2PQ\7\3\2\2Q")
        buf.write("R\5\2\2\2RS\7\26\2\2ST\5\2\2\2TU\7\4\2\2U\u0085\3\2\2")
        buf.write("\2VW\7\3\2\2WX\5\2\2\2XY\7\27\2\2YZ\5\2\2\2Z[\7\4\2\2")
        buf.write("[\u0085\3\2\2\2\\]\7\3\2\2]^\7\30\2\2^_\5\n\6\2_`\7\16")
        buf.write("\2\2`a\5\2\2\2ab\7\4\2\2bc\7\3\2\2cd\5\6\4\2de\7\4\2\2")
        buf.write("e\u0085\3\2\2\2fg\7\3\2\2gh\7\31\2\2hi\5\n\6\2ij\7\16")
        buf.write("\2\2jk\5\2\2\2kl\7\4\2\2lm\7\3\2\2mn\5\6\4\2no\7\4\2\2")
        buf.write("o\u0085\3\2\2\2pq\7\3\2\2qr\7\32\2\2rs\5\n\6\2st\7\16")
        buf.write("\2\2tu\5\2\2\2uv\7\4\2\2vw\7\3\2\2wx\5\6\4\2xy\7\4\2\2")
        buf.write("y\u0085\3\2\2\2z{\7\3\2\2{|\7\33\2\2|}\5\n\6\2}~\7\16")
        buf.write("\2\2~\177\5\2\2\2\177\u0080\7\4\2\2\u0080\u0081\7\3\2")
        buf.write("\2\u0081\u0082\5\6\4\2\u0082\u0083\7\4\2\2\u0083\u0085")
        buf.write("\3\2\2\2\u0084\f\3\2\2\2\u0084\20\3\2\2\2\u0084\26\3\2")
        buf.write("\2\2\u0084\34\3\2\2\2\u0084!\3\2\2\2\u0084&\3\2\2\2\u0084")
        buf.write("+\3\2\2\2\u0084/\3\2\2\2\u0084\63\3\2\2\2\u0084\67\3\2")
        buf.write("\2\2\u0084;\3\2\2\2\u0084?\3\2\2\2\u0084C\3\2\2\2\u0084")
        buf.write("D\3\2\2\2\u0084J\3\2\2\2\u0084P\3\2\2\2\u0084V\3\2\2\2")
        buf.write("\u0084\\\3\2\2\2\u0084f\3\2\2\2\u0084p\3\2\2\2\u0084z")
        buf.write("\3\2\2\2\u0085\3\3\2\2\2\u0086\u008c\5\b\5\2\u0087\u0088")
        buf.write("\5\b\5\2\u0088\u0089\7\34\2\2\u0089\u008a\5\b\5\2\u008a")
        buf.write("\u008c\3\2\2\2\u008b\u0086\3\2\2\2\u008b\u0087\3\2\2\2")
        buf.write("\u008c\5\3\2\2\2\u008d\u0092\5\b\5\2\u008e\u008f\7\34")
        buf.write("\2\2\u008f\u0091\5\b\5\2\u0090\u008e\3\2\2\2\u0091\u0094")
        buf.write("\3\2\2\2\u0092\u0090\3\2\2\2\u0092\u0093\3\2\2\2\u0093")
        buf.write("\u0096\3\2\2\2\u0094\u0092\3\2\2\2\u0095\u008d\3\2\2\2")
        buf.write("\u0095\u0096\3\2\2\2\u0096\7\3\2\2\2\u0097\u0098\t\2\2")
        buf.write("\2\u0098\t\3\2\2\2\u0099\u009a\7\36\2\2\u009a\u009b\7")
        buf.write("\3\2\2\u009b\u009c\5\6\4\2\u009c\u009d\7\4\2\2\u009d\13")
        buf.write("\3\2\2\2\6\u0084\u008b\u0092\u0095")
        return buf.getvalue()


class LogicParser ( Parser ):

    grammarFileName = "Logic.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'['", "'='", "']'", "'\u2260'", 
                     "'\u27E8'", "'\u27E9'", "'<'", "'>'", "'\u22C1'", "'.'", 
                     "'\u22C0'", "'\u0418'", "'\\OR'", "'\\AND'", "'\\NEW'", 
                     "'\u2228'", "'\u2227'", "'\\or'", "'\\and'", "'\u03BC'", 
                     "'\u03BD'", "'\\mu'", "'\\nu'", "','", "'*'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "NUMBER", "WS" ]

    RULE_formula = 0
    RULE_label = 1
    RULE_args = 2
    RULE_term = 3
    RULE_var = 4

    ruleNames =  [ "formula", "label", "args", "term", "var" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    ID=28
    NUMBER=29
    WS=30

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class FormulaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LogicParser.RULE_formula

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Diamond2Context(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogicParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def label(self):
            return self.getTypedRuleContext(LogicParser.LabelContext,0)

        def formula(self):
            return self.getTypedRuleContext(LogicParser.FormulaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDiamond2" ):
                listener.enterDiamond2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDiamond2" ):
                listener.exitDiamond2(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDiamond2" ):
                return visitor.visitDiamond2(self)
            else:
                return visitor.visitChildren(self)


    class Fresh2Context(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogicParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(LogicParser.ID, 0)
        def formula(self):
            return self.getTypedRuleContext(LogicParser.FormulaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFresh2" ):
                listener.enterFresh2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFresh2" ):
                listener.exitFresh2(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFresh2" ):
                return visitor.visitFresh2(self)
            else:
                return visitor.visitChildren(self)


    class BigAnd2Context(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogicParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(LogicParser.ID, 0)
        def formula(self):
            return self.getTypedRuleContext(LogicParser.FormulaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBigAnd2" ):
                listener.enterBigAnd2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBigAnd2" ):
                listener.exitBigAnd2(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBigAnd2" ):
                return visitor.visitBigAnd2(self)
            else:
                return visitor.visitChildren(self)


    class ParensContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogicParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self):
            return self.getTypedRuleContext(LogicParser.FormulaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class OrContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogicParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LogicParser.FormulaContext)
            else:
                return self.getTypedRuleContext(LogicParser.FormulaContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOr" ):
                listener.enterOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOr" ):
                listener.exitOr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOr" ):
                return visitor.visitOr(self)
            else:
                return visitor.visitChildren(self)


    class BigAndContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogicParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(LogicParser.ID, 0)
        def formula(self):
            return self.getTypedRuleContext(LogicParser.FormulaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBigAnd" ):
                listener.enterBigAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBigAnd" ):
                listener.exitBigAnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBigAnd" ):
                return visitor.visitBigAnd(self)
            else:
                return visitor.visitChildren(self)


    class NuContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogicParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def var(self):
            return self.getTypedRuleContext(LogicParser.VarContext,0)

        def formula(self):
            return self.getTypedRuleContext(LogicParser.FormulaContext,0)

        def args(self):
            return self.getTypedRuleContext(LogicParser.ArgsContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNu" ):
                listener.enterNu(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNu" ):
                listener.exitNu(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNu" ):
                return visitor.visitNu(self)
            else:
                return visitor.visitChildren(self)


    class MuContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogicParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def var(self):
            return self.getTypedRuleContext(LogicParser.VarContext,0)

        def formula(self):
            return self.getTypedRuleContext(LogicParser.FormulaContext,0)

        def args(self):
            return self.getTypedRuleContext(LogicParser.ArgsContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMu" ):
                listener.enterMu(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMu" ):
                listener.exitMu(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMu" ):
                return visitor.visitMu(self)
            else:
                return visitor.visitChildren(self)


    class BoxContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogicParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def label(self):
            return self.getTypedRuleContext(LogicParser.LabelContext,0)

        def formula(self):
            return self.getTypedRuleContext(LogicParser.FormulaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBox" ):
                listener.enterBox(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBox" ):
                listener.exitBox(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBox" ):
                return visitor.visitBox(self)
            else:
                return visitor.visitChildren(self)


    class Nu2Context(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogicParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def var(self):
            return self.getTypedRuleContext(LogicParser.VarContext,0)

        def formula(self):
            return self.getTypedRuleContext(LogicParser.FormulaContext,0)

        def args(self):
            return self.getTypedRuleContext(LogicParser.ArgsContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNu2" ):
                listener.enterNu2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNu2" ):
                listener.exitNu2(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNu2" ):
                return visitor.visitNu2(self)
            else:
                return visitor.visitChildren(self)


    class Mu2Context(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogicParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def var(self):
            return self.getTypedRuleContext(LogicParser.VarContext,0)

        def formula(self):
            return self.getTypedRuleContext(LogicParser.FormulaContext,0)

        def args(self):
            return self.getTypedRuleContext(LogicParser.ArgsContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMu2" ):
                listener.enterMu2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMu2" ):
                listener.exitMu2(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMu2" ):
                return visitor.visitMu2(self)
            else:
                return visitor.visitChildren(self)


    class EqContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogicParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LogicParser.TermContext)
            else:
                return self.getTypedRuleContext(LogicParser.TermContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEq" ):
                listener.enterEq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEq" ):
                listener.exitEq(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEq" ):
                return visitor.visitEq(self)
            else:
                return visitor.visitChildren(self)


    class Or2Context(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogicParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LogicParser.FormulaContext)
            else:
                return self.getTypedRuleContext(LogicParser.FormulaContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOr2" ):
                listener.enterOr2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOr2" ):
                listener.exitOr2(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOr2" ):
                return visitor.visitOr2(self)
            else:
                return visitor.visitChildren(self)


    class RecVarContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogicParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def var(self):
            return self.getTypedRuleContext(LogicParser.VarContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRecVar" ):
                listener.enterRecVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRecVar" ):
                listener.exitRecVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRecVar" ):
                return visitor.visitRecVar(self)
            else:
                return visitor.visitChildren(self)


    class DiamondContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogicParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def label(self):
            return self.getTypedRuleContext(LogicParser.LabelContext,0)

        def formula(self):
            return self.getTypedRuleContext(LogicParser.FormulaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDiamond" ):
                listener.enterDiamond(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDiamond" ):
                listener.exitDiamond(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDiamond" ):
                return visitor.visitDiamond(self)
            else:
                return visitor.visitChildren(self)


    class BigOrContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogicParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(LogicParser.ID, 0)
        def formula(self):
            return self.getTypedRuleContext(LogicParser.FormulaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBigOr" ):
                listener.enterBigOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBigOr" ):
                listener.exitBigOr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBigOr" ):
                return visitor.visitBigOr(self)
            else:
                return visitor.visitChildren(self)


    class AndContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogicParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LogicParser.FormulaContext)
            else:
                return self.getTypedRuleContext(LogicParser.FormulaContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnd" ):
                listener.enterAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnd" ):
                listener.exitAnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnd" ):
                return visitor.visitAnd(self)
            else:
                return visitor.visitChildren(self)


    class And2Context(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogicParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LogicParser.FormulaContext)
            else:
                return self.getTypedRuleContext(LogicParser.FormulaContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnd2" ):
                listener.enterAnd2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnd2" ):
                listener.exitAnd2(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnd2" ):
                return visitor.visitAnd2(self)
            else:
                return visitor.visitChildren(self)


    class NeqContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogicParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LogicParser.TermContext)
            else:
                return self.getTypedRuleContext(LogicParser.TermContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNeq" ):
                listener.enterNeq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNeq" ):
                listener.exitNeq(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNeq" ):
                return visitor.visitNeq(self)
            else:
                return visitor.visitChildren(self)


    class FreshContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogicParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(LogicParser.ID, 0)
        def formula(self):
            return self.getTypedRuleContext(LogicParser.FormulaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFresh" ):
                listener.enterFresh(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFresh" ):
                listener.exitFresh(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFresh" ):
                return visitor.visitFresh(self)
            else:
                return visitor.visitChildren(self)


    class BigOr2Context(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogicParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(LogicParser.ID, 0)
        def formula(self):
            return self.getTypedRuleContext(LogicParser.FormulaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBigOr2" ):
                listener.enterBigOr2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBigOr2" ):
                listener.exitBigOr2(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBigOr2" ):
                return visitor.visitBigOr2(self)
            else:
                return visitor.visitChildren(self)



    def formula(self):

        localctx = LogicParser.FormulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_formula)
        try:
            self.state = 130
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                localctx = LogicParser.ParensContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 10
                self.match(LogicParser.T__0)
                self.state = 11
                self.formula()
                self.state = 12
                self.match(LogicParser.T__1)
                pass

            elif la_ == 2:
                localctx = LogicParser.EqContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 14
                self.match(LogicParser.T__2)
                self.state = 15
                self.term()
                self.state = 16
                self.match(LogicParser.T__3)
                self.state = 17
                self.term()
                self.state = 18
                self.match(LogicParser.T__4)
                pass

            elif la_ == 3:
                localctx = LogicParser.NeqContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 20
                self.match(LogicParser.T__2)
                self.state = 21
                self.term()
                self.state = 22
                self.match(LogicParser.T__5)
                self.state = 23
                self.term()
                self.state = 24
                self.match(LogicParser.T__4)
                pass

            elif la_ == 4:
                localctx = LogicParser.DiamondContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 26
                self.match(LogicParser.T__6)
                self.state = 27
                self.label()
                self.state = 28
                self.match(LogicParser.T__7)
                self.state = 29
                self.formula()
                pass

            elif la_ == 5:
                localctx = LogicParser.Diamond2Context(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 31
                self.match(LogicParser.T__8)
                self.state = 32
                self.label()
                self.state = 33
                self.match(LogicParser.T__9)
                self.state = 34
                self.formula()
                pass

            elif la_ == 6:
                localctx = LogicParser.BoxContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 36
                self.match(LogicParser.T__2)
                self.state = 37
                self.label()
                self.state = 38
                self.match(LogicParser.T__4)
                self.state = 39
                self.formula()
                pass

            elif la_ == 7:
                localctx = LogicParser.BigOrContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 41
                self.match(LogicParser.T__10)
                self.state = 42
                self.match(LogicParser.ID)
                self.state = 43
                self.match(LogicParser.T__11)
                self.state = 44
                self.formula()
                pass

            elif la_ == 8:
                localctx = LogicParser.BigAndContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 45
                self.match(LogicParser.T__12)
                self.state = 46
                self.match(LogicParser.ID)
                self.state = 47
                self.match(LogicParser.T__11)
                self.state = 48
                self.formula()
                pass

            elif la_ == 9:
                localctx = LogicParser.FreshContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 49
                self.match(LogicParser.T__13)
                self.state = 50
                self.match(LogicParser.ID)
                self.state = 51
                self.match(LogicParser.T__11)
                self.state = 52
                self.formula()
                pass

            elif la_ == 10:
                localctx = LogicParser.BigOr2Context(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 53
                self.match(LogicParser.T__14)
                self.state = 54
                self.match(LogicParser.ID)
                self.state = 55
                self.match(LogicParser.T__11)
                self.state = 56
                self.formula()
                pass

            elif la_ == 11:
                localctx = LogicParser.BigAnd2Context(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 57
                self.match(LogicParser.T__15)
                self.state = 58
                self.match(LogicParser.ID)
                self.state = 59
                self.match(LogicParser.T__11)
                self.state = 60
                self.formula()
                pass

            elif la_ == 12:
                localctx = LogicParser.Fresh2Context(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 61
                self.match(LogicParser.T__16)
                self.state = 62
                self.match(LogicParser.ID)
                self.state = 63
                self.match(LogicParser.T__11)
                self.state = 64
                self.formula()
                pass

            elif la_ == 13:
                localctx = LogicParser.RecVarContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 65
                self.var()
                pass

            elif la_ == 14:
                localctx = LogicParser.OrContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 66
                self.match(LogicParser.T__0)
                self.state = 67
                self.formula()
                self.state = 68
                self.match(LogicParser.T__17)
                self.state = 69
                self.formula()
                self.state = 70
                self.match(LogicParser.T__1)
                pass

            elif la_ == 15:
                localctx = LogicParser.AndContext(self, localctx)
                self.enterOuterAlt(localctx, 15)
                self.state = 72
                self.match(LogicParser.T__0)
                self.state = 73
                self.formula()
                self.state = 74
                self.match(LogicParser.T__18)
                self.state = 75
                self.formula()
                self.state = 76
                self.match(LogicParser.T__1)
                pass

            elif la_ == 16:
                localctx = LogicParser.Or2Context(self, localctx)
                self.enterOuterAlt(localctx, 16)
                self.state = 78
                self.match(LogicParser.T__0)
                self.state = 79
                self.formula()
                self.state = 80
                self.match(LogicParser.T__19)
                self.state = 81
                self.formula()
                self.state = 82
                self.match(LogicParser.T__1)
                pass

            elif la_ == 17:
                localctx = LogicParser.And2Context(self, localctx)
                self.enterOuterAlt(localctx, 17)
                self.state = 84
                self.match(LogicParser.T__0)
                self.state = 85
                self.formula()
                self.state = 86
                self.match(LogicParser.T__20)
                self.state = 87
                self.formula()
                self.state = 88
                self.match(LogicParser.T__1)
                pass

            elif la_ == 18:
                localctx = LogicParser.MuContext(self, localctx)
                self.enterOuterAlt(localctx, 18)
                self.state = 90
                self.match(LogicParser.T__0)
                self.state = 91
                self.match(LogicParser.T__21)
                self.state = 92
                self.var()
                self.state = 93
                self.match(LogicParser.T__11)
                self.state = 94
                self.formula()
                self.state = 95
                self.match(LogicParser.T__1)
                self.state = 96
                self.match(LogicParser.T__0)
                self.state = 97
                self.args()
                self.state = 98
                self.match(LogicParser.T__1)
                pass

            elif la_ == 19:
                localctx = LogicParser.NuContext(self, localctx)
                self.enterOuterAlt(localctx, 19)
                self.state = 100
                self.match(LogicParser.T__0)
                self.state = 101
                self.match(LogicParser.T__22)
                self.state = 102
                self.var()
                self.state = 103
                self.match(LogicParser.T__11)
                self.state = 104
                self.formula()
                self.state = 105
                self.match(LogicParser.T__1)
                self.state = 106
                self.match(LogicParser.T__0)
                self.state = 107
                self.args()
                self.state = 108
                self.match(LogicParser.T__1)
                pass

            elif la_ == 20:
                localctx = LogicParser.Mu2Context(self, localctx)
                self.enterOuterAlt(localctx, 20)
                self.state = 110
                self.match(LogicParser.T__0)
                self.state = 111
                self.match(LogicParser.T__23)
                self.state = 112
                self.var()
                self.state = 113
                self.match(LogicParser.T__11)
                self.state = 114
                self.formula()
                self.state = 115
                self.match(LogicParser.T__1)
                self.state = 116
                self.match(LogicParser.T__0)
                self.state = 117
                self.args()
                self.state = 118
                self.match(LogicParser.T__1)
                pass

            elif la_ == 21:
                localctx = LogicParser.Nu2Context(self, localctx)
                self.enterOuterAlt(localctx, 21)
                self.state = 120
                self.match(LogicParser.T__0)
                self.state = 121
                self.match(LogicParser.T__24)
                self.state = 122
                self.var()
                self.state = 123
                self.match(LogicParser.T__11)
                self.state = 124
                self.formula()
                self.state = 125
                self.match(LogicParser.T__1)
                self.state = 126
                self.match(LogicParser.T__0)
                self.state = 127
                self.args()
                self.state = 128
                self.match(LogicParser.T__1)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LabelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LogicParser.TermContext)
            else:
                return self.getTypedRuleContext(LogicParser.TermContext,i)


        def getRuleIndex(self):
            return LogicParser.RULE_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabel" ):
                listener.enterLabel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabel" ):
                listener.exitLabel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabel" ):
                return visitor.visitLabel(self)
            else:
                return visitor.visitChildren(self)




    def label(self):

        localctx = LogicParser.LabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_label)
        try:
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.term()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 133
                self.term()
                self.state = 134
                self.match(LogicParser.T__25)
                self.state = 135
                self.term()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LogicParser.TermContext)
            else:
                return self.getTypedRuleContext(LogicParser.TermContext,i)


        def getRuleIndex(self):
            return LogicParser.RULE_args

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgs" ):
                listener.enterArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgs" ):
                listener.exitArgs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgs" ):
                return visitor.visitArgs(self)
            else:
                return visitor.visitChildren(self)




    def args(self):

        localctx = LogicParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LogicParser.T__26) | (1 << LogicParser.ID) | (1 << LogicParser.NUMBER))) != 0):
                self.state = 139
                self.term()
                self.state = 144
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==LogicParser.T__25:
                    self.state = 140
                    self.match(LogicParser.T__25)
                    self.state = 141
                    self.term()
                    self.state = 146
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(LogicParser.ID, 0)

        def NUMBER(self):
            return self.getToken(LogicParser.NUMBER, 0)

        def getRuleIndex(self):
            return LogicParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = LogicParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LogicParser.T__26) | (1 << LogicParser.ID) | (1 << LogicParser.NUMBER))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(LogicParser.ID, 0)

        def args(self):
            return self.getTypedRuleContext(LogicParser.ArgsContext,0)


        def getRuleIndex(self):
            return LogicParser.RULE_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)




    def var(self):

        localctx = LogicParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(LogicParser.ID)
            self.state = 152
            self.match(LogicParser.T__0)
            self.state = 153
            self.args()
            self.state = 154
            self.match(LogicParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





