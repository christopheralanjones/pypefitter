# Generated from C:/Users/cj123/Documents/Github/pypefitter/antlr4\Pypefitter.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("\31\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\2\3\3\3\3\3\3\3")
        buf.write("\4\3\4\3\4\7\4\22\n\4\f\4\16\4\25\13\4\3\4\3\4\3\4\2\2")
        buf.write("\5\2\4\6\2\2\2\26\2\b\3\2\2\2\4\13\3\2\2\2\6\16\3\2\2")
        buf.write("\2\b\t\7\3\2\2\t\n\5\6\4\2\n\3\3\2\2\2\13\f\7\4\2\2\f")
        buf.write("\r\5\6\4\2\r\5\3\2\2\2\16\17\7\16\2\2\17\23\7\7\2\2\20")
        buf.write("\22\5\4\3\2\21\20\3\2\2\2\22\25\3\2\2\2\23\21\3\2\2\2")
        buf.write("\23\24\3\2\2\2\24\26\3\2\2\2\25\23\3\2\2\2\26\27\7\b\2")
        buf.write("\2\27\7\3\2\2\2\3\23")
        return buf.getvalue()


class PypefitterParser ( Parser ):

    grammarFileName = "Pypefitter.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'pypefitter'", "'stage'", "'('", "')'", 
                     "'{'", "'}'", "'['", "']'", "';'", "','", "'.'" ]

    symbolicNames = [ "<INVALID>", "PYPEFITTER", "STAGE", "LPAREN", "RPAREN", 
                      "LBRACE", "RBRACE", "LBRACK", "RBRACK", "SEMI", "COMMA", 
                      "DOT", "Identifier", "WS", "COMMENT" ]

    RULE_pypefitter = 0
    RULE_stage = 1
    RULE_stage_body = 2

    ruleNames =  [ "pypefitter", "stage", "stage_body" ]

    EOF = Token.EOF
    PYPEFITTER=1
    STAGE=2
    LPAREN=3
    RPAREN=4
    LBRACE=5
    RBRACE=6
    LBRACK=7
    RBRACK=8
    SEMI=9
    COMMA=10
    DOT=11
    Identifier=12
    WS=13
    COMMENT=14

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
            self.state = 6
            self.match(PypefitterParser.PYPEFITTER)
            self.state = 7
            self.stage_body()
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
        self.enterRule(localctx, 2, self.RULE_stage)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            self.match(PypefitterParser.STAGE)
            self.state = 10
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
        self.enterRule(localctx, 4, self.RULE_stage_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            localctx.name = self.match(PypefitterParser.Identifier)
            self.state = 13
            self.match(PypefitterParser.LBRACE)
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PypefitterParser.STAGE:
                self.state = 14
                self.stage()
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 20
            self.match(PypefitterParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





