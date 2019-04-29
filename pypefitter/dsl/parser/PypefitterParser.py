# Generated from C:/Users/cjones/Documents/pypefitter/antlr4\Pypefitter.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\24")
        buf.write("\65\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4")
        buf.write("\b\t\b\3\2\3\2\3\2\3\3\3\3\5\3\26\n\3\3\3\3\3\3\4\3\4")
        buf.write("\3\4\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\7\b(")
        buf.write("\n\b\f\b\16\b+\13\b\3\b\7\b.\n\b\f\b\16\b\61\13\b\3\b")
        buf.write("\3\b\3\b\2\2\t\2\4\6\b\n\f\16\2\3\3\2\3\4\2\60\2\20\3")
        buf.write("\2\2\2\4\23\3\2\2\2\6\31\3\2\2\2\b\34\3\2\2\2\n\37\3\2")
        buf.write("\2\2\f!\3\2\2\2\16$\3\2\2\2\20\21\7\5\2\2\21\22\5\16\b")
        buf.write("\2\22\3\3\2\2\2\23\25\5\n\6\2\24\26\5\b\5\2\25\24\3\2")
        buf.write("\2\2\25\26\3\2\2\2\26\27\3\2\2\2\27\30\5\6\4\2\30\5\3")
        buf.write("\2\2\2\31\32\7\20\2\2\32\33\7\21\2\2\33\7\3\2\2\2\34\35")
        buf.write("\7\13\2\2\35\36\7\f\2\2\36\t\3\2\2\2\37 \t\2\2\2 \13\3")
        buf.write("\2\2\2!\"\7\6\2\2\"#\5\16\b\2#\r\3\2\2\2$%\7\21\2\2%)")
        buf.write("\7\t\2\2&(\5\4\3\2\'&\3\2\2\2(+\3\2\2\2)\'\3\2\2\2)*\3")
        buf.write("\2\2\2*/\3\2\2\2+)\3\2\2\2,.\5\f\7\2-,\3\2\2\2.\61\3\2")
        buf.write("\2\2/-\3\2\2\2/\60\3\2\2\2\60\62\3\2\2\2\61/\3\2\2\2\62")
        buf.write("\63\7\n\2\2\63\17\3\2\2\2\5\25)/")
        return buf.getvalue()


class PypefitterParser ( Parser ):

    grammarFileName = "Pypefitter.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'on_enter'", "'on_exit'", "'pypefitter'", 
                     "'stage'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
                     "';'", "','", "'.'", "'/'" ]

    symbolicNames = [ "<INVALID>", "ON_ENTER", "ON_EXIT", "PYPEFITTER", 
                      "STAGE", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", 
                      "RBRACK", "SEMI", "COMMA", "DOT", "FSLASH", "Identifier", 
                      "StringLiteral", "WS", "COMMENT" ]

    RULE_pypefitter = 0
    RULE_event_decl = 1
    RULE_event_action = 2
    RULE_event_condition = 3
    RULE_event_type = 4
    RULE_stage = 5
    RULE_stage_body = 6

    ruleNames =  [ "pypefitter", "event_decl", "event_action", "event_condition", 
                   "event_type", "stage", "stage_body" ]

    EOF = Token.EOF
    ON_ENTER=1
    ON_EXIT=2
    PYPEFITTER=3
    STAGE=4
    LPAREN=5
    RPAREN=6
    LBRACE=7
    RBRACE=8
    LBRACK=9
    RBRACK=10
    SEMI=11
    COMMA=12
    DOT=13
    FSLASH=14
    Identifier=15
    StringLiteral=16
    WS=17
    COMMENT=18

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPypefitter" ):
                listener.enterPypefitter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPypefitter" ):
                listener.exitPypefitter(self)




    def pypefitter(self):

        localctx = PypefitterParser.PypefitterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_pypefitter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.match(PypefitterParser.PYPEFITTER)
            self.state = 15
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

        def event_type(self):
            return self.getTypedRuleContext(PypefitterParser.Event_typeContext,0)


        def event_action(self):
            return self.getTypedRuleContext(PypefitterParser.Event_actionContext,0)


        def event_condition(self):
            return self.getTypedRuleContext(PypefitterParser.Event_conditionContext,0)


        def getRuleIndex(self):
            return PypefitterParser.RULE_event_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEvent_decl" ):
                listener.enterEvent_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEvent_decl" ):
                listener.exitEvent_decl(self)




    def event_decl(self):

        localctx = PypefitterParser.Event_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_event_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.event_type()
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PypefitterParser.LBRACK:
                self.state = 18
                self.event_condition()


            self.state = 21
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEvent_action" ):
                listener.enterEvent_action(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEvent_action" ):
                listener.exitEvent_action(self)




    def event_action(self):

        localctx = PypefitterParser.Event_actionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_event_action)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.match(PypefitterParser.FSLASH)
            self.state = 24
            localctx.action = self.match(PypefitterParser.Identifier)
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

        def LBRACK(self):
            return self.getToken(PypefitterParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(PypefitterParser.RBRACK, 0)

        def getRuleIndex(self):
            return PypefitterParser.RULE_event_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEvent_condition" ):
                listener.enterEvent_condition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEvent_condition" ):
                listener.exitEvent_condition(self)




    def event_condition(self):

        localctx = PypefitterParser.Event_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_event_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(PypefitterParser.LBRACK)
            self.state = 27
            self.match(PypefitterParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Event_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ON_ENTER(self):
            return self.getToken(PypefitterParser.ON_ENTER, 0)

        def ON_EXIT(self):
            return self.getToken(PypefitterParser.ON_EXIT, 0)

        def getRuleIndex(self):
            return PypefitterParser.RULE_event_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEvent_type" ):
                listener.enterEvent_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEvent_type" ):
                listener.exitEvent_type(self)




    def event_type(self):

        localctx = PypefitterParser.Event_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_event_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            _la = self._input.LA(1)
            if not(_la==PypefitterParser.ON_ENTER or _la==PypefitterParser.ON_EXIT):
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStage" ):
                listener.enterStage(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStage" ):
                listener.exitStage(self)




    def stage(self):

        localctx = PypefitterParser.StageContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_stage)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(PypefitterParser.STAGE)
            self.state = 32
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStage_body" ):
                listener.enterStage_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStage_body" ):
                listener.exitStage_body(self)




    def stage_body(self):

        localctx = PypefitterParser.Stage_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_stage_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            localctx.name = self.match(PypefitterParser.Identifier)
            self.state = 35
            self.match(PypefitterParser.LBRACE)
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PypefitterParser.ON_ENTER or _la==PypefitterParser.ON_EXIT:
                self.state = 36
                self.event_decl()
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PypefitterParser.STAGE:
                self.state = 42
                self.stage()
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 48
            self.match(PypefitterParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





