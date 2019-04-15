# Generated from C:/Users/cj123/Documents/Github/pypefitter/antlr4\Pypefitter.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("\t\4\2\t\2\3\2\3\2\3\2\3\2\3\2\2\2\3\2\2\2\2\7\2\4\3\2")
        buf.write("\2\2\4\5\7\3\2\2\5\6\7\6\2\2\6\7\7\7\2\2\7\3\3\2\2\2\2")
        return buf.getvalue()


class PypefitterParser ( Parser ):

    grammarFileName = "Pypefitter.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'pypefitter'", "'('", "')'", "'{'", "'}'", 
                     "'['", "']'", "';'", "','", "'.'" ]

    symbolicNames = [ "<INVALID>", "PYPEFITTER", "LPAREN", "RPAREN", "LBRACE", 
                      "RBRACE", "LBRACK", "RBRACK", "SEMI", "COMMA", "DOT", 
                      "Identifier", "WS", "COMMENT" ]

    RULE_pypefitter = 0

    ruleNames =  [ "pypefitter" ]

    EOF = Token.EOF
    PYPEFITTER=1
    LPAREN=2
    RPAREN=3
    LBRACE=4
    RBRACE=5
    LBRACK=6
    RBRACK=7
    SEMI=8
    COMMA=9
    DOT=10
    Identifier=11
    WS=12
    COMMENT=13

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

        def LBRACE(self):
            return self.getToken(PypefitterParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(PypefitterParser.RBRACE, 0)

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
            self.state = 2
            self.match(PypefitterParser.PYPEFITTER)
            self.state = 3
            self.match(PypefitterParser.LBRACE)
            self.state = 4
            self.match(PypefitterParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





