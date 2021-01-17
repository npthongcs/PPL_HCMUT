# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3E")
        buf.write("\u01bd\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\5\3")
        buf.write("j\n\3\3\4\3\4\3\4\3\4\3\4\5\4q\n\4\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\6\3\6\3\6\3\6\3\6\5\6}\n\6\3\7\3\7\3\7\5\7\u0082\n")
        buf.write("\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t")
        buf.write("\u0090\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u009a\n")
        buf.write("\n\3\13\3\13\3\13\3\13\3\13\5\13\u00a1\n\13\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\5\f\u00a9\n\f\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\5\r\u00c0\n\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\17\5\17\u00cb\n\17\3\20\3\20\5\20\u00cf\n\20\3")
        buf.write("\21\3\21\3\21\3\21\3\21\5\21\u00d6\n\21\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u00e1\n\22\3\23\3")
        buf.write("\23\3\23\3\23\3\23\3\24\3\24\5\24\u00ea\n\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\5\26\u00fe\n\26\3\27\3\27\3")
        buf.write("\27\3\27\3\27\5\27\u0105\n\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35")
        buf.write("\u0137\n\35\3\36\3\36\3\36\3\36\3\36\5\36\u013e\n\36\3")
        buf.write("\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\5\37\u0148\n\37")
        buf.write("\3 \3 \3 \3 \3 \5 \u014f\n \3!\3!\3!\3!\3!\3!\5!\u0157")
        buf.write("\n!\3\"\3\"\3\"\3\"\6\"\u015d\n\"\r\"\16\"\u015e\3#\3")
        buf.write("#\3#\3#\3#\5#\u0166\n#\3$\3$\3$\3$\3$\3$\7$\u016e\n$\f")
        buf.write("$\16$\u0171\13$\3%\3%\3%\3%\3%\3%\7%\u0179\n%\f%\16%\u017c")
        buf.write("\13%\3&\3&\3&\3&\3&\3&\7&\u0184\n&\f&\16&\u0187\13&\3")
        buf.write("\'\3\'\3\'\5\'\u018c\n\'\3(\3(\3(\5(\u0191\n(\3)\3)\3")
        buf.write(")\3)\3)\7)\u0198\n)\f)\16)\u019b\13)\3*\3*\3*\3*\5*\u01a1")
        buf.write("\n*\3+\3+\3,\3,\3,\3,\3,\3,\3,\5,\u01ac\n,\3-\3-\3-\3")
        buf.write("-\3-\3-\3-\5-\u01b5\n-\3.\3.\3/\3/\3\60\3\60\3\60\2\6")
        buf.write("FHJP\61\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*")
        buf.write(",.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^\2\t\3\2)*\3\2\37\"")
        buf.write("\3\2#\'\3\2!\"\4\2++-\66\3\2\5\7\3\2\34\35\2\u01bf\2`")
        buf.write("\3\2\2\2\4i\3\2\2\2\6p\3\2\2\2\br\3\2\2\2\n|\3\2\2\2\f")
        buf.write("\u0081\3\2\2\2\16\u0083\3\2\2\2\20\u008f\3\2\2\2\22\u0099")
        buf.write("\3\2\2\2\24\u00a0\3\2\2\2\26\u00a8\3\2\2\2\30\u00bf\3")
        buf.write("\2\2\2\32\u00c1\3\2\2\2\34\u00ca\3\2\2\2\36\u00ce\3\2")
        buf.write("\2\2 \u00d5\3\2\2\2\"\u00e0\3\2\2\2$\u00e2\3\2\2\2&\u00e9")
        buf.write("\3\2\2\2(\u00eb\3\2\2\2*\u00fd\3\2\2\2,\u0104\3\2\2\2")
        buf.write(".\u0106\3\2\2\2\60\u0116\3\2\2\2\62\u011e\3\2\2\2\64\u0126")
        buf.write("\3\2\2\2\66\u0129\3\2\2\28\u0136\3\2\2\2:\u013d\3\2\2")
        buf.write("\2<\u0147\3\2\2\2>\u014e\3\2\2\2@\u0156\3\2\2\2B\u015c")
        buf.write("\3\2\2\2D\u0165\3\2\2\2F\u0167\3\2\2\2H\u0172\3\2\2\2")
        buf.write("J\u017d\3\2\2\2L\u018b\3\2\2\2N\u0190\3\2\2\2P\u0192\3")
        buf.write("\2\2\2R\u01a0\3\2\2\2T\u01a2\3\2\2\2V\u01ab\3\2\2\2X\u01b4")
        buf.write("\3\2\2\2Z\u01b6\3\2\2\2\\\u01b8\3\2\2\2^\u01ba\3\2\2\2")
        buf.write("`a\5\4\3\2ab\5\6\4\2bc\7\2\2\3c\3\3\2\2\2de\5\b\5\2ef")
        buf.write("\5\4\3\2fj\3\2\2\2gj\5\b\5\2hj\3\2\2\2id\3\2\2\2ig\3\2")
        buf.write("\2\2ih\3\2\2\2j\5\3\2\2\2kl\5\30\r\2lm\5\6\4\2mq\3\2\2")
        buf.write("\2nq\5\30\r\2oq\3\2\2\2pk\3\2\2\2pn\3\2\2\2po\3\2\2\2")
        buf.write("q\7\3\2\2\2rs\7\32\2\2st\7=\2\2tu\5\n\6\2uv\7>\2\2v\t")
        buf.write("\3\2\2\2wx\5\f\7\2xy\7?\2\2yz\5\n\6\2z}\3\2\2\2{}\5\f")
        buf.write("\7\2|w\3\2\2\2|{\3\2\2\2}\13\3\2\2\2~\u0082\7\4\2\2\177")
        buf.write("\u0082\5\16\b\2\u0080\u0082\5\22\n\2\u0081~\3\2\2\2\u0081")
        buf.write("\177\3\2\2\2\u0081\u0080\3\2\2\2\u0082\r\3\2\2\2\u0083")
        buf.write("\u0084\7\4\2\2\u0084\u0085\5\20\t\2\u0085\17\3\2\2\2\u0086")
        buf.write("\u0087\79\2\2\u0087\u0088\5\\/\2\u0088\u0089\7:\2\2\u0089")
        buf.write("\u008a\5\20\t\2\u008a\u0090\3\2\2\2\u008b\u008c\79\2\2")
        buf.write("\u008c\u008d\5\\/\2\u008d\u008e\7:\2\2\u008e\u0090\3\2")
        buf.write("\2\2\u008f\u0086\3\2\2\2\u008f\u008b\3\2\2\2\u0090\21")
        buf.write("\3\2\2\2\u0091\u0092\7\4\2\2\u0092\u0093\7,\2\2\u0093")
        buf.write("\u009a\5X-\2\u0094\u0095\7\4\2\2\u0095\u0096\5\20\t\2")
        buf.write("\u0096\u0097\7,\2\2\u0097\u0098\5X-\2\u0098\u009a\3\2")
        buf.write("\2\2\u0099\u0091\3\2\2\2\u0099\u0094\3\2\2\2\u009a\23")
        buf.write("\3\2\2\2\u009b\u009c\5X-\2\u009c\u009d\7?\2\2\u009d\u009e")
        buf.write("\5\24\13\2\u009e\u00a1\3\2\2\2\u009f\u00a1\5X-\2\u00a0")
        buf.write("\u009b\3\2\2\2\u00a0\u009f\3\2\2\2\u00a1\25\3\2\2\2\u00a2")
        buf.write("\u00a3\7;\2\2\u00a3\u00a4\5\24\13\2\u00a4\u00a5\7<\2\2")
        buf.write("\u00a5\u00a9\3\2\2\2\u00a6\u00a7\7;\2\2\u00a7\u00a9\7")
        buf.write("<\2\2\u00a8\u00a2\3\2\2\2\u00a8\u00a6\3\2\2\2\u00a9\27")
        buf.write("\3\2\2\2\u00aa\u00ab\7\25\2\2\u00ab\u00ac\7=\2\2\u00ac")
        buf.write("\u00ad\7\4\2\2\u00ad\u00ae\5\32\16\2\u00ae\u00af\7\n\2")
        buf.write("\2\u00af\u00b0\7=\2\2\u00b0\u00b1\5\4\3\2\u00b1\u00b2")
        buf.write("\5 \21\2\u00b2\u00b3\7\20\2\2\u00b3\u00b4\7@\2\2\u00b4")
        buf.write("\u00c0\3\2\2\2\u00b5\u00b6\7\25\2\2\u00b6\u00b7\7=\2\2")
        buf.write("\u00b7\u00b8\7\4\2\2\u00b8\u00b9\7\n\2\2\u00b9\u00ba\7")
        buf.write("=\2\2\u00ba\u00bb\5\4\3\2\u00bb\u00bc\5 \21\2\u00bc\u00bd")
        buf.write("\7\20\2\2\u00bd\u00be\7@\2\2\u00be\u00c0\3\2\2\2\u00bf")
        buf.write("\u00aa\3\2\2\2\u00bf\u00b5\3\2\2\2\u00c0\31\3\2\2\2\u00c1")
        buf.write("\u00c2\7\27\2\2\u00c2\u00c3\7=\2\2\u00c3\u00c4\5\34\17")
        buf.write("\2\u00c4\33\3\2\2\2\u00c5\u00c6\5\36\20\2\u00c6\u00c7")
        buf.write("\7?\2\2\u00c7\u00c8\5\34\17\2\u00c8\u00cb\3\2\2\2\u00c9")
        buf.write("\u00cb\5\36\20\2\u00ca\u00c5\3\2\2\2\u00ca\u00c9\3\2\2")
        buf.write("\2\u00cb\35\3\2\2\2\u00cc\u00cf\7\4\2\2\u00cd\u00cf\5")
        buf.write("\16\b\2\u00ce\u00cc\3\2\2\2\u00ce\u00cd\3\2\2\2\u00cf")
        buf.write("\37\3\2\2\2\u00d0\u00d1\5\"\22\2\u00d1\u00d2\5 \21\2\u00d2")
        buf.write("\u00d6\3\2\2\2\u00d3\u00d6\5\"\22\2\u00d4\u00d6\3\2\2")
        buf.write("\2\u00d5\u00d0\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d5\u00d4")
        buf.write("\3\2\2\2\u00d6!\3\2\2\2\u00d7\u00e1\5$\23\2\u00d8\u00e1")
        buf.write("\5(\25\2\u00d9\u00e1\5.\30\2\u00da\u00e1\5\60\31\2\u00db")
        buf.write("\u00e1\5\62\32\2\u00dc\u00e1\5\64\33\2\u00dd\u00e1\5\66")
        buf.write("\34\2\u00de\u00e1\58\35\2\u00df\u00e1\5@!\2\u00e0\u00d7")
        buf.write("\3\2\2\2\u00e0\u00d8\3\2\2\2\u00e0\u00d9\3\2\2\2\u00e0")
        buf.write("\u00da\3\2\2\2\u00e0\u00db\3\2\2\2\u00e0\u00dc\3\2\2\2")
        buf.write("\u00e0\u00dd\3\2\2\2\u00e0\u00de\3\2\2\2\u00e0\u00df\3")
        buf.write("\2\2\2\u00e1#\3\2\2\2\u00e2\u00e3\5&\24\2\u00e3\u00e4")
        buf.write("\7,\2\2\u00e4\u00e5\5D#\2\u00e5\u00e6\7>\2\2\u00e6%\3")
        buf.write("\2\2\2\u00e7\u00ea\5P)\2\u00e8\u00ea\7\4\2\2\u00e9\u00e7")
        buf.write("\3\2\2\2\u00e9\u00e8\3\2\2\2\u00ea\'\3\2\2\2\u00eb\u00ec")
        buf.write("\7\26\2\2\u00ec\u00ed\5D#\2\u00ed\u00ee\7\31\2\2\u00ee")
        buf.write("\u00ef\5\4\3\2\u00ef\u00f0\5 \21\2\u00f0\u00f1\5*\26\2")
        buf.write("\u00f1\u00f2\5,\27\2\u00f2\u00f3\7\21\2\2\u00f3\u00f4")
        buf.write("\7@\2\2\u00f4)\3\2\2\2\u00f5\u00f6\7\17\2\2\u00f6\u00f7")
        buf.write("\5D#\2\u00f7\u00f8\7\31\2\2\u00f8\u00f9\5\4\3\2\u00f9")
        buf.write("\u00fa\5 \21\2\u00fa\u00fb\5*\26\2\u00fb\u00fe\3\2\2\2")
        buf.write("\u00fc\u00fe\3\2\2\2\u00fd\u00f5\3\2\2\2\u00fd\u00fc\3")
        buf.write("\2\2\2\u00fe+\3\2\2\2\u00ff\u0100\7\16\2\2\u0100\u0101")
        buf.write("\5\4\3\2\u0101\u0102\5 \21\2\u0102\u0105\3\2\2\2\u0103")
        buf.write("\u0105\3\2\2\2\u0104\u00ff\3\2\2\2\u0104\u0103\3\2\2\2")
        buf.write("\u0105-\3\2\2\2\u0106\u0107\7\24\2\2\u0107\u0108\7\67")
        buf.write("\2\2\u0108\u0109\7\4\2\2\u0109\u010a\7,\2\2\u010a\u010b")
        buf.write("\5D#\2\u010b\u010c\7?\2\2\u010c\u010d\5D#\2\u010d\u010e")
        buf.write("\7?\2\2\u010e\u010f\5D#\2\u010f\u0110\78\2\2\u0110\u0111")
        buf.write("\7\r\2\2\u0111\u0112\5\4\3\2\u0112\u0113\5 \21\2\u0113")
        buf.write("\u0114\7\22\2\2\u0114\u0115\7@\2\2\u0115/\3\2\2\2\u0116")
        buf.write("\u0117\7\33\2\2\u0117\u0118\5D#\2\u0118\u0119\7\r\2\2")
        buf.write("\u0119\u011a\5\4\3\2\u011a\u011b\5 \21\2\u011b\u011c\7")
        buf.write("\23\2\2\u011c\u011d\7@\2\2\u011d\61\3\2\2\2\u011e\u011f")
        buf.write("\7\r\2\2\u011f\u0120\5\4\3\2\u0120\u0121\5 \21\2\u0121")
        buf.write("\u0122\7\33\2\2\u0122\u0123\5D#\2\u0123\u0124\7\36\2\2")
        buf.write("\u0124\u0125\7@\2\2\u0125\63\3\2\2\2\u0126\u0127\7\13")
        buf.write("\2\2\u0127\u0128\7>\2\2\u0128\65\3\2\2\2\u0129\u012a\7")
        buf.write("\f\2\2\u012a\u012b\7>\2\2\u012b\67\3\2\2\2\u012c\u012d")
        buf.write("\7\4\2\2\u012d\u012e\7\67\2\2\u012e\u012f\5:\36\2\u012f")
        buf.write("\u0130\78\2\2\u0130\u0131\7>\2\2\u0131\u0137\3\2\2\2\u0132")
        buf.write("\u0133\7\4\2\2\u0133\u0134\7\67\2\2\u0134\u0135\78\2\2")
        buf.write("\u0135\u0137\7>\2\2\u0136\u012c\3\2\2\2\u0136\u0132\3")
        buf.write("\2\2\2\u01379\3\2\2\2\u0138\u0139\5D#\2\u0139\u013a\7")
        buf.write("?\2\2\u013a\u013b\5:\36\2\u013b\u013e\3\2\2\2\u013c\u013e")
        buf.write("\5D#\2\u013d\u0138\3\2\2\2\u013d\u013c\3\2\2\2\u013e;")
        buf.write("\3\2\2\2\u013f\u0140\7\4\2\2\u0140\u0141\7\67\2\2\u0141")
        buf.write("\u0142\5> \2\u0142\u0143\78\2\2\u0143\u0148\3\2\2\2\u0144")
        buf.write("\u0145\7\4\2\2\u0145\u0146\7\67\2\2\u0146\u0148\78\2\2")
        buf.write("\u0147\u013f\3\2\2\2\u0147\u0144\3\2\2\2\u0148=\3\2\2")
        buf.write("\2\u0149\u014a\5D#\2\u014a\u014b\7?\2\2\u014b\u014c\5")
        buf.write("> \2\u014c\u014f\3\2\2\2\u014d\u014f\5D#\2\u014e\u0149")
        buf.write("\3\2\2\2\u014e\u014d\3\2\2\2\u014f?\3\2\2\2\u0150\u0151")
        buf.write("\7\30\2\2\u0151\u0152\5D#\2\u0152\u0153\7>\2\2\u0153\u0157")
        buf.write("\3\2\2\2\u0154\u0155\7\30\2\2\u0155\u0157\7>\2\2\u0156")
        buf.write("\u0150\3\2\2\2\u0156\u0154\3\2\2\2\u0157A\3\2\2\2\u0158")
        buf.write("\u0159\79\2\2\u0159\u015a\5D#\2\u015a\u015b\7:\2\2\u015b")
        buf.write("\u015d\3\2\2\2\u015c\u0158\3\2\2\2\u015d\u015e\3\2\2\2")
        buf.write("\u015e\u015c\3\2\2\2\u015e\u015f\3\2\2\2\u015fC\3\2\2")
        buf.write("\2\u0160\u0161\5F$\2\u0161\u0162\5Z.\2\u0162\u0163\5F")
        buf.write("$\2\u0163\u0166\3\2\2\2\u0164\u0166\5F$\2\u0165\u0160")
        buf.write("\3\2\2\2\u0165\u0164\3\2\2\2\u0166E\3\2\2\2\u0167\u0168")
        buf.write("\b$\1\2\u0168\u0169\5H%\2\u0169\u016f\3\2\2\2\u016a\u016b")
        buf.write("\f\4\2\2\u016b\u016c\t\2\2\2\u016c\u016e\5H%\2\u016d\u016a")
        buf.write("\3\2\2\2\u016e\u0171\3\2\2\2\u016f\u016d\3\2\2\2\u016f")
        buf.write("\u0170\3\2\2\2\u0170G\3\2\2\2\u0171\u016f\3\2\2\2\u0172")
        buf.write("\u0173\b%\1\2\u0173\u0174\5J&\2\u0174\u017a\3\2\2\2\u0175")
        buf.write("\u0176\f\4\2\2\u0176\u0177\t\3\2\2\u0177\u0179\5J&\2\u0178")
        buf.write("\u0175\3\2\2\2\u0179\u017c\3\2\2\2\u017a\u0178\3\2\2\2")
        buf.write("\u017a\u017b\3\2\2\2\u017bI\3\2\2\2\u017c\u017a\3\2\2")
        buf.write("\2\u017d\u017e\b&\1\2\u017e\u017f\5L\'\2\u017f\u0185\3")
        buf.write("\2\2\2\u0180\u0181\f\4\2\2\u0181\u0182\t\4\2\2\u0182\u0184")
        buf.write("\5L\'\2\u0183\u0180\3\2\2\2\u0184\u0187\3\2\2\2\u0185")
        buf.write("\u0183\3\2\2\2\u0185\u0186\3\2\2\2\u0186K\3\2\2\2\u0187")
        buf.write("\u0185\3\2\2\2\u0188\u0189\7(\2\2\u0189\u018c\5L\'\2\u018a")
        buf.write("\u018c\5N(\2\u018b\u0188\3\2\2\2\u018b\u018a\3\2\2\2\u018c")
        buf.write("M\3\2\2\2\u018d\u018e\t\5\2\2\u018e\u0191\5N(\2\u018f")
        buf.write("\u0191\5P)\2\u0190\u018d\3\2\2\2\u0190\u018f\3\2\2\2\u0191")
        buf.write("O\3\2\2\2\u0192\u0193\b)\1\2\u0193\u0194\5R*\2\u0194\u0199")
        buf.write("\3\2\2\2\u0195\u0196\f\4\2\2\u0196\u0198\5B\"\2\u0197")
        buf.write("\u0195\3\2\2\2\u0198\u019b\3\2\2\2\u0199\u0197\3\2\2\2")
        buf.write("\u0199\u019a\3\2\2\2\u019aQ\3\2\2\2\u019b\u0199\3\2\2")
        buf.write("\2\u019c\u019d\5<\37\2\u019d\u019e\5T+\2\u019e\u01a1\3")
        buf.write("\2\2\2\u019f\u01a1\5T+\2\u01a0\u019c\3\2\2\2\u01a0\u019f")
        buf.write("\3\2\2\2\u01a1S\3\2\2\2\u01a2\u01a3\5V,\2\u01a3U\3\2\2")
        buf.write("\2\u01a4\u01ac\7\4\2\2\u01a5\u01ac\5X-\2\u01a6\u01a7\7")
        buf.write("\67\2\2\u01a7\u01a8\5D#\2\u01a8\u01a9\78\2\2\u01a9\u01ac")
        buf.write("\3\2\2\2\u01aa\u01ac\5<\37\2\u01ab\u01a4\3\2\2\2\u01ab")
        buf.write("\u01a5\3\2\2\2\u01ab\u01a6\3\2\2\2\u01ab\u01aa\3\2\2\2")
        buf.write("\u01acW\3\2\2\2\u01ad\u01b5\7\b\2\2\u01ae\u01b5\5^\60")
        buf.write("\2\u01af\u01b5\7\5\2\2\u01b0\u01b5\7\7\2\2\u01b1\u01b5")
        buf.write("\7\6\2\2\u01b2\u01b5\7\t\2\2\u01b3\u01b5\5\26\f\2\u01b4")
        buf.write("\u01ad\3\2\2\2\u01b4\u01ae\3\2\2\2\u01b4\u01af\3\2\2\2")
        buf.write("\u01b4\u01b0\3\2\2\2\u01b4\u01b1\3\2\2\2\u01b4\u01b2\3")
        buf.write("\2\2\2\u01b4\u01b3\3\2\2\2\u01b5Y\3\2\2\2\u01b6\u01b7")
        buf.write("\t\6\2\2\u01b7[\3\2\2\2\u01b8\u01b9\t\7\2\2\u01b9]\3\2")
        buf.write("\2\2\u01ba\u01bb\t\b\2\2\u01bb_\3\2\2\2\"ip|\u0081\u008f")
        buf.write("\u0099\u00a0\u00a8\u00bf\u00ca\u00ce\u00d5\u00e0\u00e9")
        buf.write("\u00fd\u0104\u0136\u013d\u0147\u014e\u0156\u015e\u0165")
        buf.write("\u016f\u017a\u0185\u018b\u0190\u0199\u01a0\u01ab\u01b4")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'Body'", "'Break'", "'Continue'", "'Do'", "'Else'", 
                     "'ElseIf'", "'EndBody'", "'EndIf'", "'EndFor'", "'EndWhile'", 
                     "'For'", "'Function'", "'If'", "'Parameter'", "'Return'", 
                     "'Then'", "'Var'", "'While'", "'True'", "'False'", 
                     "'EndDo'", "'+'", "'+.'", "'-'", "'-.'", "'*'", "'*.'", 
                     "'\\'", "'\\.'", "'%'", "'!'", "'&&'", "'||'", "'=='", 
                     "'='", "'!='", "'>'", "'<'", "'>='", "'<='", "'=/='", 
                     "'<.'", "'>.'", "'>=.'", "'<=.'", "'('", "')'", "'['", 
                     "']'", "'{'", "'}'", "':'", "';'", "','", "'.'" ]

    symbolicNames = [ "<INVALID>", "COMMENT", "ID", "DEC", "HEXA", "OCTAL", 
                      "FLOAT", "STRING", "BODY", "BREAK", "CONTINUE", "DO", 
                      "ELSE", "ELSEIF", "ENDBODY", "ENDIF", "ENDFOR", "ENDWHILE", 
                      "FOR", "FUNCTION", "IF", "PARAMETER", "RETURN", "THEN", 
                      "VAR", "WHILE", "TRUE", "FALSE", "ENDDO", "ADD", "ADDF", 
                      "SUB", "SUBF", "MUL", "MULF", "DIV", "DIVF", "MODUL", 
                      "NOT", "AND", "OR", "EQ", "ASS", "NEQ", "GREATER", 
                      "LESS", "GEQ", "LEQ", "NEQF", "LESSF", "GREATERF", 
                      "GEQF", "LEQF", "LP", "RP", "LS", "RS", "LB", "RB", 
                      "COLON", "SM", "CM", "DOT", "WS", "ILLEGAL_ESCAPE", 
                      "UNCLOSE_STRING", "UNTERMINATED_COMMENT", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_list_var_decl = 1
    RULE_list_func_decl = 2
    RULE_var_decl = 3
    RULE_listID = 4
    RULE_typeID = 5
    RULE_typearray = 6
    RULE_dimension = 7
    RULE_init_var = 8
    RULE_unit_array = 9
    RULE_array = 10
    RULE_func_decl = 11
    RULE_parameter = 12
    RULE_list_para = 13
    RULE_typePara = 14
    RULE_list_stm = 15
    RULE_stm = 16
    RULE_assign_stm = 17
    RULE_lhs = 18
    RULE_if_stm = 19
    RULE_list_elseif = 20
    RULE_else_ = 21
    RULE_for_stm = 22
    RULE_while_stm = 23
    RULE_dowhile_stm = 24
    RULE_break_stm = 25
    RULE_continue_stm = 26
    RULE_call_stm = 27
    RULE_para_call_stm = 28
    RULE_call_func = 29
    RULE_para_call_func = 30
    RULE_return_stm = 31
    RULE_index_operators = 32
    RULE_exp = 33
    RULE_exp1 = 34
    RULE_exp2 = 35
    RULE_exp3 = 36
    RULE_exp4 = 37
    RULE_exp5 = 38
    RULE_exp6 = 39
    RULE_exp7 = 40
    RULE_exp8 = 41
    RULE_operand = 42
    RULE_literal = 43
    RULE_relational = 44
    RULE_intlit = 45
    RULE_bool_literal = 46

    ruleNames =  [ "program", "list_var_decl", "list_func_decl", "var_decl", 
                   "listID", "typeID", "typearray", "dimension", "init_var", 
                   "unit_array", "array", "func_decl", "parameter", "list_para", 
                   "typePara", "list_stm", "stm", "assign_stm", "lhs", "if_stm", 
                   "list_elseif", "else_", "for_stm", "while_stm", "dowhile_stm", 
                   "break_stm", "continue_stm", "call_stm", "para_call_stm", 
                   "call_func", "para_call_func", "return_stm", "index_operators", 
                   "exp", "exp1", "exp2", "exp3", "exp4", "exp5", "exp6", 
                   "exp7", "exp8", "operand", "literal", "relational", "intlit", 
                   "bool_literal" ]

    EOF = Token.EOF
    COMMENT=1
    ID=2
    DEC=3
    HEXA=4
    OCTAL=5
    FLOAT=6
    STRING=7
    BODY=8
    BREAK=9
    CONTINUE=10
    DO=11
    ELSE=12
    ELSEIF=13
    ENDBODY=14
    ENDIF=15
    ENDFOR=16
    ENDWHILE=17
    FOR=18
    FUNCTION=19
    IF=20
    PARAMETER=21
    RETURN=22
    THEN=23
    VAR=24
    WHILE=25
    TRUE=26
    FALSE=27
    ENDDO=28
    ADD=29
    ADDF=30
    SUB=31
    SUBF=32
    MUL=33
    MULF=34
    DIV=35
    DIVF=36
    MODUL=37
    NOT=38
    AND=39
    OR=40
    EQ=41
    ASS=42
    NEQ=43
    GREATER=44
    LESS=45
    GEQ=46
    LEQ=47
    NEQF=48
    LESSF=49
    GREATERF=50
    GEQF=51
    LEQF=52
    LP=53
    RP=54
    LS=55
    RS=56
    LB=57
    RB=58
    COLON=59
    SM=60
    CM=61
    DOT=62
    WS=63
    ILLEGAL_ESCAPE=64
    UNCLOSE_STRING=65
    UNTERMINATED_COMMENT=66
    ERROR_CHAR=67

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_var_decl(self):
            return self.getTypedRuleContext(BKITParser.List_var_declContext,0)


        def list_func_decl(self):
            return self.getTypedRuleContext(BKITParser.List_func_declContext,0)


        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.list_var_decl()
            self.state = 95
            self.list_func_decl()
            self.state = 96
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_var_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(BKITParser.Var_declContext,0)


        def list_var_decl(self):
            return self.getTypedRuleContext(BKITParser.List_var_declContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_list_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_var_decl" ):
                return visitor.visitList_var_decl(self)
            else:
                return visitor.visitChildren(self)




    def list_var_decl(self):

        localctx = BKITParser.List_var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_list_var_decl)
        try:
            self.state = 103
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 98
                self.var_decl()
                self.state = 99
                self.list_var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 101
                self.var_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_func_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_decl(self):
            return self.getTypedRuleContext(BKITParser.Func_declContext,0)


        def list_func_decl(self):
            return self.getTypedRuleContext(BKITParser.List_func_declContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_list_func_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_func_decl" ):
                return visitor.visitList_func_decl(self)
            else:
                return visitor.visitChildren(self)




    def list_func_decl(self):

        localctx = BKITParser.List_func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_list_func_decl)
        try:
            self.state = 110
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.func_decl()
                self.state = 106
                self.list_func_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 108
                self.func_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BKITParser.VAR, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def listID(self):
            return self.getTypedRuleContext(BKITParser.ListIDContext,0)


        def SM(self):
            return self.getToken(BKITParser.SM, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = BKITParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_var_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(BKITParser.VAR)
            self.state = 113
            self.match(BKITParser.COLON)
            self.state = 114
            self.listID()
            self.state = 115
            self.match(BKITParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListIDContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeID(self):
            return self.getTypedRuleContext(BKITParser.TypeIDContext,0)


        def CM(self):
            return self.getToken(BKITParser.CM, 0)

        def listID(self):
            return self.getTypedRuleContext(BKITParser.ListIDContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_listID

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListID" ):
                return visitor.visitListID(self)
            else:
                return visitor.visitChildren(self)




    def listID(self):

        localctx = BKITParser.ListIDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_listID)
        try:
            self.state = 122
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.typeID()
                self.state = 118
                self.match(BKITParser.CM)
                self.state = 119
                self.listID()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 121
                self.typeID()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeIDContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def typearray(self):
            return self.getTypedRuleContext(BKITParser.TypearrayContext,0)


        def init_var(self):
            return self.getTypedRuleContext(BKITParser.Init_varContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_typeID

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeID" ):
                return visitor.visitTypeID(self)
            else:
                return visitor.visitChildren(self)




    def typeID(self):

        localctx = BKITParser.TypeIDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_typeID)
        try:
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.match(BKITParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.typearray()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 126
                self.init_var()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypearrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def dimension(self):
            return self.getTypedRuleContext(BKITParser.DimensionContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_typearray

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypearray" ):
                return visitor.visitTypearray(self)
            else:
                return visitor.visitChildren(self)




    def typearray(self):

        localctx = BKITParser.TypearrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_typearray)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(BKITParser.ID)
            self.state = 130
            self.dimension()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimensionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LS(self):
            return self.getToken(BKITParser.LS, 0)

        def intlit(self):
            return self.getTypedRuleContext(BKITParser.IntlitContext,0)


        def RS(self):
            return self.getToken(BKITParser.RS, 0)

        def dimension(self):
            return self.getTypedRuleContext(BKITParser.DimensionContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_dimension

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimension" ):
                return visitor.visitDimension(self)
            else:
                return visitor.visitChildren(self)




    def dimension(self):

        localctx = BKITParser.DimensionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_dimension)
        try:
            self.state = 141
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.match(BKITParser.LS)
                self.state = 133
                self.intlit()
                self.state = 134
                self.match(BKITParser.RS)
                self.state = 135
                self.dimension()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 137
                self.match(BKITParser.LS)
                self.state = 138
                self.intlit()
                self.state = 139
                self.match(BKITParser.RS)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Init_varContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def ASS(self):
            return self.getToken(BKITParser.ASS, 0)

        def literal(self):
            return self.getTypedRuleContext(BKITParser.LiteralContext,0)


        def dimension(self):
            return self.getTypedRuleContext(BKITParser.DimensionContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_init_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit_var" ):
                return visitor.visitInit_var(self)
            else:
                return visitor.visitChildren(self)




    def init_var(self):

        localctx = BKITParser.Init_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_init_var)
        try:
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                self.match(BKITParser.ID)
                self.state = 144
                self.match(BKITParser.ASS)
                self.state = 145
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                self.match(BKITParser.ID)
                self.state = 147
                self.dimension()
                self.state = 148
                self.match(BKITParser.ASS)
                self.state = 149
                self.literal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unit_arrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(BKITParser.LiteralContext,0)


        def CM(self):
            return self.getToken(BKITParser.CM, 0)

        def unit_array(self):
            return self.getTypedRuleContext(BKITParser.Unit_arrayContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_unit_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnit_array" ):
                return visitor.visitUnit_array(self)
            else:
                return visitor.visitChildren(self)




    def unit_array(self):

        localctx = BKITParser.Unit_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_unit_array)
        try:
            self.state = 158
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.literal()
                self.state = 154
                self.match(BKITParser.CM)
                self.state = 155
                self.unit_array()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
                self.literal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def unit_array(self):
            return self.getTypedRuleContext(BKITParser.Unit_arrayContext,0)


        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = BKITParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_array)
        try:
            self.state = 166
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.match(BKITParser.LB)
                self.state = 161
                self.unit_array()
                self.state = 162
                self.match(BKITParser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
                self.match(BKITParser.LB)
                self.state = 165
                self.match(BKITParser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(BKITParser.FUNCTION, 0)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COLON)
            else:
                return self.getToken(BKITParser.COLON, i)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def parameter(self):
            return self.getTypedRuleContext(BKITParser.ParameterContext,0)


        def BODY(self):
            return self.getToken(BKITParser.BODY, 0)

        def list_var_decl(self):
            return self.getTypedRuleContext(BKITParser.List_var_declContext,0)


        def list_stm(self):
            return self.getTypedRuleContext(BKITParser.List_stmContext,0)


        def ENDBODY(self):
            return self.getToken(BKITParser.ENDBODY, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_func_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl" ):
                return visitor.visitFunc_decl(self)
            else:
                return visitor.visitChildren(self)




    def func_decl(self):

        localctx = BKITParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_func_decl)
        try:
            self.state = 189
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self.match(BKITParser.FUNCTION)
                self.state = 169
                self.match(BKITParser.COLON)
                self.state = 170
                self.match(BKITParser.ID)
                self.state = 171
                self.parameter()
                self.state = 172
                self.match(BKITParser.BODY)
                self.state = 173
                self.match(BKITParser.COLON)
                self.state = 174
                self.list_var_decl()
                self.state = 175
                self.list_stm()
                self.state = 176
                self.match(BKITParser.ENDBODY)
                self.state = 177
                self.match(BKITParser.DOT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 179
                self.match(BKITParser.FUNCTION)
                self.state = 180
                self.match(BKITParser.COLON)
                self.state = 181
                self.match(BKITParser.ID)
                self.state = 182
                self.match(BKITParser.BODY)
                self.state = 183
                self.match(BKITParser.COLON)
                self.state = 184
                self.list_var_decl()
                self.state = 185
                self.list_stm()
                self.state = 186
                self.match(BKITParser.ENDBODY)
                self.state = 187
                self.match(BKITParser.DOT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARAMETER(self):
            return self.getToken(BKITParser.PARAMETER, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def list_para(self):
            return self.getTypedRuleContext(BKITParser.List_paraContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = BKITParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(BKITParser.PARAMETER)
            self.state = 192
            self.match(BKITParser.COLON)
            self.state = 193
            self.list_para()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_paraContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typePara(self):
            return self.getTypedRuleContext(BKITParser.TypeParaContext,0)


        def CM(self):
            return self.getToken(BKITParser.CM, 0)

        def list_para(self):
            return self.getTypedRuleContext(BKITParser.List_paraContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_list_para

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_para" ):
                return visitor.visitList_para(self)
            else:
                return visitor.visitChildren(self)




    def list_para(self):

        localctx = BKITParser.List_paraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_list_para)
        try:
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                self.typePara()
                self.state = 196
                self.match(BKITParser.CM)
                self.state = 197
                self.list_para()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 199
                self.typePara()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeParaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def typearray(self):
            return self.getTypedRuleContext(BKITParser.TypearrayContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_typePara

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypePara" ):
                return visitor.visitTypePara(self)
            else:
                return visitor.visitChildren(self)




    def typePara(self):

        localctx = BKITParser.TypeParaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_typePara)
        try:
            self.state = 204
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.match(BKITParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                self.typearray()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stm(self):
            return self.getTypedRuleContext(BKITParser.StmContext,0)


        def list_stm(self):
            return self.getTypedRuleContext(BKITParser.List_stmContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_list_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_stm" ):
                return visitor.visitList_stm(self)
            else:
                return visitor.visitChildren(self)




    def list_stm(self):

        localctx = BKITParser.List_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_list_stm)
        try:
            self.state = 211
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 206
                self.stm()
                self.state = 207
                self.list_stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 209
                self.stm()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_stm(self):
            return self.getTypedRuleContext(BKITParser.Assign_stmContext,0)


        def if_stm(self):
            return self.getTypedRuleContext(BKITParser.If_stmContext,0)


        def for_stm(self):
            return self.getTypedRuleContext(BKITParser.For_stmContext,0)


        def while_stm(self):
            return self.getTypedRuleContext(BKITParser.While_stmContext,0)


        def dowhile_stm(self):
            return self.getTypedRuleContext(BKITParser.Dowhile_stmContext,0)


        def break_stm(self):
            return self.getTypedRuleContext(BKITParser.Break_stmContext,0)


        def continue_stm(self):
            return self.getTypedRuleContext(BKITParser.Continue_stmContext,0)


        def call_stm(self):
            return self.getTypedRuleContext(BKITParser.Call_stmContext,0)


        def return_stm(self):
            return self.getTypedRuleContext(BKITParser.Return_stmContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStm" ):
                return visitor.visitStm(self)
            else:
                return visitor.visitChildren(self)




    def stm(self):

        localctx = BKITParser.StmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_stm)
        try:
            self.state = 222
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                self.assign_stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 214
                self.if_stm()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 215
                self.for_stm()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 216
                self.while_stm()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 217
                self.dowhile_stm()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 218
                self.break_stm()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 219
                self.continue_stm()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 220
                self.call_stm()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 221
                self.return_stm()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(BKITParser.LhsContext,0)


        def ASS(self):
            return self.getToken(BKITParser.ASS, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def SM(self):
            return self.getToken(BKITParser.SM, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_assign_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stm" ):
                return visitor.visitAssign_stm(self)
            else:
                return visitor.visitChildren(self)




    def assign_stm(self):

        localctx = BKITParser.Assign_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_assign_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.lhs()
            self.state = 225
            self.match(BKITParser.ASS)
            self.state = 226
            self.exp()
            self.state = 227
            self.match(BKITParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp6(self):
            return self.getTypedRuleContext(BKITParser.Exp6Context,0)


        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = BKITParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_lhs)
        try:
            self.state = 231
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 229
                self.exp6(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 230
                self.match(BKITParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKITParser.IF, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def THEN(self):
            return self.getToken(BKITParser.THEN, 0)

        def list_var_decl(self):
            return self.getTypedRuleContext(BKITParser.List_var_declContext,0)


        def list_stm(self):
            return self.getTypedRuleContext(BKITParser.List_stmContext,0)


        def list_elseif(self):
            return self.getTypedRuleContext(BKITParser.List_elseifContext,0)


        def else_(self):
            return self.getTypedRuleContext(BKITParser.Else_Context,0)


        def ENDIF(self):
            return self.getToken(BKITParser.ENDIF, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_if_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stm" ):
                return visitor.visitIf_stm(self)
            else:
                return visitor.visitChildren(self)




    def if_stm(self):

        localctx = BKITParser.If_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_if_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(BKITParser.IF)
            self.state = 234
            self.exp()
            self.state = 235
            self.match(BKITParser.THEN)
            self.state = 236
            self.list_var_decl()
            self.state = 237
            self.list_stm()
            self.state = 238
            self.list_elseif()
            self.state = 239
            self.else_()
            self.state = 240
            self.match(BKITParser.ENDIF)
            self.state = 241
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_elseifContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF(self):
            return self.getToken(BKITParser.ELSEIF, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def THEN(self):
            return self.getToken(BKITParser.THEN, 0)

        def list_var_decl(self):
            return self.getTypedRuleContext(BKITParser.List_var_declContext,0)


        def list_stm(self):
            return self.getTypedRuleContext(BKITParser.List_stmContext,0)


        def list_elseif(self):
            return self.getTypedRuleContext(BKITParser.List_elseifContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_list_elseif

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_elseif" ):
                return visitor.visitList_elseif(self)
            else:
                return visitor.visitChildren(self)




    def list_elseif(self):

        localctx = BKITParser.List_elseifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_list_elseif)
        try:
            self.state = 251
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.ELSEIF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 243
                self.match(BKITParser.ELSEIF)
                self.state = 244
                self.exp()
                self.state = 245
                self.match(BKITParser.THEN)
                self.state = 246
                self.list_var_decl()
                self.state = 247
                self.list_stm()
                self.state = 248
                self.list_elseif()
                pass
            elif token in [BKITParser.ELSE, BKITParser.ENDIF]:
                self.enterOuterAlt(localctx, 2)

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


    class Else_Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(BKITParser.ELSE, 0)

        def list_var_decl(self):
            return self.getTypedRuleContext(BKITParser.List_var_declContext,0)


        def list_stm(self):
            return self.getTypedRuleContext(BKITParser.List_stmContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_else_

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_" ):
                return visitor.visitElse_(self)
            else:
                return visitor.visitChildren(self)




    def else_(self):

        localctx = BKITParser.Else_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_else_)
        try:
            self.state = 258
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.ELSE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 253
                self.match(BKITParser.ELSE)
                self.state = 254
                self.list_var_decl()
                self.state = 255
                self.list_stm()
                pass
            elif token in [BKITParser.ENDIF]:
                self.enterOuterAlt(localctx, 2)

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


    class For_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKITParser.FOR, 0)

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def ASS(self):
            return self.getToken(BKITParser.ASS, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.CM)
            else:
                return self.getToken(BKITParser.CM, i)

        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def list_var_decl(self):
            return self.getTypedRuleContext(BKITParser.List_var_declContext,0)


        def list_stm(self):
            return self.getTypedRuleContext(BKITParser.List_stmContext,0)


        def ENDFOR(self):
            return self.getToken(BKITParser.ENDFOR, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_for_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stm" ):
                return visitor.visitFor_stm(self)
            else:
                return visitor.visitChildren(self)




    def for_stm(self):

        localctx = BKITParser.For_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_for_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.match(BKITParser.FOR)
            self.state = 261
            self.match(BKITParser.LP)
            self.state = 262
            self.match(BKITParser.ID)
            self.state = 263
            self.match(BKITParser.ASS)
            self.state = 264
            self.exp()
            self.state = 265
            self.match(BKITParser.CM)
            self.state = 266
            self.exp()
            self.state = 267
            self.match(BKITParser.CM)
            self.state = 268
            self.exp()
            self.state = 269
            self.match(BKITParser.RP)
            self.state = 270
            self.match(BKITParser.DO)
            self.state = 271
            self.list_var_decl()
            self.state = 272
            self.list_stm()
            self.state = 273
            self.match(BKITParser.ENDFOR)
            self.state = 274
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def list_var_decl(self):
            return self.getTypedRuleContext(BKITParser.List_var_declContext,0)


        def list_stm(self):
            return self.getTypedRuleContext(BKITParser.List_stmContext,0)


        def ENDWHILE(self):
            return self.getToken(BKITParser.ENDWHILE, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_while_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_stm" ):
                return visitor.visitWhile_stm(self)
            else:
                return visitor.visitChildren(self)




    def while_stm(self):

        localctx = BKITParser.While_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_while_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.match(BKITParser.WHILE)
            self.state = 277
            self.exp()
            self.state = 278
            self.match(BKITParser.DO)
            self.state = 279
            self.list_var_decl()
            self.state = 280
            self.list_stm()
            self.state = 281
            self.match(BKITParser.ENDWHILE)
            self.state = 282
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dowhile_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def list_var_decl(self):
            return self.getTypedRuleContext(BKITParser.List_var_declContext,0)


        def list_stm(self):
            return self.getTypedRuleContext(BKITParser.List_stmContext,0)


        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def ENDDO(self):
            return self.getToken(BKITParser.ENDDO, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_dowhile_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDowhile_stm" ):
                return visitor.visitDowhile_stm(self)
            else:
                return visitor.visitChildren(self)




    def dowhile_stm(self):

        localctx = BKITParser.Dowhile_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_dowhile_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.match(BKITParser.DO)
            self.state = 285
            self.list_var_decl()
            self.state = 286
            self.list_stm()
            self.state = 287
            self.match(BKITParser.WHILE)
            self.state = 288
            self.exp()
            self.state = 289
            self.match(BKITParser.ENDDO)
            self.state = 290
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BKITParser.BREAK, 0)

        def SM(self):
            return self.getToken(BKITParser.SM, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_break_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stm" ):
                return visitor.visitBreak_stm(self)
            else:
                return visitor.visitChildren(self)




    def break_stm(self):

        localctx = BKITParser.Break_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_break_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.match(BKITParser.BREAK)
            self.state = 293
            self.match(BKITParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BKITParser.CONTINUE, 0)

        def SM(self):
            return self.getToken(BKITParser.SM, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_continue_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stm" ):
                return visitor.visitContinue_stm(self)
            else:
                return visitor.visitChildren(self)




    def continue_stm(self):

        localctx = BKITParser.Continue_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_continue_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.match(BKITParser.CONTINUE)
            self.state = 296
            self.match(BKITParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def para_call_stm(self):
            return self.getTypedRuleContext(BKITParser.Para_call_stmContext,0)


        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def SM(self):
            return self.getToken(BKITParser.SM, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_call_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_stm" ):
                return visitor.visitCall_stm(self)
            else:
                return visitor.visitChildren(self)




    def call_stm(self):

        localctx = BKITParser.Call_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_call_stm)
        try:
            self.state = 308
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 298
                self.match(BKITParser.ID)
                self.state = 299
                self.match(BKITParser.LP)
                self.state = 300
                self.para_call_stm()
                self.state = 301
                self.match(BKITParser.RP)
                self.state = 302
                self.match(BKITParser.SM)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 304
                self.match(BKITParser.ID)
                self.state = 305
                self.match(BKITParser.LP)
                self.state = 306
                self.match(BKITParser.RP)
                self.state = 307
                self.match(BKITParser.SM)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Para_call_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def CM(self):
            return self.getToken(BKITParser.CM, 0)

        def para_call_stm(self):
            return self.getTypedRuleContext(BKITParser.Para_call_stmContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_para_call_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara_call_stm" ):
                return visitor.visitPara_call_stm(self)
            else:
                return visitor.visitChildren(self)




    def para_call_stm(self):

        localctx = BKITParser.Para_call_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_para_call_stm)
        try:
            self.state = 315
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 310
                self.exp()
                self.state = 311
                self.match(BKITParser.CM)
                self.state = 312
                self.para_call_stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 314
                self.exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_funcContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def para_call_func(self):
            return self.getTypedRuleContext(BKITParser.Para_call_funcContext,0)


        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_call_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_func" ):
                return visitor.visitCall_func(self)
            else:
                return visitor.visitChildren(self)




    def call_func(self):

        localctx = BKITParser.Call_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_call_func)
        try:
            self.state = 325
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 317
                self.match(BKITParser.ID)
                self.state = 318
                self.match(BKITParser.LP)
                self.state = 319
                self.para_call_func()
                self.state = 320
                self.match(BKITParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 322
                self.match(BKITParser.ID)
                self.state = 323
                self.match(BKITParser.LP)
                self.state = 324
                self.match(BKITParser.RP)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Para_call_funcContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def CM(self):
            return self.getToken(BKITParser.CM, 0)

        def para_call_func(self):
            return self.getTypedRuleContext(BKITParser.Para_call_funcContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_para_call_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara_call_func" ):
                return visitor.visitPara_call_func(self)
            else:
                return visitor.visitChildren(self)




    def para_call_func(self):

        localctx = BKITParser.Para_call_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_para_call_func)
        try:
            self.state = 332
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 327
                self.exp()
                self.state = 328
                self.match(BKITParser.CM)
                self.state = 329
                self.para_call_func()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 331
                self.exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKITParser.RETURN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def SM(self):
            return self.getToken(BKITParser.SM, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_return_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stm" ):
                return visitor.visitReturn_stm(self)
            else:
                return visitor.visitChildren(self)




    def return_stm(self):

        localctx = BKITParser.Return_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_return_stm)
        try:
            self.state = 340
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 334
                self.match(BKITParser.RETURN)
                self.state = 335
                self.exp()
                self.state = 336
                self.match(BKITParser.SM)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 338
                self.match(BKITParser.RETURN)
                self.state = 339
                self.match(BKITParser.SM)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LS(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.LS)
            else:
                return self.getToken(BKITParser.LS, i)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpContext,i)


        def RS(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.RS)
            else:
                return self.getToken(BKITParser.RS, i)

        def getRuleIndex(self):
            return BKITParser.RULE_index_operators

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operators" ):
                return visitor.visitIndex_operators(self)
            else:
                return visitor.visitChildren(self)




    def index_operators(self):

        localctx = BKITParser.Index_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_index_operators)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 342
                    self.match(BKITParser.LS)
                    self.state = 343
                    self.exp()
                    self.state = 344
                    self.match(BKITParser.RS)

                else:
                    raise NoViableAltException(self)
                self.state = 348 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Exp1Context)
            else:
                return self.getTypedRuleContext(BKITParser.Exp1Context,i)


        def relational(self):
            return self.getTypedRuleContext(BKITParser.RelationalContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = BKITParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_exp)
        try:
            self.state = 355
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 350
                self.exp1(0)
                self.state = 351
                self.relational()
                self.state = 352
                self.exp1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 354
                self.exp1(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self):
            return self.getTypedRuleContext(BKITParser.Exp2Context,0)


        def exp1(self):
            return self.getTypedRuleContext(BKITParser.Exp1Context,0)


        def AND(self):
            return self.getToken(BKITParser.AND, 0)

        def OR(self):
            return self.getToken(BKITParser.OR, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)



    def exp1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_exp1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self.exp2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 365
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                    self.state = 360
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 361
                    _la = self._input.LA(1)
                    if not(_la==BKITParser.AND or _la==BKITParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 362
                    self.exp2(0) 
                self.state = 367
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(BKITParser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(BKITParser.Exp2Context,0)


        def SUB(self):
            return self.getToken(BKITParser.SUB, 0)

        def SUBF(self):
            return self.getToken(BKITParser.SUBF, 0)

        def ADD(self):
            return self.getToken(BKITParser.ADD, 0)

        def ADDF(self):
            return self.getToken(BKITParser.ADDF, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_exp2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 376
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 371
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 372
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ADD) | (1 << BKITParser.ADDF) | (1 << BKITParser.SUB) | (1 << BKITParser.SUBF))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 373
                    self.exp3(0) 
                self.state = 378
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(BKITParser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(BKITParser.Exp3Context,0)


        def MUL(self):
            return self.getToken(BKITParser.MUL, 0)

        def MULF(self):
            return self.getToken(BKITParser.MULF, 0)

        def DIV(self):
            return self.getToken(BKITParser.DIV, 0)

        def DIVF(self):
            return self.getToken(BKITParser.DIVF, 0)

        def MODUL(self):
            return self.getToken(BKITParser.MODUL, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_exp3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380
            self.exp4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 387
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 382
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 383
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.MUL) | (1 << BKITParser.MULF) | (1 << BKITParser.DIV) | (1 << BKITParser.DIVF) | (1 << BKITParser.MODUL))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 384
                    self.exp4() 
                self.state = 389
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(BKITParser.NOT, 0)

        def exp4(self):
            return self.getTypedRuleContext(BKITParser.Exp4Context,0)


        def exp5(self):
            return self.getTypedRuleContext(BKITParser.Exp5Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)




    def exp4(self):

        localctx = BKITParser.Exp4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_exp4)
        try:
            self.state = 393
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 390
                self.match(BKITParser.NOT)
                self.state = 391
                self.exp4()
                pass
            elif token in [BKITParser.ID, BKITParser.DEC, BKITParser.HEXA, BKITParser.OCTAL, BKITParser.FLOAT, BKITParser.STRING, BKITParser.TRUE, BKITParser.FALSE, BKITParser.SUB, BKITParser.SUBF, BKITParser.LP, BKITParser.LB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 392
                self.exp5()
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


    class Exp5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp5(self):
            return self.getTypedRuleContext(BKITParser.Exp5Context,0)


        def SUB(self):
            return self.getToken(BKITParser.SUB, 0)

        def SUBF(self):
            return self.getToken(BKITParser.SUBF, 0)

        def exp6(self):
            return self.getTypedRuleContext(BKITParser.Exp6Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)




    def exp5(self):

        localctx = BKITParser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_exp5)
        self._la = 0 # Token type
        try:
            self.state = 398
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.SUB, BKITParser.SUBF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 395
                _la = self._input.LA(1)
                if not(_la==BKITParser.SUB or _la==BKITParser.SUBF):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 396
                self.exp5()
                pass
            elif token in [BKITParser.ID, BKITParser.DEC, BKITParser.HEXA, BKITParser.OCTAL, BKITParser.FLOAT, BKITParser.STRING, BKITParser.TRUE, BKITParser.FALSE, BKITParser.LP, BKITParser.LB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 397
                self.exp6(0)
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


    class Exp6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp7(self):
            return self.getTypedRuleContext(BKITParser.Exp7Context,0)


        def exp6(self):
            return self.getTypedRuleContext(BKITParser.Exp6Context,0)


        def index_operators(self):
            return self.getTypedRuleContext(BKITParser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)



    def exp6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_exp6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            self.exp7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 407
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp6)
                    self.state = 403
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 404
                    self.index_operators() 
                self.state = 409
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp7Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def call_func(self):
            return self.getTypedRuleContext(BKITParser.Call_funcContext,0)


        def exp8(self):
            return self.getTypedRuleContext(BKITParser.Exp8Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp7" ):
                return visitor.visitExp7(self)
            else:
                return visitor.visitChildren(self)




    def exp7(self):

        localctx = BKITParser.Exp7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_exp7)
        try:
            self.state = 414
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 410
                self.call_func()
                self.state = 411
                self.exp8()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 413
                self.exp8()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp8Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self):
            return self.getTypedRuleContext(BKITParser.OperandContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp8" ):
                return visitor.visitExp8(self)
            else:
                return visitor.visitChildren(self)




    def exp8(self):

        localctx = BKITParser.Exp8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_exp8)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            self.operand()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def literal(self):
            return self.getTypedRuleContext(BKITParser.LiteralContext,0)


        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def call_func(self):
            return self.getTypedRuleContext(BKITParser.Call_funcContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = BKITParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_operand)
        try:
            self.state = 425
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 418
                self.match(BKITParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 419
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 420
                self.match(BKITParser.LP)
                self.state = 421
                self.exp()
                self.state = 422
                self.match(BKITParser.RP)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 424
                self.call_func()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT(self):
            return self.getToken(BKITParser.FLOAT, 0)

        def bool_literal(self):
            return self.getTypedRuleContext(BKITParser.Bool_literalContext,0)


        def DEC(self):
            return self.getToken(BKITParser.DEC, 0)

        def OCTAL(self):
            return self.getToken(BKITParser.OCTAL, 0)

        def HEXA(self):
            return self.getToken(BKITParser.HEXA, 0)

        def STRING(self):
            return self.getToken(BKITParser.STRING, 0)

        def array(self):
            return self.getTypedRuleContext(BKITParser.ArrayContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = BKITParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_literal)
        try:
            self.state = 434
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.FLOAT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 427
                self.match(BKITParser.FLOAT)
                pass
            elif token in [BKITParser.TRUE, BKITParser.FALSE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 428
                self.bool_literal()
                pass
            elif token in [BKITParser.DEC]:
                self.enterOuterAlt(localctx, 3)
                self.state = 429
                self.match(BKITParser.DEC)
                pass
            elif token in [BKITParser.OCTAL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 430
                self.match(BKITParser.OCTAL)
                pass
            elif token in [BKITParser.HEXA]:
                self.enterOuterAlt(localctx, 5)
                self.state = 431
                self.match(BKITParser.HEXA)
                pass
            elif token in [BKITParser.STRING]:
                self.enterOuterAlt(localctx, 6)
                self.state = 432
                self.match(BKITParser.STRING)
                pass
            elif token in [BKITParser.LB]:
                self.enterOuterAlt(localctx, 7)
                self.state = 433
                self.array()
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


    class RelationalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(BKITParser.EQ, 0)

        def NEQ(self):
            return self.getToken(BKITParser.NEQ, 0)

        def LESS(self):
            return self.getToken(BKITParser.LESS, 0)

        def GREATER(self):
            return self.getToken(BKITParser.GREATER, 0)

        def LEQ(self):
            return self.getToken(BKITParser.LEQ, 0)

        def GEQ(self):
            return self.getToken(BKITParser.GEQ, 0)

        def NEQF(self):
            return self.getToken(BKITParser.NEQF, 0)

        def LESSF(self):
            return self.getToken(BKITParser.LESSF, 0)

        def GREATERF(self):
            return self.getToken(BKITParser.GREATERF, 0)

        def LEQF(self):
            return self.getToken(BKITParser.LEQF, 0)

        def GEQF(self):
            return self.getToken(BKITParser.GEQF, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_relational

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational" ):
                return visitor.visitRelational(self)
            else:
                return visitor.visitChildren(self)




    def relational(self):

        localctx = BKITParser.RelationalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_relational)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 436
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.EQ) | (1 << BKITParser.NEQ) | (1 << BKITParser.GREATER) | (1 << BKITParser.LESS) | (1 << BKITParser.GEQ) | (1 << BKITParser.LEQ) | (1 << BKITParser.NEQF) | (1 << BKITParser.LESSF) | (1 << BKITParser.GREATERF) | (1 << BKITParser.GEQF) | (1 << BKITParser.LEQF))) != 0)):
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


    class IntlitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEC(self):
            return self.getToken(BKITParser.DEC, 0)

        def HEXA(self):
            return self.getToken(BKITParser.HEXA, 0)

        def OCTAL(self):
            return self.getToken(BKITParser.OCTAL, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_intlit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntlit" ):
                return visitor.visitIntlit(self)
            else:
                return visitor.visitChildren(self)




    def intlit(self):

        localctx = BKITParser.IntlitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_intlit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 438
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.DEC) | (1 << BKITParser.HEXA) | (1 << BKITParser.OCTAL))) != 0)):
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


    class Bool_literalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(BKITParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(BKITParser.FALSE, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_bool_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool_literal" ):
                return visitor.visitBool_literal(self)
            else:
                return visitor.visitChildren(self)




    def bool_literal(self):

        localctx = BKITParser.Bool_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_bool_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 440
            _la = self._input.LA(1)
            if not(_la==BKITParser.TRUE or _la==BKITParser.FALSE):
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[34] = self.exp1_sempred
        self._predicates[35] = self.exp2_sempred
        self._predicates[36] = self.exp3_sempred
        self._predicates[39] = self.exp6_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp1_sempred(self, localctx:Exp1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def exp6_sempred(self, localctx:Exp6Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




