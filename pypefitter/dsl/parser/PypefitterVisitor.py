# Generated from C:/Users/cj123/Documents/Github/pypefitter/antlr4\Pypefitter.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PypefitterParser import PypefitterParser
else:
    from PypefitterParser import PypefitterParser

# This class defines a complete generic visitor for a parse tree produced by PypefitterParser.

class PypefitterVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PypefitterParser#pypefitter.
    def visitPypefitter(self, ctx:PypefitterParser.PypefitterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PypefitterParser#stage.
    def visitStage(self, ctx:PypefitterParser.StageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PypefitterParser#stage_body.
    def visitStage_body(self, ctx:PypefitterParser.Stage_bodyContext):
        return self.visitChildren(ctx)



del PypefitterParser