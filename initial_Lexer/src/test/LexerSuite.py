import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("tutorial","tutorial,<EOF>",500))
        self.assertTrue(TestLexer.checkLexeme("tu23torial program","tu23torial,program,<EOF>",501))
        self.assertTrue(TestLexer.checkLexeme("tutorial PPL","tutorial,Error Token P",502))
        self.assertTrue(TestLexer.checkLexeme("0tutorial","Error Token 0",503))
        self.assertTrue(TestLexer.checkLexeme("tutOrial","tut,Error Token O",504))
        self.assertTrue(TestLexer.checkLexeme("17.0","17.0,<EOF>",505))
        self.assertTrue(TestLexer.checkLexeme("-213.0","-,213.0,<EOF>",506))
        self.assertTrue(TestLexer.checkLexeme("1.","Error Token 1",507))
        self.assertTrue(TestLexer.checkLexeme("0.000001 -0.12e-192 12.213e-123 362e-13","0.000001,-,0.12e-192,12.213e-123,362e-13,<EOF>",508))
        self.assertTrue(TestLexer.checkLexeme(" 'abc' ","'abc',<EOF>",509))
        self.assertTrue(TestLexer.checkLexeme(" 'abc\"xyz' ","'abc\"xyz',<EOF>",510))
        self.assertTrue(TestLexer.checkLexeme(" 'abc\"xyz ","Error Token '",511))
         

    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.checkLexeme("Var","Var,<EOF>",102))

    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("ab?svn","ab,Error Token ?",103))

    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("Var x;","Var,x,;,<EOF>",104))

    def test_illegal_escape(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\h def"  ""","""Illegal Escape In String: abc\\h""",105))

    def test_unterminated_string(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc def  ""","""Unclosed String: abc def  """,106))

    def test_normal_string_with_escape(self):
        """test normal string with escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "ab'"c\\n def"  ""","""ab'"c\\n def,<EOF>""",107))
        

