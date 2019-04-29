# Generated from C:/Users/cj123/Documents/Github/pypefitter/antlr4\Pypefitter.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\26")
        buf.write(">\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\3\2\3\2\3\3\3\3\5\3\30\n\3\3\3\3\3\3")
        buf.write("\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\5\6%\n\6\3\7\3\7\5")
        buf.write("\7)\n\7\3\b\3\b\3\b\3\t\3\t\3\t\7\t\61\n\t\f\t\16\t\64")
        buf.write("\13\t\3\t\7\t\67\n\t\f\t\16\t:\13\t\3\t\3\t\3\t\2\2\n")
        buf.write("\2\4\6\b\n\f\16\20\2\2\2:\2\22\3\2\2\2\4\25\3\2\2\2\6")
        buf.write("\33\3\2\2\2\b\36\3\2\2\2\n$\3\2\2\2\f(\3\2\2\2\16*\3\2")
        buf.write("\2\2\20-\3\2\2\2\22\23\7\6\2\2\23\24\5\20\t\2\24\3\3\2")
        buf.write("\2\2\25\27\5\f\7\2\26\30\5\b\5\2\27\26\3\2\2\2\27\30\3")
        buf.write("\2\2\2\30\31\3\2\2\2\31\32\5\6\4\2\32\5\3\2\2\2\33\34")
        buf.write("\7\22\2\2\34\35\7\23\2\2\35\7\3\2\2\2\36\37\7\r\2\2\37")
        buf.write(" \5\n\6\2 !\7\16\2\2!\t\3\2\2\2\"%\7\3\2\2#%\7\b\2\2$")
        buf.write("\"\3\2\2\2$#\3\2\2\2%\13\3\2\2\2&)\7\4\2\2\')\7\5\2\2")
        buf.write("(&\3\2\2\2(\'\3\2\2\2)\r\3\2\2\2*+\7\7\2\2+,\5\20\t\2")
        buf.write(",\17\3\2\2\2-.\7\23\2\2.\62\7\13\2\2/\61\5\4\3\2\60/\3")
        buf.write("\2\2\2\61\64\3\2\2\2\62\60\3\2\2\2\62\63\3\2\2\2\638\3")
        buf.write("\2\2\2\64\62\3\2\2\2\65\67\5\16\b\2\66\65\3\2\2\2\67:")
        buf.write("\3\2\2\28\66\3\2\2\289\3\2\2\29;\3\2\2\2:8\3\2\2\2;<\7")
        buf.write("\f\2\2<\21\3\2\2\2\7\27$(\628")
        return buf.getvalue()


class PypefitterParser ( Parser ):

    grammarFileName = "Pypefitter.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'failure'", "'on_enter'", "'on_exit'", 
                     "'pypefitter'", "'stage'", "'success'", "'('", "')'", 
                     "'{'", "'}'", "'['", "']'", "';'", "','", "'.'", "'/'" ]

    symbolicNames = [ "<INVALID>", "FAILURE", "ON_ENTER", "ON_EXIT", "PYPEFITTER", 
                      "STAGE", "SUCCESS", "LPAREN", "RPAREN", "LBRACE", 
                      "RBRACE", "LBRACK", "RBRACK", "SEMI", "COMMA", "DOT", 
                      "FSLASH", "Identifier", "StringLiteral", "WS", "COMMENT" ]

    RULE_pypefitter = 0
    RULE_event_decl = 1
    RULE_event_action = 2
    RULE_event_condition_decl = 3
    RULE_event_condition = 4
    RULE_event_name = 5
    RULE_stage = 6
    RULE_stage_body = 7

    ruleNames =  [ "pypefitter", "event_decl", "event_action", "event_condition_decl", 
                   "event_condition", "event_name", "stage", "stage_body" ]

    EOF = Token.EOF
    FAILURE=1
    ON_ENTER=2
    ON_EXIT=3
    PYPEFITTER=4
    STAGE=5
    SUCCESS=6
    LPAREN=7
    RPAREN=8
    LBRACE=9
    RBRACE=10
    LBRACK=11
    RBRACK=12
    SEMI=13
    COMMA=14
    DOT=15
    FSLASH=16
    Identifier=17
    StringLiteral=18
    WS=19
    COMMENT=20

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class PypefitterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PYPEFITTER(self):
            return self.getToken(PypefitterParser.PYPEFITTER, 0)

        def stage_body(self):
            return self.getTypedRuleContext(PypefitterParser.Stage_bodyContext,0)


        def getRuleIndex(self):
            return PypefitterParser.RULE_pypefitter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPypefitter" ):
                return visitor.visitPypefitter(self)
            else:
                return visitor.visitChildren(self)




    def pypefitter(self):

        localctx = PypefitterParser.PypefitterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_pypefitter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.match(PypefitterParser.PYPEFITTER)
            self.state = 17
            self.stage_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Event_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def event_name(self):
            return self.getTypedRuleContext(PypefitterParser.Event_nameContext,0)


        def event_action(self):
            return self.getTypedRuleContext(PypefitterParser.Event_actionContext,0)


        def event_condition_decl(self):
            return self.getTypedRuleContext(PypefitterParser.Event_condition_declContext,0)


        def getRuleIndex(self):
            return PypefitterParser.RULE_event_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEvent_decl" ):
                return visitor.visitEvent_decl(self)
            else:
                return visitor.visitChildren(self)




    def event_decl(self):

        localctx = PypefitterParser.Event_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_event_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.event_name()
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PypefitterParser.LBRACK:
                self.state = 20
                self.event_condition_decl()


            self.state = 23
            self.event_action()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Event_actionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.action = None # Token

        def FSLASH(self):
            return self.getToken(PypefitterParser.FSLASH, 0)

        def Identifier(self):
            return self.getToken(PypefitterParser.Identifier, 0)

        def getRuleIndex(self):
            return PypefitterParser.RULE_event_action

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEvent_action" ):
                return visitor.visitEvent_action(self)
            else:
                return visitor.visitChildren(self)




    def event_action(self):

        localctx = PypefitterParser.Event_actionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_event_action)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(PypefitterParser.FSLASH)
            self.state = 26
            localctx.action = self.match(PypefitterParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Event_condition_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(PypefitterParser.LBRACK, 0)

        def event_condition(self):
            return self.getTypedRuleContext(PypefitterParser.Event_conditionContext,0)


        def RBRACK(self):
            return self.getToken(PypefitterParser.RBRACK, 0)

        def getRuleIndex(self):
            return PypefitterParser.RULE_event_condition_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEvent_condition_decl" ):
                return visitor.visitEvent_condition_decl(self)
            else:
                return visitor.visitChildren(self)




    def event_condition_decl(self):

        localctx = PypefitterParser.Event_condition_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_event_condition_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(PypefitterParser.LBRACK)
            self.state = 29
            self.event_condition()
            self.state = 30
            self.match(PypefitterParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Event_conditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token

        def FAILURE(self):
            return self.getToken(PypefitterParser.FAILURE, 0)

        def SUCCESS(self):
            return self.getToken(PypefitterParser.SUCCESS, 0)

        def getRuleIndex(self):
            return PypefitterParser.RULE_event_condition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEvent_condition" ):
                return visitor.visitEvent_condition(self)
            else:
                return visitor.visitChildren(self)




    def event_condition(self):

        localctx = PypefitterParser.Event_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_event_condition)
        try:
            self.state = 34
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PypefitterParser.FAILURE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                localctx.name = self.match(PypefitterParser.FAILURE)
                pass
            elif token in [PypefitterParser.SUCCESS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 33
                localctx.name = self.match(PypefitterParser.SUCCESS)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Event_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token

        def ON_ENTER(self):
            return self.getToken(PypefitterParser.ON_ENTER, 0)

        def ON_EXIT(self):
            return self.getToken(PypefitterParser.ON_EXIT, 0)

        def getRuleIndex(self):
            return PypefitterParser.RULE_event_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEvent_name" ):
                return visitor.visitEvent_name(self)
            else:
                return visitor.visitChildren(self)




    def event_name(self):

        localctx = PypefitterParser.Event_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_event_name)
        try:
            self.state = 38
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PypefitterParser.ON_ENTER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 36
                localctx.name = self.match(PypefitterParser.ON_ENTER)
                pass
            elif token in [PypefitterParser.ON_EXIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 37
                localctx.name = self.match(PypefitterParser.ON_EXIT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StageContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAGE(self):
            return self.getToken(PypefitterParser.STAGE, 0)

        def stage_body(self):
            return self.getTypedRuleContext(PypefitterParser.Stage_bodyContext,0)


        def getRuleIndex(self):
            return PypefitterParser.RULE_stage

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStage" ):
                return visitor.visitStage(self)
            else:
                return visitor.visitChildren(self)




    def stage(self):

        localctx = PypefitterParser.StageContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_stage)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(PypefitterParser.STAGE)
            self.state = 41
            self.stage_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stage_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token

        def LBRACE(self):
            return self.getToken(PypefitterParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(PypefitterParser.RBRACE, 0)

        def Identifier(self):
            return self.getToken(PypefitterParser.Identifier, 0)

        def event_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PypefitterParser.Event_declContext)
            else:
                return self.getTypedRuleContext(PypefitterParser.Event_declContext,i)


        def stage(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PypefitterParser.StageContext)
            else:
                return self.getTypedRuleContext(PypefitterParser.StageContext,i)


        def getRuleIndex(self):
            return PypefitterParser.RULE_stage_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStage_body" ):
                return visitor.visitStage_body(self)
            else:
                return visitor.visitChildren(self)




    def stage_body(self):

        localctx = PypefitterParser.Stage_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_stage_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            localctx.name = self.match(PypefitterParser.Identifier)
            self.state = 44
            self.match(PypefitterParser.LBRACE)
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PypefitterParser.ON_ENTER or _la==PypefitterParser.ON_EXIT:
                self.state = 45
                self.event_decl()
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PypefitterParser.STAGE:
                self.state = 51
                self.stage()
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 57
            self.match(PypefitterParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





