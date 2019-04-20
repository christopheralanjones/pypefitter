# Generated from C:/Users/cj123/Documents/Github/pypefitter/antlr4\Pypefitter.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20")
        buf.write("a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4")
        buf.write("\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3")
        buf.write("\13\3\13\3\f\3\f\3\r\3\r\7\rI\n\r\f\r\16\rL\13\r\3\16")
        buf.write("\3\16\3\17\3\17\3\20\6\20S\n\20\r\20\16\20T\3\20\3\20")
        buf.write("\3\21\3\21\7\21[\n\21\f\21\16\21^\13\21\3\21\3\21\2\2")
        buf.write("\22\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\2\35\2\37\17!\20\3\2\6\5\2C\\aac|\6\2\62;C\\")
        buf.write("aac|\5\2\13\f\16\17\"\"\4\2\f\f\16\17\2a\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2")
        buf.write("\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2")
        buf.write("\3#\3\2\2\2\5.\3\2\2\2\7\64\3\2\2\2\t\66\3\2\2\2\138\3")
        buf.write("\2\2\2\r:\3\2\2\2\17<\3\2\2\2\21>\3\2\2\2\23@\3\2\2\2")
        buf.write("\25B\3\2\2\2\27D\3\2\2\2\31F\3\2\2\2\33M\3\2\2\2\35O\3")
        buf.write("\2\2\2\37R\3\2\2\2!X\3\2\2\2#$\7r\2\2$%\7{\2\2%&\7r\2")
        buf.write("\2&\'\7g\2\2\'(\7h\2\2()\7k\2\2)*\7v\2\2*+\7v\2\2+,\7")
        buf.write("g\2\2,-\7t\2\2-\4\3\2\2\2./\7u\2\2/\60\7v\2\2\60\61\7")
        buf.write("c\2\2\61\62\7i\2\2\62\63\7g\2\2\63\6\3\2\2\2\64\65\7*")
        buf.write("\2\2\65\b\3\2\2\2\66\67\7+\2\2\67\n\3\2\2\289\7}\2\29")
        buf.write("\f\3\2\2\2:;\7\177\2\2;\16\3\2\2\2<=\7]\2\2=\20\3\2\2")
        buf.write("\2>?\7_\2\2?\22\3\2\2\2@A\7=\2\2A\24\3\2\2\2BC\7.\2\2")
        buf.write("C\26\3\2\2\2DE\7\60\2\2E\30\3\2\2\2FJ\5\33\16\2GI\5\35")
        buf.write("\17\2HG\3\2\2\2IL\3\2\2\2JH\3\2\2\2JK\3\2\2\2K\32\3\2")
        buf.write("\2\2LJ\3\2\2\2MN\t\2\2\2N\34\3\2\2\2OP\t\3\2\2P\36\3\2")
        buf.write("\2\2QS\t\4\2\2RQ\3\2\2\2ST\3\2\2\2TR\3\2\2\2TU\3\2\2\2")
        buf.write("UV\3\2\2\2VW\b\20\2\2W \3\2\2\2X\\\7%\2\2Y[\n\5\2\2ZY")
        buf.write("\3\2\2\2[^\3\2\2\2\\Z\3\2\2\2\\]\3\2\2\2]_\3\2\2\2^\\")
        buf.write("\3\2\2\2_`\b\21\3\2`\"\3\2\2\2\6\2JT\\\4\b\2\2\2\3\2")
        return buf.getvalue()


class PypefitterLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PYPEFITTER = 1
    STAGE = 2
    LPAREN = 3
    RPAREN = 4
    LBRACE = 5
    RBRACE = 6
    LBRACK = 7
    RBRACK = 8
    SEMI = 9
    COMMA = 10
    DOT = 11
    Identifier = 12
    WS = 13
    COMMENT = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'pypefitter'", "'stage'", "'('", "')'", "'{'", "'}'", "'['", 
            "']'", "';'", "','", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "PYPEFITTER", "STAGE", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
            "LBRACK", "RBRACK", "SEMI", "COMMA", "DOT", "Identifier", "WS", 
            "COMMENT" ]

    ruleNames = [ "PYPEFITTER", "STAGE", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                  "LBRACK", "RBRACK", "SEMI", "COMMA", "DOT", "Identifier", 
                  "Letter", "LetterOrDigit", "WS", "COMMENT" ]

    grammarFileName = "Pypefitter.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


