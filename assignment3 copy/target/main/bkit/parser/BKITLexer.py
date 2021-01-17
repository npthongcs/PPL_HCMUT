# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2E")
        buf.write("\u0203\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\3\2\3\2\3\2\3\2\7\2\u0090\n\2\f\2\16\2\u0093")
        buf.write("\13\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\7\4\u009e\n")
        buf.write("\4\f\4\16\4\u00a1\13\4\3\5\3\5\3\5\7\5\u00a6\n\5\f\5\16")
        buf.write("\5\u00a9\13\5\5\5\u00ab\n\5\3\6\3\6\3\6\3\6\7\6\u00b1")
        buf.write("\n\6\f\6\16\6\u00b4\13\6\3\7\3\7\3\7\3\7\7\7\u00ba\n\7")
        buf.write("\f\7\16\7\u00bd\13\7\3\b\6\b\u00c0\n\b\r\b\16\b\u00c1")
        buf.write("\3\b\3\b\7\b\u00c6\n\b\f\b\16\b\u00c9\13\b\3\b\3\b\5\b")
        buf.write("\u00cd\n\b\3\b\6\b\u00d0\n\b\r\b\16\b\u00d1\5\b\u00d4")
        buf.write("\n\b\3\b\6\b\u00d7\n\b\r\b\16\b\u00d8\3\b\3\b\5\b\u00dd")
        buf.write("\n\b\3\b\6\b\u00e0\n\b\r\b\16\b\u00e1\3\b\6\b\u00e5\n")
        buf.write("\b\r\b\16\b\u00e6\3\b\3\b\5\b\u00eb\n\b\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\7\t\u00f3\n\t\f\t\16\t\u00f6\13\t\3\t\3\t\3")
        buf.write("\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3 \3 \3")
        buf.write(" \3!\3!\3\"\3\"\3\"\3#\3#\3$\3$\3$\3%\3%\3&\3&\3&\3\'")
        buf.write("\3\'\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3-\3-\3-\3")
        buf.write(".\3.\3/\3/\3\60\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3\62")
        buf.write("\3\62\3\63\3\63\3\63\3\64\3\64\3\64\3\65\3\65\3\65\3\65")
        buf.write("\3\66\3\66\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3")
        buf.write(";\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3A\6A\u01d4\nA\rA\16A")
        buf.write("\u01d5\3A\3A\3B\3B\3B\3B\3B\3B\7B\u01e0\nB\fB\16B\u01e3")
        buf.write("\13B\3B\3B\3B\3B\3C\3C\3C\3C\3C\3C\7C\u01ef\nC\fC\16C")
        buf.write("\u01f2\13C\3C\3C\3D\3D\3D\3D\7D\u01fa\nD\fD\16D\u01fd")
        buf.write("\13D\3D\3D\3E\3E\3E\4\u0091\u01fb\2F\3\3\5\2\7\4\t\5\13")
        buf.write("\6\r\7\17\b\21\t\23\n\25\13\27\f\31\r\33\16\35\17\37\20")
        buf.write("!\21#\22%\23\'\24)\25+\26-\27/\30\61\31\63\32\65\33\67")
        buf.write("\349\35;\36=\37? A!C\"E#G$I%K&M\'O(Q)S*U+W,Y-[.]/_\60")
        buf.write("a\61c\62e\63g\64i\65k\66m\67o8q9s:u;w<y={>}?\177@\u0081")
        buf.write("A\u0083B\u0085C\u0087D\u0089E\3\2\23\3\2\62;\3\2c|\6\2")
        buf.write("\62;C\\aac|\3\2\63;\4\2ZZzz\4\2\63;CH\4\2\62;CH\4\2QQ")
        buf.write("qq\3\2\639\3\2\629\4\2GGgg\4\2--//\3\2$$\t\2))^^ddhhp")
        buf.write("pttvv\6\2\f\f$$))^^\5\2\13\f\16\17\"\"\5\2$$))^^\2\u021d")
        buf.write("\2\3\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3")
        buf.write("\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2")
        buf.write("\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'")
        buf.write("\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2")
        buf.write("\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29")
        buf.write("\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2")
        buf.write("C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2")
        buf.write("\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2")
        buf.write("\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2")
        buf.write("\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3")
        buf.write("\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s")
        buf.write("\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2")
        buf.write("}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2")
        buf.write("\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\3\u008b")
        buf.write("\3\2\2\2\5\u0099\3\2\2\2\7\u009b\3\2\2\2\t\u00aa\3\2\2")
        buf.write("\2\13\u00ac\3\2\2\2\r\u00b5\3\2\2\2\17\u00ea\3\2\2\2\21")
        buf.write("\u00ec\3\2\2\2\23\u00fa\3\2\2\2\25\u00ff\3\2\2\2\27\u0105")
        buf.write("\3\2\2\2\31\u010e\3\2\2\2\33\u0111\3\2\2\2\35\u0116\3")
        buf.write("\2\2\2\37\u011d\3\2\2\2!\u0125\3\2\2\2#\u012b\3\2\2\2")
        buf.write("%\u0132\3\2\2\2\'\u013b\3\2\2\2)\u013f\3\2\2\2+\u0148")
        buf.write("\3\2\2\2-\u014b\3\2\2\2/\u0155\3\2\2\2\61\u015c\3\2\2")
        buf.write("\2\63\u0161\3\2\2\2\65\u0165\3\2\2\2\67\u016b\3\2\2\2")
        buf.write("9\u0170\3\2\2\2;\u0176\3\2\2\2=\u017c\3\2\2\2?\u017e\3")
        buf.write("\2\2\2A\u0181\3\2\2\2C\u0183\3\2\2\2E\u0186\3\2\2\2G\u0188")
        buf.write("\3\2\2\2I\u018b\3\2\2\2K\u018d\3\2\2\2M\u0190\3\2\2\2")
        buf.write("O\u0192\3\2\2\2Q\u0194\3\2\2\2S\u0197\3\2\2\2U\u019a\3")
        buf.write("\2\2\2W\u019d\3\2\2\2Y\u019f\3\2\2\2[\u01a2\3\2\2\2]\u01a4")
        buf.write("\3\2\2\2_\u01a6\3\2\2\2a\u01a9\3\2\2\2c\u01ac\3\2\2\2")
        buf.write("e\u01b0\3\2\2\2g\u01b3\3\2\2\2i\u01b6\3\2\2\2k\u01ba\3")
        buf.write("\2\2\2m\u01be\3\2\2\2o\u01c0\3\2\2\2q\u01c2\3\2\2\2s\u01c4")
        buf.write("\3\2\2\2u\u01c6\3\2\2\2w\u01c8\3\2\2\2y\u01ca\3\2\2\2")
        buf.write("{\u01cc\3\2\2\2}\u01ce\3\2\2\2\177\u01d0\3\2\2\2\u0081")
        buf.write("\u01d3\3\2\2\2\u0083\u01d9\3\2\2\2\u0085\u01e8\3\2\2\2")
        buf.write("\u0087\u01f5\3\2\2\2\u0089\u0200\3\2\2\2\u008b\u008c\7")
        buf.write(",\2\2\u008c\u008d\7,\2\2\u008d\u0091\3\2\2\2\u008e\u0090")
        buf.write("\13\2\2\2\u008f\u008e\3\2\2\2\u0090\u0093\3\2\2\2\u0091")
        buf.write("\u0092\3\2\2\2\u0091\u008f\3\2\2\2\u0092\u0094\3\2\2\2")
        buf.write("\u0093\u0091\3\2\2\2\u0094\u0095\7,\2\2\u0095\u0096\7")
        buf.write(",\2\2\u0096\u0097\3\2\2\2\u0097\u0098\b\2\2\2\u0098\4")
        buf.write("\3\2\2\2\u0099\u009a\t\2\2\2\u009a\6\3\2\2\2\u009b\u009f")
        buf.write("\t\3\2\2\u009c\u009e\t\4\2\2\u009d\u009c\3\2\2\2\u009e")
        buf.write("\u00a1\3\2\2\2\u009f\u009d\3\2\2\2\u009f\u00a0\3\2\2\2")
        buf.write("\u00a0\b\3\2\2\2\u00a1\u009f\3\2\2\2\u00a2\u00ab\7\62")
        buf.write("\2\2\u00a3\u00a7\t\5\2\2\u00a4\u00a6\t\2\2\2\u00a5\u00a4")
        buf.write("\3\2\2\2\u00a6\u00a9\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a7")
        buf.write("\u00a8\3\2\2\2\u00a8\u00ab\3\2\2\2\u00a9\u00a7\3\2\2\2")
        buf.write("\u00aa\u00a2\3\2\2\2\u00aa\u00a3\3\2\2\2\u00ab\n\3\2\2")
        buf.write("\2\u00ac\u00ad\7\62\2\2\u00ad\u00ae\t\6\2\2\u00ae\u00b2")
        buf.write("\t\7\2\2\u00af\u00b1\t\b\2\2\u00b0\u00af\3\2\2\2\u00b1")
        buf.write("\u00b4\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b2\u00b3\3\2\2\2")
        buf.write("\u00b3\f\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b5\u00b6\7\62")
        buf.write("\2\2\u00b6\u00b7\t\t\2\2\u00b7\u00bb\t\n\2\2\u00b8\u00ba")
        buf.write("\t\13\2\2\u00b9\u00b8\3\2\2\2\u00ba\u00bd\3\2\2\2\u00bb")
        buf.write("\u00b9\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\16\3\2\2\2\u00bd")
        buf.write("\u00bb\3\2\2\2\u00be\u00c0\5\5\3\2\u00bf\u00be\3\2\2\2")
        buf.write("\u00c0\u00c1\3\2\2\2\u00c1\u00bf\3\2\2\2\u00c1\u00c2\3")
        buf.write("\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\u00c7\7\60\2\2\u00c4")
        buf.write("\u00c6\5\5\3\2\u00c5\u00c4\3\2\2\2\u00c6\u00c9\3\2\2\2")
        buf.write("\u00c7\u00c5\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\u00d3\3")
        buf.write("\2\2\2\u00c9\u00c7\3\2\2\2\u00ca\u00cc\t\f\2\2\u00cb\u00cd")
        buf.write("\t\r\2\2\u00cc\u00cb\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd")
        buf.write("\u00cf\3\2\2\2\u00ce\u00d0\5\5\3\2\u00cf\u00ce\3\2\2\2")
        buf.write("\u00d0\u00d1\3\2\2\2\u00d1\u00cf\3\2\2\2\u00d1\u00d2\3")
        buf.write("\2\2\2\u00d2\u00d4\3\2\2\2\u00d3\u00ca\3\2\2\2\u00d3\u00d4")
        buf.write("\3\2\2\2\u00d4\u00eb\3\2\2\2\u00d5\u00d7\5\5\3\2\u00d6")
        buf.write("\u00d5\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8\u00d6\3\2\2\2")
        buf.write("\u00d8\u00d9\3\2\2\2\u00d9\u00da\3\2\2\2\u00da\u00dc\t")
        buf.write("\f\2\2\u00db\u00dd\t\r\2\2\u00dc\u00db\3\2\2\2\u00dc\u00dd")
        buf.write("\3\2\2\2\u00dd\u00df\3\2\2\2\u00de\u00e0\5\5\3\2\u00df")
        buf.write("\u00de\3\2\2\2\u00e0\u00e1\3\2\2\2\u00e1\u00df\3\2\2\2")
        buf.write("\u00e1\u00e2\3\2\2\2\u00e2\u00eb\3\2\2\2\u00e3\u00e5\5")
        buf.write("\5\3\2\u00e4\u00e3\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6\u00e4")
        buf.write("\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8")
        buf.write("\u00e9\7\60\2\2\u00e9\u00eb\3\2\2\2\u00ea\u00bf\3\2\2")
        buf.write("\2\u00ea\u00d6\3\2\2\2\u00ea\u00e4\3\2\2\2\u00eb\20\3")
        buf.write("\2\2\2\u00ec\u00f4\t\16\2\2\u00ed\u00ee\7^\2\2\u00ee\u00f3")
        buf.write("\t\17\2\2\u00ef\u00f0\7)\2\2\u00f0\u00f3\7$\2\2\u00f1")
        buf.write("\u00f3\n\20\2\2\u00f2\u00ed\3\2\2\2\u00f2\u00ef\3\2\2")
        buf.write("\2\u00f2\u00f1\3\2\2\2\u00f3\u00f6\3\2\2\2\u00f4\u00f2")
        buf.write("\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5\u00f7\3\2\2\2\u00f6")
        buf.write("\u00f4\3\2\2\2\u00f7\u00f8\t\16\2\2\u00f8\u00f9\b\t\3")
        buf.write("\2\u00f9\22\3\2\2\2\u00fa\u00fb\7D\2\2\u00fb\u00fc\7q")
        buf.write("\2\2\u00fc\u00fd\7f\2\2\u00fd\u00fe\7{\2\2\u00fe\24\3")
        buf.write("\2\2\2\u00ff\u0100\7D\2\2\u0100\u0101\7t\2\2\u0101\u0102")
        buf.write("\7g\2\2\u0102\u0103\7c\2\2\u0103\u0104\7m\2\2\u0104\26")
        buf.write("\3\2\2\2\u0105\u0106\7E\2\2\u0106\u0107\7q\2\2\u0107\u0108")
        buf.write("\7p\2\2\u0108\u0109\7v\2\2\u0109\u010a\7k\2\2\u010a\u010b")
        buf.write("\7p\2\2\u010b\u010c\7w\2\2\u010c\u010d\7g\2\2\u010d\30")
        buf.write("\3\2\2\2\u010e\u010f\7F\2\2\u010f\u0110\7q\2\2\u0110\32")
        buf.write("\3\2\2\2\u0111\u0112\7G\2\2\u0112\u0113\7n\2\2\u0113\u0114")
        buf.write("\7u\2\2\u0114\u0115\7g\2\2\u0115\34\3\2\2\2\u0116\u0117")
        buf.write("\7G\2\2\u0117\u0118\7n\2\2\u0118\u0119\7u\2\2\u0119\u011a")
        buf.write("\7g\2\2\u011a\u011b\7K\2\2\u011b\u011c\7h\2\2\u011c\36")
        buf.write("\3\2\2\2\u011d\u011e\7G\2\2\u011e\u011f\7p\2\2\u011f\u0120")
        buf.write("\7f\2\2\u0120\u0121\7D\2\2\u0121\u0122\7q\2\2\u0122\u0123")
        buf.write("\7f\2\2\u0123\u0124\7{\2\2\u0124 \3\2\2\2\u0125\u0126")
        buf.write("\7G\2\2\u0126\u0127\7p\2\2\u0127\u0128\7f\2\2\u0128\u0129")
        buf.write("\7K\2\2\u0129\u012a\7h\2\2\u012a\"\3\2\2\2\u012b\u012c")
        buf.write("\7G\2\2\u012c\u012d\7p\2\2\u012d\u012e\7f\2\2\u012e\u012f")
        buf.write("\7H\2\2\u012f\u0130\7q\2\2\u0130\u0131\7t\2\2\u0131$\3")
        buf.write("\2\2\2\u0132\u0133\7G\2\2\u0133\u0134\7p\2\2\u0134\u0135")
        buf.write("\7f\2\2\u0135\u0136\7Y\2\2\u0136\u0137\7j\2\2\u0137\u0138")
        buf.write("\7k\2\2\u0138\u0139\7n\2\2\u0139\u013a\7g\2\2\u013a&\3")
        buf.write("\2\2\2\u013b\u013c\7H\2\2\u013c\u013d\7q\2\2\u013d\u013e")
        buf.write("\7t\2\2\u013e(\3\2\2\2\u013f\u0140\7H\2\2\u0140\u0141")
        buf.write("\7w\2\2\u0141\u0142\7p\2\2\u0142\u0143\7e\2\2\u0143\u0144")
        buf.write("\7v\2\2\u0144\u0145\7k\2\2\u0145\u0146\7q\2\2\u0146\u0147")
        buf.write("\7p\2\2\u0147*\3\2\2\2\u0148\u0149\7K\2\2\u0149\u014a")
        buf.write("\7h\2\2\u014a,\3\2\2\2\u014b\u014c\7R\2\2\u014c\u014d")
        buf.write("\7c\2\2\u014d\u014e\7t\2\2\u014e\u014f\7c\2\2\u014f\u0150")
        buf.write("\7o\2\2\u0150\u0151\7g\2\2\u0151\u0152\7v\2\2\u0152\u0153")
        buf.write("\7g\2\2\u0153\u0154\7t\2\2\u0154.\3\2\2\2\u0155\u0156")
        buf.write("\7T\2\2\u0156\u0157\7g\2\2\u0157\u0158\7v\2\2\u0158\u0159")
        buf.write("\7w\2\2\u0159\u015a\7t\2\2\u015a\u015b\7p\2\2\u015b\60")
        buf.write("\3\2\2\2\u015c\u015d\7V\2\2\u015d\u015e\7j\2\2\u015e\u015f")
        buf.write("\7g\2\2\u015f\u0160\7p\2\2\u0160\62\3\2\2\2\u0161\u0162")
        buf.write("\7X\2\2\u0162\u0163\7c\2\2\u0163\u0164\7t\2\2\u0164\64")
        buf.write("\3\2\2\2\u0165\u0166\7Y\2\2\u0166\u0167\7j\2\2\u0167\u0168")
        buf.write("\7k\2\2\u0168\u0169\7n\2\2\u0169\u016a\7g\2\2\u016a\66")
        buf.write("\3\2\2\2\u016b\u016c\7V\2\2\u016c\u016d\7t\2\2\u016d\u016e")
        buf.write("\7w\2\2\u016e\u016f\7g\2\2\u016f8\3\2\2\2\u0170\u0171")
        buf.write("\7H\2\2\u0171\u0172\7c\2\2\u0172\u0173\7n\2\2\u0173\u0174")
        buf.write("\7u\2\2\u0174\u0175\7g\2\2\u0175:\3\2\2\2\u0176\u0177")
        buf.write("\7G\2\2\u0177\u0178\7p\2\2\u0178\u0179\7f\2\2\u0179\u017a")
        buf.write("\7F\2\2\u017a\u017b\7q\2\2\u017b<\3\2\2\2\u017c\u017d")
        buf.write("\7-\2\2\u017d>\3\2\2\2\u017e\u017f\7-\2\2\u017f\u0180")
        buf.write("\7\60\2\2\u0180@\3\2\2\2\u0181\u0182\7/\2\2\u0182B\3\2")
        buf.write("\2\2\u0183\u0184\7/\2\2\u0184\u0185\7\60\2\2\u0185D\3")
        buf.write("\2\2\2\u0186\u0187\7,\2\2\u0187F\3\2\2\2\u0188\u0189\7")
        buf.write(",\2\2\u0189\u018a\7\60\2\2\u018aH\3\2\2\2\u018b\u018c")
        buf.write("\7^\2\2\u018cJ\3\2\2\2\u018d\u018e\7^\2\2\u018e\u018f")
        buf.write("\7\60\2\2\u018fL\3\2\2\2\u0190\u0191\7\'\2\2\u0191N\3")
        buf.write("\2\2\2\u0192\u0193\7#\2\2\u0193P\3\2\2\2\u0194\u0195\7")
        buf.write("(\2\2\u0195\u0196\7(\2\2\u0196R\3\2\2\2\u0197\u0198\7")
        buf.write("~\2\2\u0198\u0199\7~\2\2\u0199T\3\2\2\2\u019a\u019b\7")
        buf.write("?\2\2\u019b\u019c\7?\2\2\u019cV\3\2\2\2\u019d\u019e\7")
        buf.write("?\2\2\u019eX\3\2\2\2\u019f\u01a0\7#\2\2\u01a0\u01a1\7")
        buf.write("?\2\2\u01a1Z\3\2\2\2\u01a2\u01a3\7@\2\2\u01a3\\\3\2\2")
        buf.write("\2\u01a4\u01a5\7>\2\2\u01a5^\3\2\2\2\u01a6\u01a7\7@\2")
        buf.write("\2\u01a7\u01a8\7?\2\2\u01a8`\3\2\2\2\u01a9\u01aa\7>\2")
        buf.write("\2\u01aa\u01ab\7?\2\2\u01abb\3\2\2\2\u01ac\u01ad\7?\2")
        buf.write("\2\u01ad\u01ae\7\61\2\2\u01ae\u01af\7?\2\2\u01afd\3\2")
        buf.write("\2\2\u01b0\u01b1\7>\2\2\u01b1\u01b2\7\60\2\2\u01b2f\3")
        buf.write("\2\2\2\u01b3\u01b4\7@\2\2\u01b4\u01b5\7\60\2\2\u01b5h")
        buf.write("\3\2\2\2\u01b6\u01b7\7@\2\2\u01b7\u01b8\7?\2\2\u01b8\u01b9")
        buf.write("\7\60\2\2\u01b9j\3\2\2\2\u01ba\u01bb\7>\2\2\u01bb\u01bc")
        buf.write("\7?\2\2\u01bc\u01bd\7\60\2\2\u01bdl\3\2\2\2\u01be\u01bf")
        buf.write("\7*\2\2\u01bfn\3\2\2\2\u01c0\u01c1\7+\2\2\u01c1p\3\2\2")
        buf.write("\2\u01c2\u01c3\7]\2\2\u01c3r\3\2\2\2\u01c4\u01c5\7_\2")
        buf.write("\2\u01c5t\3\2\2\2\u01c6\u01c7\7}\2\2\u01c7v\3\2\2\2\u01c8")
        buf.write("\u01c9\7\177\2\2\u01c9x\3\2\2\2\u01ca\u01cb\7<\2\2\u01cb")
        buf.write("z\3\2\2\2\u01cc\u01cd\7=\2\2\u01cd|\3\2\2\2\u01ce\u01cf")
        buf.write("\7.\2\2\u01cf~\3\2\2\2\u01d0\u01d1\7\60\2\2\u01d1\u0080")
        buf.write("\3\2\2\2\u01d2\u01d4\t\21\2\2\u01d3\u01d2\3\2\2\2\u01d4")
        buf.write("\u01d5\3\2\2\2\u01d5\u01d3\3\2\2\2\u01d5\u01d6\3\2\2\2")
        buf.write("\u01d6\u01d7\3\2\2\2\u01d7\u01d8\bA\2\2\u01d8\u0082\3")
        buf.write("\2\2\2\u01d9\u01e1\7$\2\2\u01da\u01db\7^\2\2\u01db\u01e0")
        buf.write("\t\17\2\2\u01dc\u01dd\7)\2\2\u01dd\u01e0\7$\2\2\u01de")
        buf.write("\u01e0\n\22\2\2\u01df\u01da\3\2\2\2\u01df\u01dc\3\2\2")
        buf.write("\2\u01df\u01de\3\2\2\2\u01e0\u01e3\3\2\2\2\u01e1\u01df")
        buf.write("\3\2\2\2\u01e1\u01e2\3\2\2\2\u01e2\u01e4\3\2\2\2\u01e3")
        buf.write("\u01e1\3\2\2\2\u01e4\u01e5\7^\2\2\u01e5\u01e6\n\17\2\2")
        buf.write("\u01e6\u01e7\bB\4\2\u01e7\u0084\3\2\2\2\u01e8\u01f0\7")
        buf.write("$\2\2\u01e9\u01ea\7^\2\2\u01ea\u01ef\t\17\2\2\u01eb\u01ec")
        buf.write("\7)\2\2\u01ec\u01ef\7$\2\2\u01ed\u01ef\n\22\2\2\u01ee")
        buf.write("\u01e9\3\2\2\2\u01ee\u01eb\3\2\2\2\u01ee\u01ed\3\2\2\2")
        buf.write("\u01ef\u01f2\3\2\2\2\u01f0\u01ee\3\2\2\2\u01f0\u01f1\3")
        buf.write("\2\2\2\u01f1\u01f3\3\2\2\2\u01f2\u01f0\3\2\2\2\u01f3\u01f4")
        buf.write("\bC\5\2\u01f4\u0086\3\2\2\2\u01f5\u01f6\7,\2\2\u01f6\u01f7")
        buf.write("\7,\2\2\u01f7\u01fb\3\2\2\2\u01f8\u01fa\13\2\2\2\u01f9")
        buf.write("\u01f8\3\2\2\2\u01fa\u01fd\3\2\2\2\u01fb\u01fc\3\2\2\2")
        buf.write("\u01fb\u01f9\3\2\2\2\u01fc\u01fe\3\2\2\2\u01fd\u01fb\3")
        buf.write("\2\2\2\u01fe\u01ff\bD\6\2\u01ff\u0088\3\2\2\2\u0200\u0201")
        buf.write("\13\2\2\2\u0201\u0202\bE\7\2\u0202\u008a\3\2\2\2\33\2")
        buf.write("\u0091\u009f\u00a7\u00aa\u00b2\u00bb\u00c1\u00c7\u00cc")
        buf.write("\u00d1\u00d3\u00d8\u00dc\u00e1\u00e6\u00ea\u00f2\u00f4")
        buf.write("\u01d5\u01df\u01e1\u01ee\u01f0\u01fb\b\b\2\2\3\t\2\3B")
        buf.write("\3\3C\4\3D\5\3E\6")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMENT = 1
    ID = 2
    DEC = 3
    HEXA = 4
    OCTAL = 5
    FLOAT = 6
    STRING = 7
    BODY = 8
    BREAK = 9
    CONTINUE = 10
    DO = 11
    ELSE = 12
    ELSEIF = 13
    ENDBODY = 14
    ENDIF = 15
    ENDFOR = 16
    ENDWHILE = 17
    FOR = 18
    FUNCTION = 19
    IF = 20
    PARAMETER = 21
    RETURN = 22
    THEN = 23
    VAR = 24
    WHILE = 25
    TRUE = 26
    FALSE = 27
    ENDDO = 28
    ADD = 29
    ADDF = 30
    SUB = 31
    SUBF = 32
    MUL = 33
    MULF = 34
    DIV = 35
    DIVF = 36
    MODUL = 37
    NOT = 38
    AND = 39
    OR = 40
    EQ = 41
    ASS = 42
    NEQ = 43
    GREATER = 44
    LESS = 45
    GEQ = 46
    LEQ = 47
    NEQF = 48
    LESSF = 49
    GREATERF = 50
    GEQF = 51
    LEQF = 52
    LP = 53
    RP = 54
    LS = 55
    RS = 56
    LB = 57
    RB = 58
    COLON = 59
    SM = 60
    CM = 61
    DOT = 62
    WS = 63
    ILLEGAL_ESCAPE = 64
    UNCLOSE_STRING = 65
    UNTERMINATED_COMMENT = 66
    ERROR_CHAR = 67

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
            "COMMENT", "ID", "DEC", "HEXA", "OCTAL", "FLOAT", "STRING", 
            "BODY", "BREAK", "CONTINUE", "DO", "ELSE", "ELSEIF", "ENDBODY", 
            "ENDIF", "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", 
            "RETURN", "THEN", "VAR", "WHILE", "TRUE", "FALSE", "ENDDO", 
            "ADD", "ADDF", "SUB", "SUBF", "MUL", "MULF", "DIV", "DIVF", 
            "MODUL", "NOT", "AND", "OR", "EQ", "ASS", "NEQ", "GREATER", 
            "LESS", "GEQ", "LEQ", "NEQF", "LESSF", "GREATERF", "GEQF", "LEQF", 
            "LP", "RP", "LS", "RS", "LB", "RB", "COLON", "SM", "CM", "DOT", 
            "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "UNTERMINATED_COMMENT", 
            "ERROR_CHAR" ]

    ruleNames = [ "COMMENT", "DIGIT", "ID", "DEC", "HEXA", "OCTAL", "FLOAT", 
                  "STRING", "BODY", "BREAK", "CONTINUE", "DO", "ELSE", "ELSEIF", 
                  "ENDBODY", "ENDIF", "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", 
                  "IF", "PARAMETER", "RETURN", "THEN", "VAR", "WHILE", "TRUE", 
                  "FALSE", "ENDDO", "ADD", "ADDF", "SUB", "SUBF", "MUL", 
                  "MULF", "DIV", "DIVF", "MODUL", "NOT", "AND", "OR", "EQ", 
                  "ASS", "NEQ", "GREATER", "LESS", "GEQ", "LEQ", "NEQF", 
                  "LESSF", "GREATERF", "GEQF", "LEQF", "LP", "RP", "LS", 
                  "RS", "LB", "RB", "COLON", "SM", "CM", "DOT", "WS", "ILLEGAL_ESCAPE", 
                  "UNCLOSE_STRING", "UNTERMINATED_COMMENT", "ERROR_CHAR" ]

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
            actions[64] = self.ILLEGAL_ESCAPE_action 
            actions[65] = self.UNCLOSE_STRING_action 
            actions[66] = self.UNTERMINATED_COMMENT_action 
            actions[67] = self.ERROR_CHAR_action 
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

     


