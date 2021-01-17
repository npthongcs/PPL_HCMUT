import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """ int a,y,w; """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,401))
        input = """ float foo(){
            int a,b,c;
            a = b / 2.0;
            c = a + c;
            return a*b*c; """
        expect = "Error on line 5 col 26: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,402))
        input = """ float foo(){
            int a,b,c;
            a = b / 2.0;
            c = a + c;
            return a*b*c;
            } """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,403))
        input = """ int ; """
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input,expect,404))
        input = """ float foo(){
            int a,b,c;
            a = b / 2.0;
            c = a + c;
            return a*b*c;
            }
            float main(int x,y,z; float g,h,j){
                return foo();
            } """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,405))
       
    
    def test_wrong_miss_close(self):
        """Miss variable"""
        