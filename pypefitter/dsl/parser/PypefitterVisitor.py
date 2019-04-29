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


    # Visit a parse tree produced by PypefitterParser#event_decl.
    def visitEvent_decl(self, ctx:PypefitterParser.Event_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PypefitterParser#event_action.
    def visitEvent_action(self, ctx:PypefitterParser.Event_actionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PypefitterParser#event_condition_decl.
    def visitEvent_condition_decl(self, ctx:PypefitterParser.Event_condition_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PypefitterParser#event_condition.
    def visitEvent_condition(self, ctx:PypefitterParser.Event_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PypefitterParser#event_name.
    def visitEvent_name(self, ctx:PypefitterParser.Event_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PypefitterParser#stage.
    def visitStage(self, ctx:PypefitterParser.StageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PypefitterParser#stage_body.
    def visitStage_body(self, ctx:PypefitterParser.Stage_bodyContext):
        return self.visitChildren(ctx)



del PypefitterParser