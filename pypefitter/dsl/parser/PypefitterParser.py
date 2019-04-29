# Generated from C:/Users/cjones/Documents/pypefitter/antlr4\Pypefitter.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\22")
        buf.write("\'\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2")
        buf.write("\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\7\6\32\n\6\f")
        buf.write("\6\16\6\35\13\6\3\6\7\6 \n\6\f\6\16\6#\13\6\3\6\3\6\3")
        buf.write("\6\2\2\7\2\4\6\b\n\2\3\3\2\3\4\2#\2\f\3\2\2\2\4\17\3\2")
        buf.write("\2\2\6\21\3\2\2\2\b\23\3\2\2\2\n\26\3\2\2\2\f\r\7\5\2")
        buf.write("\2\r\16\5\n\6\2\16\3\3\2\2\2\17\20\5\6\4\2\20\5\3\2\2")
        buf.write("\2\21\22\t\2\2\2\22\7\3\2\2\2\23\24\7\6\2\2\24\25\5\n")
        buf.write("\6\2\25\t\3\2\2\2\26\27\7\20\2\2\27\33\7\t\2\2\30\32\5")
        buf.write("\4\3\2\31\30\3\2\2\2\32\35\3\2\2\2\33\31\3\2\2\2\33\34")
        buf.write("\3\2\2\2\34!\3\2\2\2\35\33\3\2\2\2\36 \5\b\5\2\37\36\3")
        buf.write("\2\2\2 #\3\2\2\2!\37\3\2\2\2!\"\3\2\2\2\"$\3\2\2\2#!\3")
        buf.write("\2\2\2$%\7\n\2\2%\13\3\2\2\2\4\33!")
        return buf.getvalue()


class PypefitterParser ( Parser ):

    grammarFileName = "Pypefitter.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'on_enter'", "'on_exit'", "'pypefitter'", 
                     "'stage'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
                     "';'", "','", "'.'" ]

    symbolicNames = [ "<INVALID>", "ON_ENTER", "ON_EXIT", "PYPEFITTER", 
                      "STAGE", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", 
                      "RBRACK", "SEMI", "COMMA", "DOT", "Identifier", "WS", 
                      "COMMENT" ]

    RULE_pypefitter = 0
    RULE_event_decl = 1
    RULE_event_type = 2
    RULE_stage = 3
    RULE_stage_body = 4

    ruleNames =  [ "pypefitter", "event_decl", "event_type", "stage", "stage_body" ]

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
    Identifier=14
    WS=15
    COMMENT=16

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
            self.state = 10
            self.match(PypefitterParser.PYPEFITTER)
            self.state = 11
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self.event_type()
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
        self.enterRule(localctx, 4, self.RULE_event_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
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
        self.enterRule(localctx, 6, self.RULE_stage)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.match(PypefitterParser.STAGE)
            self.state = 18
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
        self.enterRule(localctx, 8, self.RULE_stage_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            localctx.name = self.match(PypefitterParser.Identifier)
            self.state = 21
            self.match(PypefitterParser.LBRACE)
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PypefitterParser.ON_ENTER or _la==PypefitterParser.ON_EXIT:
                self.state = 22
                self.event_decl()
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PypefitterParser.STAGE:
                self.state = 28
                self.stage()
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 34
            self.match(PypefitterParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





