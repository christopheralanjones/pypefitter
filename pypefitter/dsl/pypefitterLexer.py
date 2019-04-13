# Generated from C:/Users/cj123/Documents/Github/pypefitter/antlr4\pypefitter.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("Y\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3")
        buf.write("\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\7\fA\n\f")
        buf.write("\f\f\16\fD\13\f\3\r\3\r\3\16\3\16\3\17\6\17K\n\17\r\17")
        buf.write("\16\17L\3\17\3\17\3\20\3\20\7\20S\n\20\f\20\16\20V\13")
        buf.write("\20\3\20\3\20\2\2\21\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\2\33\2\35\16\37\17\3\2\6\5\2C\\")
        buf.write("aac|\6\2\62;C\\aac|\5\2\13\f\16\17\"\"\4\2\f\f\16\17\2")
        buf.write("Y\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\35\3\2\2\2\2\37\3\2")
        buf.write("\2\2\3!\3\2\2\2\5,\3\2\2\2\7.\3\2\2\2\t\60\3\2\2\2\13")
        buf.write("\62\3\2\2\2\r\64\3\2\2\2\17\66\3\2\2\2\218\3\2\2\2\23")
        buf.write(":\3\2\2\2\25<\3\2\2\2\27>\3\2\2\2\31E\3\2\2\2\33G\3\2")
        buf.write("\2\2\35J\3\2\2\2\37P\3\2\2\2!\"\7r\2\2\"#\7{\2\2#$\7r")
        buf.write("\2\2$%\7g\2\2%&\7h\2\2&\'\7k\2\2\'(\7v\2\2()\7v\2\2)*")
        buf.write("\7g\2\2*+\7t\2\2+\4\3\2\2\2,-\7*\2\2-\6\3\2\2\2./\7+\2")
        buf.write("\2/\b\3\2\2\2\60\61\7}\2\2\61\n\3\2\2\2\62\63\7\177\2")
        buf.write("\2\63\f\3\2\2\2\64\65\7]\2\2\65\16\3\2\2\2\66\67\7_\2")
        buf.write("\2\67\20\3\2\2\289\7=\2\29\22\3\2\2\2:;\7.\2\2;\24\3\2")
        buf.write("\2\2<=\7\60\2\2=\26\3\2\2\2>B\5\31\r\2?A\5\33\16\2@?\3")
        buf.write("\2\2\2AD\3\2\2\2B@\3\2\2\2BC\3\2\2\2C\30\3\2\2\2DB\3\2")
        buf.write("\2\2EF\t\2\2\2F\32\3\2\2\2GH\t\3\2\2H\34\3\2\2\2IK\t\4")
        buf.write("\2\2JI\3\2\2\2KL\3\2\2\2LJ\3\2\2\2LM\3\2\2\2MN\3\2\2\2")
        buf.write("NO\b\17\2\2O\36\3\2\2\2PT\7%\2\2QS\n\5\2\2RQ\3\2\2\2S")
        buf.write("V\3\2\2\2TR\3\2\2\2TU\3\2\2\2UW\3\2\2\2VT\3\2\2\2WX\b")
        buf.write("\20\3\2X \3\2\2\2\6\2BLT\4\b\2\2\2\3\2")
        return buf.getvalue()


class pypefitterLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PYPEFITTER = 1
    LPAREN = 2
    RPAREN = 3
    LBRACE = 4
    RBRACE = 5
    LBRACK = 6
    RBRACK = 7
    SEMI = 8
    COMMA = 9
    DOT = 10
    Identifier = 11
    WS = 12
    COMMENT = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'pypefitter'", "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", 
            "','", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "PYPEFITTER", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", 
            "RBRACK", "SEMI", "COMMA", "DOT", "Identifier", "WS", "COMMENT" ]

    ruleNames = [ "PYPEFITTER", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                  "LBRACK", "RBRACK", "SEMI", "COMMA", "DOT", "Identifier", 
                  "Letter", "LetterOrDigit", "WS", "COMMENT" ]

    grammarFileName = "pypefitter.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


