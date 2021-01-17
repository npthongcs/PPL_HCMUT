# Generated from /Users/macintoshhd/Documents/PPL/assignment1/src/main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2F")
        buf.write("\u0209\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\3\2\3\2\3\2\3\2\7\2\u0092\n\2\f\2")
        buf.write("\16\2\u0095\13\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\7")
        buf.write("\4\u00a0\n\4\f\4\16\4\u00a3\13\4\3\5\3\5\3\5\7\5\u00a8")
        buf.write("\n\5\f\5\16\5\u00ab\13\5\5\5\u00ad\n\5\3\6\3\6\3\6\3\6")
        buf.write("\7\6\u00b3\n\6\f\6\16\6\u00b6\13\6\3\7\3\7\3\7\3\7\7\7")
        buf.write("\u00bc\n\7\f\7\16\7\u00bf\13\7\3\b\6\b\u00c2\n\b\r\b\16")
        buf.write("\b\u00c3\3\b\3\b\7\b\u00c8\n\b\f\b\16\b\u00cb\13\b\3\b")
        buf.write("\3\b\5\b\u00cf\n\b\3\b\6\b\u00d2\n\b\r\b\16\b\u00d3\5")
        buf.write("\b\u00d6\n\b\3\b\6\b\u00d9\n\b\r\b\16\b\u00da\3\b\3\b")
        buf.write("\5\b\u00df\n\b\3\b\6\b\u00e2\n\b\r\b\16\b\u00e3\3\b\6")
        buf.write("\b\u00e7\n\b\r\b\16\b\u00e8\3\b\3\b\5\b\u00ed\n\b\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\7\t\u00f5\n\t\f\t\16\t\u00f8\13\t")
        buf.write("\3\t\3\t\3\t\3\n\3\n\5\n\u00ff\n\n\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"\3#\3#\3#\3$\3$")
        buf.write("\3%\3%\3%\3&\3&\3\'\3\'\3\'\3(\3(\3)\3)\3*\3*\3*\3+\3")
        buf.write("+\3+\3,\3,\3,\3-\3-\3.\3.\3.\3/\3/\3\60\3\60\3\61\3\61")
        buf.write("\3\61\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\64\3\64\3\64")
        buf.write("\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67")
        buf.write("\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3")
        buf.write("@\3A\3A\3B\6B\u01da\nB\rB\16B\u01db\3B\3B\3C\3C\3C\3C")
        buf.write("\3C\3C\7C\u01e6\nC\fC\16C\u01e9\13C\3C\3C\3C\3C\3D\3D")
        buf.write("\3D\3D\3D\3D\7D\u01f5\nD\fD\16D\u01f8\13D\3D\3D\3E\3E")
        buf.write("\3E\3E\7E\u0200\nE\fE\16E\u0203\13E\3E\3E\3F\3F\3F\4\u0093")
        buf.write("\u0201\2G\3\3\5\2\7\4\t\5\13\6\r\7\17\b\21\t\23\n\25\13")
        buf.write("\27\f\31\r\33\16\35\17\37\20!\21#\22%\23\'\24)\25+\26")
        buf.write("-\27/\30\61\31\63\32\65\33\67\349\35;\36=\37? A!C\"E#")
        buf.write("G$I%K&M\'O(Q)S*U+W,Y-[.]/_\60a\61c\62e\63g\64i\65k\66")
        buf.write("m\67o8q9s:u;w<y={>}?\177@\u0081A\u0083B\u0085C\u0087D")
        buf.write("\u0089E\u008bF\3\2\23\3\2\62;\3\2c|\6\2\62;C\\aac|\3\2")
        buf.write("\63;\4\2ZZzz\4\2\63;CH\4\2\62;CH\4\2QQqq\3\2\639\3\2\62")
        buf.write("9\4\2GGgg\4\2--//\3\2$$\t\2))^^ddhhppttvv\6\2\f\f$$))")
        buf.write("^^\5\2\13\f\16\17\"\"\5\2$$))^^\2\u0224\2\3\3\2\2\2\2")
        buf.write("\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3")
        buf.write("\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2")
        buf.write("\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2")
        buf.write("\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2")
        buf.write("\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2")
        buf.write("c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2")
        buf.write("\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2")
        buf.write("\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3")
        buf.write("\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2")
        buf.write("\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\3\u008d")
        buf.write("\3\2\2\2\5\u009b\3\2\2\2\7\u009d\3\2\2\2\t\u00ac\3\2\2")
        buf.write("\2\13\u00ae\3\2\2\2\r\u00b7\3\2\2\2\17\u00ec\3\2\2\2\21")
        buf.write("\u00ee\3\2\2\2\23\u00fe\3\2\2\2\25\u0100\3\2\2\2\27\u0105")
        buf.write("\3\2\2\2\31\u010b\3\2\2\2\33\u0114\3\2\2\2\35\u0117\3")
        buf.write("\2\2\2\37\u011c\3\2\2\2!\u0123\3\2\2\2#\u012b\3\2\2\2")
        buf.write("%\u0131\3\2\2\2\'\u0138\3\2\2\2)\u0141\3\2\2\2+\u0145")
        buf.write("\3\2\2\2-\u014e\3\2\2\2/\u0151\3\2\2\2\61\u015b\3\2\2")
        buf.write("\2\63\u0162\3\2\2\2\65\u0167\3\2\2\2\67\u016b\3\2\2\2")
        buf.write("9\u0171\3\2\2\2;\u0176\3\2\2\2=\u017c\3\2\2\2?\u0182\3")
        buf.write("\2\2\2A\u0184\3\2\2\2C\u0187\3\2\2\2E\u0189\3\2\2\2G\u018c")
        buf.write("\3\2\2\2I\u018e\3\2\2\2K\u0191\3\2\2\2M\u0193\3\2\2\2")
        buf.write("O\u0196\3\2\2\2Q\u0198\3\2\2\2S\u019a\3\2\2\2U\u019d\3")
        buf.write("\2\2\2W\u01a0\3\2\2\2Y\u01a3\3\2\2\2[\u01a5\3\2\2\2]\u01a8")
        buf.write("\3\2\2\2_\u01aa\3\2\2\2a\u01ac\3\2\2\2c\u01af\3\2\2\2")
        buf.write("e\u01b2\3\2\2\2g\u01b6\3\2\2\2i\u01b9\3\2\2\2k\u01bc\3")
        buf.write("\2\2\2m\u01c0\3\2\2\2o\u01c4\3\2\2\2q\u01c6\3\2\2\2s\u01c8")
        buf.write("\3\2\2\2u\u01ca\3\2\2\2w\u01cc\3\2\2\2y\u01ce\3\2\2\2")
        buf.write("{\u01d0\3\2\2\2}\u01d2\3\2\2\2\177\u01d4\3\2\2\2\u0081")
        buf.write("\u01d6\3\2\2\2\u0083\u01d9\3\2\2\2\u0085\u01df\3\2\2\2")
        buf.write("\u0087\u01ee\3\2\2\2\u0089\u01fb\3\2\2\2\u008b\u0206\3")
        buf.write("\2\2\2\u008d\u008e\7,\2\2\u008e\u008f\7,\2\2\u008f\u0093")
        buf.write("\3\2\2\2\u0090\u0092\13\2\2\2\u0091\u0090\3\2\2\2\u0092")
        buf.write("\u0095\3\2\2\2\u0093\u0094\3\2\2\2\u0093\u0091\3\2\2\2")
        buf.write("\u0094\u0096\3\2\2\2\u0095\u0093\3\2\2\2\u0096\u0097\7")
        buf.write(",\2\2\u0097\u0098\7,\2\2\u0098\u0099\3\2\2\2\u0099\u009a")
        buf.write("\b\2\2\2\u009a\4\3\2\2\2\u009b\u009c\t\2\2\2\u009c\6\3")
        buf.write("\2\2\2\u009d\u00a1\t\3\2\2\u009e\u00a0\t\4\2\2\u009f\u009e")
        buf.write("\3\2\2\2\u00a0\u00a3\3\2\2\2\u00a1\u009f\3\2\2\2\u00a1")
        buf.write("\u00a2\3\2\2\2\u00a2\b\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a4")
        buf.write("\u00ad\7\62\2\2\u00a5\u00a9\t\5\2\2\u00a6\u00a8\t\2\2")
        buf.write("\2\u00a7\u00a6\3\2\2\2\u00a8\u00ab\3\2\2\2\u00a9\u00a7")
        buf.write("\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00ad\3\2\2\2\u00ab")
        buf.write("\u00a9\3\2\2\2\u00ac\u00a4\3\2\2\2\u00ac\u00a5\3\2\2\2")
        buf.write("\u00ad\n\3\2\2\2\u00ae\u00af\7\62\2\2\u00af\u00b0\t\6")
        buf.write("\2\2\u00b0\u00b4\t\7\2\2\u00b1\u00b3\t\b\2\2\u00b2\u00b1")
        buf.write("\3\2\2\2\u00b3\u00b6\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b4")
        buf.write("\u00b5\3\2\2\2\u00b5\f\3\2\2\2\u00b6\u00b4\3\2\2\2\u00b7")
        buf.write("\u00b8\7\62\2\2\u00b8\u00b9\t\t\2\2\u00b9\u00bd\t\n\2")
        buf.write("\2\u00ba\u00bc\t\13\2\2\u00bb\u00ba\3\2\2\2\u00bc\u00bf")
        buf.write("\3\2\2\2\u00bd\u00bb\3\2\2\2\u00bd\u00be\3\2\2\2\u00be")
        buf.write("\16\3\2\2\2\u00bf\u00bd\3\2\2\2\u00c0\u00c2\5\5\3\2\u00c1")
        buf.write("\u00c0\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\u00c1\3\2\2\2")
        buf.write("\u00c3\u00c4\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\u00c9\5")
        buf.write("\u0081A\2\u00c6\u00c8\5\5\3\2\u00c7\u00c6\3\2\2\2\u00c8")
        buf.write("\u00cb\3\2\2\2\u00c9\u00c7\3\2\2\2\u00c9\u00ca\3\2\2\2")
        buf.write("\u00ca\u00d5\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cc\u00ce\t")
        buf.write("\f\2\2\u00cd\u00cf\t\r\2\2\u00ce\u00cd\3\2\2\2\u00ce\u00cf")
        buf.write("\3\2\2\2\u00cf\u00d1\3\2\2\2\u00d0\u00d2\5\5\3\2\u00d1")
        buf.write("\u00d0\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00d1\3\2\2\2")
        buf.write("\u00d3\u00d4\3\2\2\2\u00d4\u00d6\3\2\2\2\u00d5\u00cc\3")
        buf.write("\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\u00ed\3\2\2\2\u00d7\u00d9")
        buf.write("\5\5\3\2\u00d8\u00d7\3\2\2\2\u00d9\u00da\3\2\2\2\u00da")
        buf.write("\u00d8\3\2\2\2\u00da\u00db\3\2\2\2\u00db\u00dc\3\2\2\2")
        buf.write("\u00dc\u00de\t\f\2\2\u00dd\u00df\t\r\2\2\u00de\u00dd\3")
        buf.write("\2\2\2\u00de\u00df\3\2\2\2\u00df\u00e1\3\2\2\2\u00e0\u00e2")
        buf.write("\5\5\3\2\u00e1\u00e0\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3")
        buf.write("\u00e1\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4\u00ed\3\2\2\2")
        buf.write("\u00e5\u00e7\5\5\3\2\u00e6\u00e5\3\2\2\2\u00e7\u00e8\3")
        buf.write("\2\2\2\u00e8\u00e6\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9\u00ea")
        buf.write("\3\2\2\2\u00ea\u00eb\5\u0081A\2\u00eb\u00ed\3\2\2\2\u00ec")
        buf.write("\u00c1\3\2\2\2\u00ec\u00d8\3\2\2\2\u00ec\u00e6\3\2\2\2")
        buf.write("\u00ed\20\3\2\2\2\u00ee\u00f6\t\16\2\2\u00ef\u00f0\7^")
        buf.write("\2\2\u00f0\u00f5\t\17\2\2\u00f1\u00f2\7)\2\2\u00f2\u00f5")
        buf.write("\7$\2\2\u00f3\u00f5\n\20\2\2\u00f4\u00ef\3\2\2\2\u00f4")
        buf.write("\u00f1\3\2\2\2\u00f4\u00f3\3\2\2\2\u00f5\u00f8\3\2\2\2")
        buf.write("\u00f6\u00f4\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7\u00f9\3")
        buf.write("\2\2\2\u00f8\u00f6\3\2\2\2\u00f9\u00fa\t\16\2\2\u00fa")
        buf.write("\u00fb\b\t\3\2\u00fb\22\3\2\2\2\u00fc\u00ff\59\35\2\u00fd")
        buf.write("\u00ff\5;\36\2\u00fe\u00fc\3\2\2\2\u00fe\u00fd\3\2\2\2")
        buf.write("\u00ff\24\3\2\2\2\u0100\u0101\7D\2\2\u0101\u0102\7q\2")
        buf.write("\2\u0102\u0103\7f\2\2\u0103\u0104\7{\2\2\u0104\26\3\2")
        buf.write("\2\2\u0105\u0106\7D\2\2\u0106\u0107\7t\2\2\u0107\u0108")
        buf.write("\7g\2\2\u0108\u0109\7c\2\2\u0109\u010a\7m\2\2\u010a\30")
        buf.write("\3\2\2\2\u010b\u010c\7E\2\2\u010c\u010d\7q\2\2\u010d\u010e")
        buf.write("\7p\2\2\u010e\u010f\7v\2\2\u010f\u0110\7k\2\2\u0110\u0111")
        buf.write("\7p\2\2\u0111\u0112\7w\2\2\u0112\u0113\7g\2\2\u0113\32")
        buf.write("\3\2\2\2\u0114\u0115\7F\2\2\u0115\u0116\7q\2\2\u0116\34")
        buf.write("\3\2\2\2\u0117\u0118\7G\2\2\u0118\u0119\7n\2\2\u0119\u011a")
        buf.write("\7u\2\2\u011a\u011b\7g\2\2\u011b\36\3\2\2\2\u011c\u011d")
        buf.write("\7G\2\2\u011d\u011e\7n\2\2\u011e\u011f\7u\2\2\u011f\u0120")
        buf.write("\7g\2\2\u0120\u0121\7K\2\2\u0121\u0122\7h\2\2\u0122 \3")
        buf.write("\2\2\2\u0123\u0124\7G\2\2\u0124\u0125\7p\2\2\u0125\u0126")
        buf.write("\7f\2\2\u0126\u0127\7D\2\2\u0127\u0128\7q\2\2\u0128\u0129")
        buf.write("\7f\2\2\u0129\u012a\7{\2\2\u012a\"\3\2\2\2\u012b\u012c")
        buf.write("\7G\2\2\u012c\u012d\7p\2\2\u012d\u012e\7f\2\2\u012e\u012f")
        buf.write("\7K\2\2\u012f\u0130\7h\2\2\u0130$\3\2\2\2\u0131\u0132")
        buf.write("\7G\2\2\u0132\u0133\7p\2\2\u0133\u0134\7f\2\2\u0134\u0135")
        buf.write("\7H\2\2\u0135\u0136\7q\2\2\u0136\u0137\7t\2\2\u0137&\3")
        buf.write("\2\2\2\u0138\u0139\7G\2\2\u0139\u013a\7p\2\2\u013a\u013b")
        buf.write("\7f\2\2\u013b\u013c\7Y\2\2\u013c\u013d\7j\2\2\u013d\u013e")
        buf.write("\7k\2\2\u013e\u013f\7n\2\2\u013f\u0140\7g\2\2\u0140(\3")
        buf.write("\2\2\2\u0141\u0142\7H\2\2\u0142\u0143\7q\2\2\u0143\u0144")
        buf.write("\7t\2\2\u0144*\3\2\2\2\u0145\u0146\7H\2\2\u0146\u0147")
        buf.write("\7w\2\2\u0147\u0148\7p\2\2\u0148\u0149\7e\2\2\u0149\u014a")
        buf.write("\7v\2\2\u014a\u014b\7k\2\2\u014b\u014c\7q\2\2\u014c\u014d")
        buf.write("\7p\2\2\u014d,\3\2\2\2\u014e\u014f\7K\2\2\u014f\u0150")
        buf.write("\7h\2\2\u0150.\3\2\2\2\u0151\u0152\7R\2\2\u0152\u0153")
        buf.write("\7c\2\2\u0153\u0154\7t\2\2\u0154\u0155\7c\2\2\u0155\u0156")
        buf.write("\7o\2\2\u0156\u0157\7g\2\2\u0157\u0158\7v\2\2\u0158\u0159")
        buf.write("\7g\2\2\u0159\u015a\7t\2\2\u015a\60\3\2\2\2\u015b\u015c")
        buf.write("\7T\2\2\u015c\u015d\7g\2\2\u015d\u015e\7v\2\2\u015e\u015f")
        buf.write("\7w\2\2\u015f\u0160\7t\2\2\u0160\u0161\7p\2\2\u0161\62")
        buf.write("\3\2\2\2\u0162\u0163\7V\2\2\u0163\u0164\7j\2\2\u0164\u0165")
        buf.write("\7g\2\2\u0165\u0166\7p\2\2\u0166\64\3\2\2\2\u0167\u0168")
        buf.write("\7X\2\2\u0168\u0169\7c\2\2\u0169\u016a\7t\2\2\u016a\66")
        buf.write("\3\2\2\2\u016b\u016c\7Y\2\2\u016c\u016d\7j\2\2\u016d\u016e")
        buf.write("\7k\2\2\u016e\u016f\7n\2\2\u016f\u0170\7g\2\2\u01708\3")
        buf.write("\2\2\2\u0171\u0172\7V\2\2\u0172\u0173\7t\2\2\u0173\u0174")
        buf.write("\7w\2\2\u0174\u0175\7g\2\2\u0175:\3\2\2\2\u0176\u0177")
        buf.write("\7H\2\2\u0177\u0178\7c\2\2\u0178\u0179\7n\2\2\u0179\u017a")
        buf.write("\7u\2\2\u017a\u017b\7g\2\2\u017b<\3\2\2\2\u017c\u017d")
        buf.write("\7G\2\2\u017d\u017e\7p\2\2\u017e\u017f\7f\2\2\u017f\u0180")
        buf.write("\7F\2\2\u0180\u0181\7q\2\2\u0181>\3\2\2\2\u0182\u0183")
        buf.write("\7-\2\2\u0183@\3\2\2\2\u0184\u0185\7-\2\2\u0185\u0186")
        buf.write("\7\60\2\2\u0186B\3\2\2\2\u0187\u0188\7/\2\2\u0188D\3\2")
        buf.write("\2\2\u0189\u018a\7/\2\2\u018a\u018b\7\60\2\2\u018bF\3")
        buf.write("\2\2\2\u018c\u018d\7,\2\2\u018dH\3\2\2\2\u018e\u018f\7")
        buf.write(",\2\2\u018f\u0190\7\60\2\2\u0190J\3\2\2\2\u0191\u0192")
        buf.write("\7^\2\2\u0192L\3\2\2\2\u0193\u0194\7^\2\2\u0194\u0195")
        buf.write("\7\60\2\2\u0195N\3\2\2\2\u0196\u0197\7\'\2\2\u0197P\3")
        buf.write("\2\2\2\u0198\u0199\7#\2\2\u0199R\3\2\2\2\u019a\u019b\7")
        buf.write("(\2\2\u019b\u019c\7(\2\2\u019cT\3\2\2\2\u019d\u019e\7")
        buf.write("~\2\2\u019e\u019f\7~\2\2\u019fV\3\2\2\2\u01a0\u01a1\7")
        buf.write("?\2\2\u01a1\u01a2\7?\2\2\u01a2X\3\2\2\2\u01a3\u01a4\7")
        buf.write("?\2\2\u01a4Z\3\2\2\2\u01a5\u01a6\7#\2\2\u01a6\u01a7\7")
        buf.write("?\2\2\u01a7\\\3\2\2\2\u01a8\u01a9\7@\2\2\u01a9^\3\2\2")
        buf.write("\2\u01aa\u01ab\7>\2\2\u01ab`\3\2\2\2\u01ac\u01ad\7@\2")
        buf.write("\2\u01ad\u01ae\7?\2\2\u01aeb\3\2\2\2\u01af\u01b0\7>\2")
        buf.write("\2\u01b0\u01b1\7?\2\2\u01b1d\3\2\2\2\u01b2\u01b3\7?\2")
        buf.write("\2\u01b3\u01b4\7\61\2\2\u01b4\u01b5\7?\2\2\u01b5f\3\2")
        buf.write("\2\2\u01b6\u01b7\7>\2\2\u01b7\u01b8\7\60\2\2\u01b8h\3")
        buf.write("\2\2\2\u01b9\u01ba\7@\2\2\u01ba\u01bb\7\60\2\2\u01bbj")
        buf.write("\3\2\2\2\u01bc\u01bd\7@\2\2\u01bd\u01be\7?\2\2\u01be\u01bf")
        buf.write("\7\60\2\2\u01bfl\3\2\2\2\u01c0\u01c1\7>\2\2\u01c1\u01c2")
        buf.write("\7?\2\2\u01c2\u01c3\7\60\2\2\u01c3n\3\2\2\2\u01c4\u01c5")
        buf.write("\7*\2\2\u01c5p\3\2\2\2\u01c6\u01c7\7+\2\2\u01c7r\3\2\2")
        buf.write("\2\u01c8\u01c9\7]\2\2\u01c9t\3\2\2\2\u01ca\u01cb\7_\2")
        buf.write("\2\u01cbv\3\2\2\2\u01cc\u01cd\7}\2\2\u01cdx\3\2\2\2\u01ce")
        buf.write("\u01cf\7\177\2\2\u01cfz\3\2\2\2\u01d0\u01d1\7<\2\2\u01d1")
        buf.write("|\3\2\2\2\u01d2\u01d3\7=\2\2\u01d3~\3\2\2\2\u01d4\u01d5")
        buf.write("\7.\2\2\u01d5\u0080\3\2\2\2\u01d6\u01d7\7\60\2\2\u01d7")
        buf.write("\u0082\3\2\2\2\u01d8\u01da\t\21\2\2\u01d9\u01d8\3\2\2")
        buf.write("\2\u01da\u01db\3\2\2\2\u01db\u01d9\3\2\2\2\u01db\u01dc")
        buf.write("\3\2\2\2\u01dc\u01dd\3\2\2\2\u01dd\u01de\bB\2\2\u01de")
        buf.write("\u0084\3\2\2\2\u01df\u01e7\7$\2\2\u01e0\u01e1\7^\2\2\u01e1")
        buf.write("\u01e6\t\17\2\2\u01e2\u01e3\7)\2\2\u01e3\u01e6\7$\2\2")
        buf.write("\u01e4\u01e6\n\22\2\2\u01e5\u01e0\3\2\2\2\u01e5\u01e2")
        buf.write("\3\2\2\2\u01e5\u01e4\3\2\2\2\u01e6\u01e9\3\2\2\2\u01e7")
        buf.write("\u01e5\3\2\2\2\u01e7\u01e8\3\2\2\2\u01e8\u01ea\3\2\2\2")
        buf.write("\u01e9\u01e7\3\2\2\2\u01ea\u01eb\7^\2\2\u01eb\u01ec\n")
        buf.write("\17\2\2\u01ec\u01ed\bC\4\2\u01ed\u0086\3\2\2\2\u01ee\u01f6")
        buf.write("\7$\2\2\u01ef\u01f0\7^\2\2\u01f0\u01f5\t\17\2\2\u01f1")
        buf.write("\u01f2\7)\2\2\u01f2\u01f5\7$\2\2\u01f3\u01f5\n\22\2\2")
        buf.write("\u01f4\u01ef\3\2\2\2\u01f4\u01f1\3\2\2\2\u01f4\u01f3\3")
        buf.write("\2\2\2\u01f5\u01f8\3\2\2\2\u01f6\u01f4\3\2\2\2\u01f6\u01f7")
        buf.write("\3\2\2\2\u01f7\u01f9\3\2\2\2\u01f8\u01f6\3\2\2\2\u01f9")
        buf.write("\u01fa\bD\5\2\u01fa\u0088\3\2\2\2\u01fb\u01fc\7,\2\2\u01fc")
        buf.write("\u01fd\7,\2\2\u01fd\u0201\3\2\2\2\u01fe\u0200\13\2\2\2")
        buf.write("\u01ff\u01fe\3\2\2\2\u0200\u0203\3\2\2\2\u0201\u0202\3")
        buf.write("\2\2\2\u0201\u01ff\3\2\2\2\u0202\u0204\3\2\2\2\u0203\u0201")
        buf.write("\3\2\2\2\u0204\u0205\bE\6\2\u0205\u008a\3\2\2\2\u0206")
        buf.write("\u0207\13\2\2\2\u0207\u0208\bF\7\2\u0208\u008c\3\2\2\2")
        buf.write("\34\2\u0093\u00a1\u00a9\u00ac\u00b4\u00bd\u00c3\u00c9")
        buf.write("\u00ce\u00d3\u00d5\u00da\u00de\u00e3\u00e8\u00ec\u00f4")
        buf.write("\u00f6\u00fe\u01db\u01e5\u01e7\u01f4\u01f6\u0201\b\b\2")
        buf.write("\2\3\t\2\3C\3\3D\4\3E\5\3F\6")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMENT = 1
    ID = 2
    INT = 3
    HEXA = 4
    OCTAL = 5
    FLOAT = 6
    STRING = 7
    BOOL = 8
    BODY = 9
    BREAK = 10
    CONTINUE = 11
    DO = 12
    ELSE = 13
    ELSEIF = 14
    ENDBODY = 15
    ENDIF = 16
    ENDFOR = 17
    ENDWHILE = 18
    FOR = 19
    FUNCTION = 20
    IF = 21
    PARAMETER = 22
    RETURN = 23
    THEN = 24
    VAR = 25
    WHILE = 26
    TRUE = 27
    FALSE = 28
    ENDDO = 29
    ADD = 30
    ADDF = 31
    SUB = 32
    SUBF = 33
    MUL = 34
    MULF = 35
    DIV = 36
    DIVF = 37
    MODUL = 38
    NOT = 39
    AND = 40
    OR = 41
    EQ = 42
    ASS = 43
    NEQ = 44
    GREATER = 45
    LESS = 46
    GEQ = 47
    LEQ = 48
    NEQF = 49
    LESSF = 50
    GREATERF = 51
    GEQF = 52
    LEQF = 53
    LP = 54
    RP = 55
    LS = 56
    RS = 57
    LB = 58
    RB = 59
    COLON = 60
    SM = 61
    CM = 62
    DOT = 63
    WS = 64
    ILLEGAL_ESCAPE = 65
    UNCLOSE_STRING = 66
    UNTERMINATED_COMMENT = 67
    ERROR_CHAR = 68

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Body'", "'Break'", "'Continue'", "'Do'", "'Else'", "'ElseIf'", 
            "'EndBody'", "'EndIf'", "'EndFor'", "'EndWhile'", "'For'", "'Function'", 
            "'If'", "'Parameter'", "'Return'", "'Then'", "'Var'", "'While'", 
            "'True'", "'False'", "'EndDo'", "'+'", "'+.'", "'-'", "'-.'", 
            "'*'", "'*.'", "'\\'", "'\\.'", "'%'", "'!'", "'&&'", "'||'", 
            "'=='", "'='", "'!='", "'>'", "'<'", "'>='", "'<='", "'=/='", 
            "'<.'", "'>.'", "'>=.'", "'<=.'", "'('", "')'", "'['", "']'", 
            "'{'", "'}'", "':'", "';'", "','", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "ID", "INT", "HEXA", "OCTAL", "FLOAT", "STRING", 
            "BOOL", "BODY", "BREAK", "CONTINUE", "DO", "ELSE", "ELSEIF", 
            "ENDBODY", "ENDIF", "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", 
            "IF", "PARAMETER", "RETURN", "THEN", "VAR", "WHILE", "TRUE", 
            "FALSE", "ENDDO", "ADD", "ADDF", "SUB", "SUBF", "MUL", "MULF", 
            "DIV", "DIVF", "MODUL", "NOT", "AND", "OR", "EQ", "ASS", "NEQ", 
            "GREATER", "LESS", "GEQ", "LEQ", "NEQF", "LESSF", "GREATERF", 
            "GEQF", "LEQF", "LP", "RP", "LS", "RS", "LB", "RB", "COLON", 
            "SM", "CM", "DOT", "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
            "UNTERMINATED_COMMENT", "ERROR_CHAR" ]

    ruleNames = [ "COMMENT", "DIGIT", "ID", "INT", "HEXA", "OCTAL", "FLOAT", 
                  "STRING", "BOOL", "BODY", "BREAK", "CONTINUE", "DO", "ELSE", 
                  "ELSEIF", "ENDBODY", "ENDIF", "ENDFOR", "ENDWHILE", "FOR", 
                  "FUNCTION", "IF", "PARAMETER", "RETURN", "THEN", "VAR", 
                  "WHILE", "TRUE", "FALSE", "ENDDO", "ADD", "ADDF", "SUB", 
                  "SUBF", "MUL", "MULF", "DIV", "DIVF", "MODUL", "NOT", 
                  "AND", "OR", "EQ", "ASS", "NEQ", "GREATER", "LESS", "GEQ", 
                  "LEQ", "NEQF", "LESSF", "GREATERF", "GEQF", "LEQF", "LP", 
                  "RP", "LS", "RS", "LB", "RB", "COLON", "SM", "CM", "DOT", 
                  "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "UNTERMINATED_COMMENT", 
                  "ERROR_CHAR" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[7] = self.STRING_action 
            actions[65] = self.ILLEGAL_ESCAPE_action 
            actions[66] = self.UNCLOSE_STRING_action 
            actions[67] = self.UNTERMINATED_COMMENT_action 
            actions[68] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                 self.text = self.text[1:-1]

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                self.text = self.text[1:]

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                self.text = self.text[1:]

     

    def UNTERMINATED_COMMENT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                self.text = self.text[1:0]

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                self.text=self.text;

     


