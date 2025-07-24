# Generated from logic_parser/Logic.g4 by ANTLR 4.9.2
from LocalLib.antlr4 import *
from io import StringIO
import sys

from LocalLib.antlr4 import ATNDeserializer, DFA, PredictionContextCache
from LocalLib.antlr4.atn.LexerATNSimulator import LexerATNSimulator

if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2 ")
        buf.write("\u009c\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3")
        buf.write("\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3")
        buf.write("\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\20\3\20\3\21\3")
        buf.write("\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\30\3\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\34\3\34\3\35\3\35\7\35\u0089\n\35\f")
        buf.write("\35\16\35\u008c\13\35\3\36\5\36\u008f\n\36\3\36\6\36\u0092")
        buf.write("\n\36\r\36\16\36\u0093\3\37\6\37\u0097\n\37\r\37\16\37")
        buf.write("\u0098\3\37\3\37\2\2 \3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24")
        buf.write("\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37")
        buf.write("= \3\2\6\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\5\2\13\f\17")
        buf.write("\17\"\"\2\u009f\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\3?\3\2\2\2\5A\3\2\2\2\7C\3\2\2\2\tE\3\2\2\2\13G\3")
        buf.write("\2\2\2\rI\3\2\2\2\17K\3\2\2\2\21M\3\2\2\2\23O\3\2\2\2")
        buf.write("\25Q\3\2\2\2\27S\3\2\2\2\31U\3\2\2\2\33W\3\2\2\2\35Y\3")
        buf.write("\2\2\2\37[\3\2\2\2!_\3\2\2\2#d\3\2\2\2%i\3\2\2\2\'k\3")
        buf.write("\2\2\2)m\3\2\2\2+q\3\2\2\2-v\3\2\2\2/x\3\2\2\2\61z\3\2")
        buf.write("\2\2\63~\3\2\2\2\65\u0082\3\2\2\2\67\u0084\3\2\2\29\u0086")
        buf.write("\3\2\2\2;\u008e\3\2\2\2=\u0096\3\2\2\2?@\7*\2\2@\4\3\2")
        buf.write("\2\2AB\7+\2\2B\6\3\2\2\2CD\7]\2\2D\b\3\2\2\2EF\7?\2\2")
        buf.write("F\n\3\2\2\2GH\7_\2\2H\f\3\2\2\2IJ\7\u2262\2\2J\16\3\2")
        buf.write("\2\2KL\7\u27ea\2\2L\20\3\2\2\2MN\7\u27eb\2\2N\22\3\2\2")
        buf.write("\2OP\7>\2\2P\24\3\2\2\2QR\7@\2\2R\26\3\2\2\2ST\7\u22c3")
        buf.write("\2\2T\30\3\2\2\2UV\7\60\2\2V\32\3\2\2\2WX\7\u22c2\2\2")
        buf.write("X\34\3\2\2\2YZ\7\u041a\2\2Z\36\3\2\2\2[\\\7^\2\2\\]\7")
        buf.write("Q\2\2]^\7T\2\2^ \3\2\2\2_`\7^\2\2`a\7C\2\2ab\7P\2\2bc")
        buf.write("\7F\2\2c\"\3\2\2\2de\7^\2\2ef\7P\2\2fg\7G\2\2gh\7Y\2\2")
        buf.write("h$\3\2\2\2ij\7\u222a\2\2j&\3\2\2\2kl\7\u2229\2\2l(\3\2")
        buf.write("\2\2mn\7^\2\2no\7q\2\2op\7t\2\2p*\3\2\2\2qr\7^\2\2rs\7")
        buf.write("c\2\2st\7p\2\2tu\7f\2\2u,\3\2\2\2vw\7\u03be\2\2w.\3\2")
        buf.write("\2\2xy\7\u03bf\2\2y\60\3\2\2\2z{\7^\2\2{|\7o\2\2|}\7w")
        buf.write("\2\2}\62\3\2\2\2~\177\7^\2\2\177\u0080\7p\2\2\u0080\u0081")
        buf.write("\7w\2\2\u0081\64\3\2\2\2\u0082\u0083\7.\2\2\u0083\66\3")
        buf.write("\2\2\2\u0084\u0085\7,\2\2\u00858\3\2\2\2\u0086\u008a\t")
        buf.write("\2\2\2\u0087\u0089\t\3\2\2\u0088\u0087\3\2\2\2\u0089\u008c")
        buf.write("\3\2\2\2\u008a\u0088\3\2\2\2\u008a\u008b\3\2\2\2\u008b")
        buf.write(":\3\2\2\2\u008c\u008a\3\2\2\2\u008d\u008f\7/\2\2\u008e")
        buf.write("\u008d\3\2\2\2\u008e\u008f\3\2\2\2\u008f\u0091\3\2\2\2")
        buf.write("\u0090\u0092\t\4\2\2\u0091\u0090\3\2\2\2\u0092\u0093\3")
        buf.write("\2\2\2\u0093\u0091\3\2\2\2\u0093\u0094\3\2\2\2\u0094<")
        buf.write("\3\2\2\2\u0095\u0097\t\5\2\2\u0096\u0095\3\2\2\2\u0097")
        buf.write("\u0098\3\2\2\2\u0098\u0096\3\2\2\2\u0098\u0099\3\2\2\2")
        buf.write("\u0099\u009a\3\2\2\2\u009a\u009b\b\37\2\2\u009b>\3\2\2")
        buf.write("\2\7\2\u008a\u008e\u0093\u0098\3\b\2\2")
        return buf.getvalue()


class LogicLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    T__22 = 23
    T__23 = 24
    T__24 = 25
    T__25 = 26
    T__26 = 27
    ID = 28
    NUMBER = 29
    WS = 30

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'['", "'='", "']'", "'\u2260'", "'\u27E8'", "'\u27E9'", 
            "'<'", "'>'", "'\u22C1'", "'.'", "'\u22C0'", "'\u0418'", "'\\OR'", 
            "'\\AND'", "'\\NEW'", "'\u2228'", "'\u2227'", "'\\or'", "'\\and'", 
            "'\u03BC'", "'\u03BD'", "'\\mu'", "'\\nu'", "','", "'*'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "NUMBER", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "T__24", "T__25", 
                  "T__26", "ID", "NUMBER", "WS" ]

    grammarFileName = "Logic.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


