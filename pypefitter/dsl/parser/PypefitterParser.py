# Generated from C:/Users/cj123/Documents/Github/pypefitter/antlr4\Pypefitter.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\22")
        buf.write("!\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\2\3\2\7\2\r\n\2\f")
        buf.write("\2\16\2\20\13\2\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\4\7\4\32")
        buf.write("\n\4\f\4\16\4\35\13\4\3\4\3\4\3\4\2\2\5\2\4\6\2\2\2\37")
        buf.write("\2\b\3\2\2\2\4\23\3\2\2\2\6\26\3\2\2\2\b\t\7\3\2\2\t\n")
        buf.write("\7\17\2\2\n\16\7\7\2\2\13\r\5\4\3\2\f\13\3\2\2\2\r\20")
        buf.write("\3\2\2\2\16\f\3\2\2\2\16\17\3\2\2\2\17\21\3\2\2\2\20\16")
        buf.write("\3\2\2\2\21\22\7\b\2\2\22\3\3\2\2\2\23\24\7\4\2\2\24\25")
        buf.write("\5\6\4\2\25\5\3\2\2\2\26\27\7\17\2\2\27\33\7\7\2\2\30")
        buf.write("\32\5\4\3\2\31\30\3\2\2\2\32\35\3\2\2\2\33\31\3\2\2\2")
        buf.write("\33\34\3\2\2\2\34\36\3\2\2\2\35\33\3\2\2\2\36\37\7\b\2")
        buf.write("\2\37\7\3\2\2\2\4\16\33")
        return buf.getvalue()


class PypefitterParser ( Parser ):

    grammarFileName = "Pypefitter.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'pypefitter'", "'stage'", "'('", "')'", 
                     "'{'", "'}'", "'['", "']'", "';'", "','", "'.'", "'/'" ]

    symbolicNames = [ "<INVALID>", "PYPEFITTER", "STAGE", "LPAREN", "RPAREN", 
                      "LBRACE", "RBRACE", "LBRACK", "RBRACK", "SEMI", "COMMA", 
                      "DOT", "FSLASH", "Identifier", "StringLiteral", "WS", 
                      "COMMENT" ]

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
    FSLASH=12
    Identifier=13
    StringLiteral=14
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
            self.name = None # Token

        def PYPEFITTER(self):
            return self.getToken(PypefitterParser.PYPEFITTER, 0)

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
            return PypefitterParser.RULE_pypefitter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPypefitter" ):
                return visitor.visitPypefitter(self)
            else:
                return visitor.visitChildren(self)




    def pypefitter(self):

        localctx = PypefitterParser.PypefitterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_pypefitter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.match(PypefitterParser.PYPEFITTER)
            self.state = 7
            localctx.name = self.match(PypefitterParser.Identifier)
            self.state = 8
            self.match(PypefitterParser.LBRACE)
            self.state = 12
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PypefitterParser.STAGE:
                self.state = 9
                self.stage()
                self.state = 14
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 15
            self.match(PypefitterParser.RBRACE)
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
            self.state = 20
            localctx.name = self.match(PypefitterParser.Identifier)
            self.state = 21
            self.match(PypefitterParser.LBRACE)
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PypefitterParser.STAGE:
                self.state = 22
                self.stage()
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 28
            self.match(PypefitterParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





