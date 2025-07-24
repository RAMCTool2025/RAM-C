from LocalLib.antlr4 import *
if __name__ is not None and "." in __name__:
    from .LogicVisitor import LogicVisitor
    from .LogicParser import LogicParser
else:
    from LogicVisitor import LogicVisitor
    from LogicParser import LogicParser

class MyLogicVisitor(LogicVisitor):

    # Visit a parse tree produced by LogicParser#parens.
    def visitParens(self, ctx:LogicParser.ParensContext):
        # return self.visitChildren(ctx)
        return self.visit(ctx.formula())

    # Visit a parse tree produced by LogicParser#eq.
    def visitEq(self, ctx:LogicParser.EqContext):
        left = ctx.term(0).getText()
        right = ctx.term(1).getText()
        return {
            "kind": "Eq",
            "left": left,
            "right": right
        }

    # Visit a parse tree produced by LogicParser#neq.
    def visitNeq(self, ctx:LogicParser.NeqContext):
        left = ctx.term(0).getText()
        right = ctx.term(1).getText()
        return {
            "kind": "Neq",
            "left": left,
            "right": right
        }

    # Visit a parse tree produced by LogicParser#diamond.
    def visitDiamond(self, ctx:LogicParser.DiamondContext):
        left = self.visitLabel(ctx.label())
        right = self.visit(ctx.formula())
        return {
            "kind": "Diamond",
            "left": left,
            "right": right
        }

    # Visit a parse tree produced by LogicParser#diamond2.
    def visitDiamond2(self, ctx:LogicParser.Diamond2Context):
        return self.visitDiamond(ctx)
    
    # Visit a parse tree produced by LogicParser#box.
    def visitBox(self, ctx:LogicParser.BoxContext):
        left = self.visitLabel(ctx.label())
        right = self.visit(ctx.formula())
        return {
            "kind": "Box",
            "left": left,
            "right": right
        }

    # Visit a parse tree produced by LogicParser#bigOr.
    def visitBigOr(self, ctx:LogicParser.BigOrContext):
        left = ctx.ID().getText()
        right = self.visit(ctx.formula())
        return {
            "kind": "BigOr",
            "left": left,
            "right": right
        }

    # Visit a parse tree produced by LogicParser#bigAnd.
    def visitBigAnd(self, ctx:LogicParser.BigAndContext):
        left = ctx.ID().getText()
        right = self.visit(ctx.formula())
        return {
            "kind": "BigAnd",
            "left": left,
            "right": right
        }

    # Visit a parse tree produced by LogicParser#fresh.
    def visitFresh(self, ctx:LogicParser.FreshContext):
        left = ctx.ID().getText()
        right = self.visit(ctx.formula())
        return {
            "kind": "Fresh",
            "left": left,
            "right": right
        }
    
    # Visit a parse tree produced by LogicParser#bigOr2.
    def visitBigOr2(self, ctx:LogicParser.BigOr2Context):
        return self.visitBigOr(ctx)

    # Visit a parse tree produced by LogicParser#bigAnd2.
    def visitBigAnd2(self, ctx:LogicParser.BigAnd2Context):
        return self.visitBigAnd(ctx)

    # Visit a parse tree produced by LogicParser#fresh2.
    def visitFresh2(self, ctx:LogicParser.Fresh2Context):
        return self.visitFresh(ctx)
    
    # Visit a parse tree produced by LogicParser#or.
    def visitOr(self, ctx:LogicParser.OrContext):
        left = self.visit(ctx.formula(0))
        right = self.visit(ctx.formula(1))
        return {
            "kind": "Or",
            "left": left,
            "right": right
        }

    # Visit a parse tree produced by LogicParser#and.
    def visitAnd(self, ctx:LogicParser.AndContext):
        left = self.visit(ctx.formula(0))
        right = self.visit(ctx.formula(1))
        return {
            "kind": "And",
            "left": left,
            "right": right
        }

    # Visit a parse tree produced by LogicParser#or2.
    def visitOr2(self, ctx:LogicParser.Or2Context):
        return self.visitOr(ctx)

    # Visit a parse tree produced by LogicParser#and2.
    def visitAnd2(self, ctx:LogicParser.And2Context):
        return self.visitAnd(ctx)
    
    # Visit a parse tree produced by LogicParser#recVar.
    def visitRecVar(self, ctx:LogicParser.RecVarContext):
        return self.visitVar(ctx.var())

    # Visit a parse tree produced by LogicParser#mu.
    def visitMu(self, ctx:LogicParser.MuContext):
        kind = self.visitVar(ctx.var())["kind"]
        left = self.visit(ctx.formula())
        right = self.visitArgs(ctx.args())
        return {
            "kind" : ("Mu",kind[1],kind[2]),
            "left" : left,
            "right": right
        }

    # Visit a parse tree produced by LogicParser#nu.
    def visitNu(self, ctx:LogicParser.NuContext):
        kind = self.visitVar(ctx.var())["kind"]
        left = self.visit(ctx.formula())
        right = self.visitArgs(ctx.args())
        return {
            "kind" : ("Nu",kind[1],kind[2]),
            "left" : left,
            "right": right
        }

    # Visit a parse tree produced by LogicParser#mu2.
    def visitMu2(self, ctx:LogicParser.Mu2Context):
        return self.visitMu(ctx)

    # Visit a parse tree produced by LogicParser#nu2.
    def visitNu2(self, ctx:LogicParser.Nu2Context):
        return self.visitNu(ctx)
    
    # Visit a parse tree produced by LogicParser#label.
    def visitLabel(self, ctx:LogicParser.LabelContext):
        terms = [term.getText() for term in ctx.term()]
        if len(terms)==1: return terms[0]
        return tuple(terms)

    # Visit a parse tree produced by LogicParser#args.
    def visitArgs(self, ctx:LogicParser.ArgsContext):
        terms = [term.getText() for term in ctx.term()]
        return tuple(terms)

    # Visit a parse tree produced by LogicParser#term.
    def visitTerm(self, ctx:LogicParser.TermContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LogicParser#var.
    def visitVar(self, ctx:LogicParser.VarContext):
        X = ctx.ID().getText()
        Xargs = self.visitArgs(ctx.args())
        return {
            "kind": ("Var",X,Xargs) 
        }


del LogicParser
