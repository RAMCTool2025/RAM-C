# Generated from logic_parser/Logic.g4 by ANTLR 4.9.2
from LocalLib.antlr4 import *
from LocalLib.antlr4.tree.Tree import ParseTreeVisitor

if __name__ is not None and "." in __name__:
    from .LogicParser import LogicParser
else:
    from LogicParser import LogicParser

# This class defines a complete generic visitor for a parse tree produced by LogicParser.

class LogicVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LogicParser#parens.
    def visitParens(self, ctx:LogicParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogicParser#eq.
    def visitEq(self, ctx:LogicParser.EqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogicParser#neq.
    def visitNeq(self, ctx:LogicParser.NeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogicParser#diamond.
    def visitDiamond(self, ctx:LogicParser.DiamondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogicParser#diamond2.
    def visitDiamond2(self, ctx:LogicParser.Diamond2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogicParser#box.
    def visitBox(self, ctx:LogicParser.BoxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogicParser#bigOr.
    def visitBigOr(self, ctx:LogicParser.BigOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogicParser#bigAnd.
    def visitBigAnd(self, ctx:LogicParser.BigAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogicParser#fresh.
    def visitFresh(self, ctx:LogicParser.FreshContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogicParser#bigOr2.
    def visitBigOr2(self, ctx:LogicParser.BigOr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogicParser#bigAnd2.
    def visitBigAnd2(self, ctx:LogicParser.BigAnd2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogicParser#fresh2.
    def visitFresh2(self, ctx:LogicParser.Fresh2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogicParser#recVar.
    def visitRecVar(self, ctx:LogicParser.RecVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogicParser#or.
    def visitOr(self, ctx:LogicParser.OrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogicParser#and.
    def visitAnd(self, ctx:LogicParser.AndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogicParser#or2.
    def visitOr2(self, ctx:LogicParser.Or2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogicParser#and2.
    def visitAnd2(self, ctx:LogicParser.And2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogicParser#mu.
    def visitMu(self, ctx:LogicParser.MuContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogicParser#nu.
    def visitNu(self, ctx:LogicParser.NuContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogicParser#mu2.
    def visitMu2(self, ctx:LogicParser.Mu2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogicParser#nu2.
    def visitNu2(self, ctx:LogicParser.Nu2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogicParser#label.
    def visitLabel(self, ctx:LogicParser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogicParser#args.
    def visitArgs(self, ctx:LogicParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogicParser#term.
    def visitTerm(self, ctx:LogicParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogicParser#var.
    def visitVar(self, ctx:LogicParser.VarContext):
        return self.visitChildren(ctx)



del LogicParser