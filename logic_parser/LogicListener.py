# Generated from logic_parser/Logic.g4 by ANTLR 4.9.2
from LocalLib.antlr4 import *
if __name__ is not None and "." in __name__:
    from .LogicParser import LogicParser
else:
    from LogicParser import LogicParser

# This class defines a complete listener for a parse tree produced by LogicParser.
class LogicListener(ParseTreeListener):

    # Enter a parse tree produced by LogicParser#parens.
    def enterParens(self, ctx:LogicParser.ParensContext):
        pass

    # Exit a parse tree produced by LogicParser#parens.
    def exitParens(self, ctx:LogicParser.ParensContext):
        pass


    # Enter a parse tree produced by LogicParser#eq.
    def enterEq(self, ctx:LogicParser.EqContext):
        pass

    # Exit a parse tree produced by LogicParser#eq.
    def exitEq(self, ctx:LogicParser.EqContext):
        pass


    # Enter a parse tree produced by LogicParser#neq.
    def enterNeq(self, ctx:LogicParser.NeqContext):
        pass

    # Exit a parse tree produced by LogicParser#neq.
    def exitNeq(self, ctx:LogicParser.NeqContext):
        pass


    # Enter a parse tree produced by LogicParser#diamond.
    def enterDiamond(self, ctx:LogicParser.DiamondContext):
        pass

    # Exit a parse tree produced by LogicParser#diamond.
    def exitDiamond(self, ctx:LogicParser.DiamondContext):
        pass


    # Enter a parse tree produced by LogicParser#diamond2.
    def enterDiamond2(self, ctx:LogicParser.Diamond2Context):
        pass

    # Exit a parse tree produced by LogicParser#diamond2.
    def exitDiamond2(self, ctx:LogicParser.Diamond2Context):
        pass


    # Enter a parse tree produced by LogicParser#box.
    def enterBox(self, ctx:LogicParser.BoxContext):
        pass

    # Exit a parse tree produced by LogicParser#box.
    def exitBox(self, ctx:LogicParser.BoxContext):
        pass


    # Enter a parse tree produced by LogicParser#bigOr.
    def enterBigOr(self, ctx:LogicParser.BigOrContext):
        pass

    # Exit a parse tree produced by LogicParser#bigOr.
    def exitBigOr(self, ctx:LogicParser.BigOrContext):
        pass


    # Enter a parse tree produced by LogicParser#bigAnd.
    def enterBigAnd(self, ctx:LogicParser.BigAndContext):
        pass

    # Exit a parse tree produced by LogicParser#bigAnd.
    def exitBigAnd(self, ctx:LogicParser.BigAndContext):
        pass


    # Enter a parse tree produced by LogicParser#fresh.
    def enterFresh(self, ctx:LogicParser.FreshContext):
        pass

    # Exit a parse tree produced by LogicParser#fresh.
    def exitFresh(self, ctx:LogicParser.FreshContext):
        pass


    # Enter a parse tree produced by LogicParser#bigOr2.
    def enterBigOr2(self, ctx:LogicParser.BigOr2Context):
        pass

    # Exit a parse tree produced by LogicParser#bigOr2.
    def exitBigOr2(self, ctx:LogicParser.BigOr2Context):
        pass


    # Enter a parse tree produced by LogicParser#bigAnd2.
    def enterBigAnd2(self, ctx:LogicParser.BigAnd2Context):
        pass

    # Exit a parse tree produced by LogicParser#bigAnd2.
    def exitBigAnd2(self, ctx:LogicParser.BigAnd2Context):
        pass


    # Enter a parse tree produced by LogicParser#fresh2.
    def enterFresh2(self, ctx:LogicParser.Fresh2Context):
        pass

    # Exit a parse tree produced by LogicParser#fresh2.
    def exitFresh2(self, ctx:LogicParser.Fresh2Context):
        pass


    # Enter a parse tree produced by LogicParser#recVar.
    def enterRecVar(self, ctx:LogicParser.RecVarContext):
        pass

    # Exit a parse tree produced by LogicParser#recVar.
    def exitRecVar(self, ctx:LogicParser.RecVarContext):
        pass


    # Enter a parse tree produced by LogicParser#or.
    def enterOr(self, ctx:LogicParser.OrContext):
        pass

    # Exit a parse tree produced by LogicParser#or.
    def exitOr(self, ctx:LogicParser.OrContext):
        pass


    # Enter a parse tree produced by LogicParser#and.
    def enterAnd(self, ctx:LogicParser.AndContext):
        pass

    # Exit a parse tree produced by LogicParser#and.
    def exitAnd(self, ctx:LogicParser.AndContext):
        pass


    # Enter a parse tree produced by LogicParser#or2.
    def enterOr2(self, ctx:LogicParser.Or2Context):
        pass

    # Exit a parse tree produced by LogicParser#or2.
    def exitOr2(self, ctx:LogicParser.Or2Context):
        pass


    # Enter a parse tree produced by LogicParser#and2.
    def enterAnd2(self, ctx:LogicParser.And2Context):
        pass

    # Exit a parse tree produced by LogicParser#and2.
    def exitAnd2(self, ctx:LogicParser.And2Context):
        pass


    # Enter a parse tree produced by LogicParser#mu.
    def enterMu(self, ctx:LogicParser.MuContext):
        pass

    # Exit a parse tree produced by LogicParser#mu.
    def exitMu(self, ctx:LogicParser.MuContext):
        pass


    # Enter a parse tree produced by LogicParser#nu.
    def enterNu(self, ctx:LogicParser.NuContext):
        pass

    # Exit a parse tree produced by LogicParser#nu.
    def exitNu(self, ctx:LogicParser.NuContext):
        pass


    # Enter a parse tree produced by LogicParser#mu2.
    def enterMu2(self, ctx:LogicParser.Mu2Context):
        pass

    # Exit a parse tree produced by LogicParser#mu2.
    def exitMu2(self, ctx:LogicParser.Mu2Context):
        pass


    # Enter a parse tree produced by LogicParser#nu2.
    def enterNu2(self, ctx:LogicParser.Nu2Context):
        pass

    # Exit a parse tree produced by LogicParser#nu2.
    def exitNu2(self, ctx:LogicParser.Nu2Context):
        pass


    # Enter a parse tree produced by LogicParser#label.
    def enterLabel(self, ctx:LogicParser.LabelContext):
        pass

    # Exit a parse tree produced by LogicParser#label.
    def exitLabel(self, ctx:LogicParser.LabelContext):
        pass


    # Enter a parse tree produced by LogicParser#args.
    def enterArgs(self, ctx:LogicParser.ArgsContext):
        pass

    # Exit a parse tree produced by LogicParser#args.
    def exitArgs(self, ctx:LogicParser.ArgsContext):
        pass


    # Enter a parse tree produced by LogicParser#term.
    def enterTerm(self, ctx:LogicParser.TermContext):
        pass

    # Exit a parse tree produced by LogicParser#term.
    def exitTerm(self, ctx:LogicParser.TermContext):
        pass


    # Enter a parse tree produced by LogicParser#var.
    def enterVar(self, ctx:LogicParser.VarContext):
        pass

    # Exit a parse tree produced by LogicParser#var.
    def exitVar(self, ctx:LogicParser.VarContext):
        pass



del LogicParser
