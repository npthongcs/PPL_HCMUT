import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    
    def test_illegal_escape_04(self):
        self.assertTrue(TestLexer.checkLexeme(""" "ntvien\n\r\t" """, """Unclosed String: ntvien""", 1000))
    
    def test_1(self):
        """test keywords"""
        self.assertTrue(TestLexer.checkLexeme(
"""Body Break Continue Do EndIf""",
"""Body,Break,Continue,Do,EndIf,<EOF>""",1))
        
    def test_2(self):
        """test float number"""
        self.assertTrue(TestLexer.checkLexeme(
"""12e-10 12. 0.00000001e-10 12.1002 113e12 10.00000e-12 12345.e-12""",
"12e-10,12.,0.00000001e-10,12.1002,113e12,10.00000e-12,12345.e-12,<EOF>",2))
        
    def test_3(self):
        """test integer number"""
        self.assertTrue(TestLexer.checkLexeme(
"""123 1332 2421 42223 19833 24712 274 2741""",
"123,1332,2421,42223,19833,24712,274,2741,<EOF>",3))
        
    def test_4(self):
        """test float number"""
        self.assertTrue(TestLexer.checkLexeme(
"""12e-10 12.e -0.00000001e-10 12.1002 113e12 10.00000e-12 -12345.e-12 """,
"12e-10,12.,e,-,0.00000001e-10,12.1002,113e12,10.00000e-12,-,12345.e-12,<EOF>",4))
        
    def test_5(self):
        """test integer number"""
        self.assertTrue(TestLexer.checkLexeme(
"""123 -1332 0 -2421 42223 -19833 24712 274 2741 """,
"""123,-,1332,0,-,2421,42223,-,19833,24712,274,2741,<EOF>""",5))
        
    def test_6(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(
""" "abc function" """,
"""abc function,<EOF>""",6))
        
    def test_7(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(
""" "abc\\n fucntion" """,
"""abc\\n fucntion,<EOF>""",7))
        
    def test_8(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(
""" "abc\\f fucntion" """,
"abc\\f fucntion,<EOF>",8))
        
    def test_9(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(
""" "abc\\r fucntion" """,
"""abc\\r fucntion,<EOF>""",9))
        
    def test_10(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\t fucntion" """,
"abc\\t fucntion,<EOF>",10))
        
    def test_11(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(
""" "abc\\b fucntion" """,
"abc\\b fucntion,<EOF>",11))
        
    def test_12(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(
""" "abc\\\\ fucntion" """,
"abc\\\\ fucntion,<EOF>",12))
        
    def test_13(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(
""" "abc\\' fucntion" """,
"abc\\' fucntion,<EOF>",13))
        
    def test_14(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(
""" "abc'" fucntion" """,
"""abc'" fucntion,<EOF>""",14))
        
    def test_15(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(
""" "function \\n declare \\b \\t" """,
"function \\n declare \\b \\t,<EOF>",15))
        
    def test_16(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(
""" "function\\\\ de\\nclare \\b \\t 12" """,
"function\\\\ de\\nclare \\b \\t 12,<EOF>",16))
        
    def test_17(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(
""" "c++ python java"  """,
"c++ python java,<EOF>",17))
        
    def test_18(self):
        """test comment"""
        self.assertTrue(TestLexer.checkLexeme(
""" **abc function** """,
"<EOF>",18))
        
    def test_19(self):
        """test comment"""
        self.assertTrue(TestLexer.checkLexeme(
""" **abc 12 12 12 function***** """,
"Unterminated Comment",19))
        
    def test_20(self):
        """test comment"""
        self.assertTrue(TestLexer.checkLexeme(
""" **   "abc"              **  """,
"<EOF>",20))
        
    def test_21(self):
        """test comment"""
        self.assertTrue(TestLexer.checkLexeme(
""" **** """,
"<EOF>",21))
        
    def test_22(self):
        """test comment"""
        self.assertTrue(TestLexer.checkLexeme(
""" **
knvdksv
vndssd
dncds
dncdjcbsd
** """,
"<EOF>",22))
        
    def test_23(self):
        """test comment"""
        self.assertTrue(TestLexer.checkLexeme(
""" **abc
*csjac
*xdsnvb\\fv
*** """,
"*,<EOF>",23))
        
    def test_24(self):
        """test comment"""
        self.assertTrue(TestLexer.checkLexeme(
""" ***** """,
"*,<EOF>",24))
        
    def test_25(self):
        """test ID"""
        self.assertTrue(TestLexer.checkLexeme(
"""function var declare""",
"function,var,declare,<EOF>",25))
        
    def test_26(self):
        """test ID"""
        self.assertTrue(TestLexer.checkLexeme(
"""fun113ction var declare""",
"fun113ction,var,declare,<EOF>",26))
        
    def test_27(self):
        """test ID"""
        self.assertTrue(TestLexer.checkLexeme(
"""12function var dec0lare""",
"12,function,var,dec0lare,<EOF>",27))
        
    def test_28(self):
        """test ID"""
        self.assertTrue(TestLexer.checkLexeme(
"""function var declare init_array""",
"function,var,declare,init_array,<EOF>",28))
        
    def test_29(self):
        """test ID"""
        self.assertTrue(TestLexer.checkLexeme(
"""function var declare int____""",
"function,var,declare,int____,<EOF>",29))
        
    def test_30(self):
        """test ID"""
        self.assertTrue(TestLexer.checkLexeme(
"""function_ var__ declare___""",
"function_,var__,declare___,<EOF>",30))
        
    def test_31(self):
        """test ID"""
        self.assertTrue(TestLexer.checkLexeme(
"""funCtion var dECLARE""",
"funCtion,var,dECLARE,<EOF>",31))
        
    def test_32(self):
        """test ID"""
        self.assertTrue(TestLexer.checkLexeme(
"""_function var declare""",
"Error Token _",32))
        
    def test_33(self):
        """test ID"""
        self.assertTrue(TestLexer.checkLexeme(
"""function? var declare""",
"function,Error Token ?",33))
        
    def test_34(self):
        """test ID"""
        self.assertTrue(TestLexer.checkLexeme(
"""function$ var declare""",
"function,Error Token $",34))
        
    def test_35(self):
        """test ID"""
        self.assertTrue(TestLexer.checkLexeme(
""" function 1234variable""",
"function,1234,variable,<EOF>",35))
        
    def test_36(self):
        """test ID"""
        self.assertTrue(TestLexer.checkLexeme(
""" function\\n 1234variable""",
"function,\\,n,1234,variable,<EOF>",36))
        
    def test_37(self):
        """test array"""
        self.assertTrue(TestLexer.checkLexeme(
"""a[10]""",
"a,[,10,],<EOF>",37))
        
    def test_38(self):
        """test array"""
        self.assertTrue(TestLexer.checkLexeme(
"""a[10] b[10][10][10][10]""",
"a,[,10,],b,[,10,],[,10,],[,10,],[,10,],<EOF>",38))
        
    def test_39(self):
        """test array"""
        self.assertTrue(TestLexer.checkLexeme(
"""a[3]={10,10,10}""",
"a,[,3,],=,{,10,,,10,,,10,},<EOF>",39))
        
    def test_40(self):
        """test array"""
        self.assertTrue(TestLexer.checkLexeme(
"""a[2][3]={{1,2,3},{1,2,3}}""",
"a,[,2,],[,3,],=,{,{,1,,,2,,,3,},,,{,1,,,2,,,3,},},<EOF>",40))
        
    def test_41(self):
        """test float"""
        self.assertTrue(TestLexer.checkLexeme(
"""12.E""",
"12.,Error Token E",41))
        
    def test_42(self):
        """test ID"""
        self.assertTrue(TestLexer.checkLexeme(
"""abdjdv$""",
"abdjdv,Error Token $",42))
        
    def test_43(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(
""" "! @ # $ % ^ & *" """,
"! @ # $ % ^ & *,<EOF>",43))
    
    def test_44(self):
        """test float int"""
        self.assertTrue(TestLexer.checkLexeme(
"""123.123.123.123""",
"123.123,.,123.123,<EOF>",44))
        
    def test_45(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(
"""0000000000.1""",
"0000000000.1,<EOF>",45))
        
    def test_46(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(
""" "abc """,
"Unclosed String: abc ",46))
        
    def test_47(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(
""" "function declare """,
"Unclosed String: function declare ",47))
        
    def test_48(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(
""" "abc\\n fucntion\\p" """,
"Illegal Escape In String: abc\\n fucntion\\p",48))
        
    def test_49(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(
""" "abc\\k fucntion\\n" """,
"Illegal Escape In String: abc\\k",49))
        
    def test_50(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(
""" "abc\\n fucntion\\' declare \\\\ PPL code" """,
"""abc\\n fucntion\\' declare \\\\ PPL code,<EOF>""",50))
        
    def test_51(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(
""" "abc\\n fucntion\\' dec\\qlare \\\\ PPL code" """,
"Illegal Escape In String: abc\\n fucntion\\' dec\\q",51))
        
    def test_52(self):
        """test hexa"""
        self.assertTrue(TestLexer.checkLexeme(
"""0x1233 0X123""",
"0x1233,0X123,<EOF>",52))
        
    def test_53(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(
"""0o123 0O123""",
"0o123,0O123,<EOF>",53))
        
    def test_54(self):
        """test mix"""
        self.assertTrue(TestLexer.checkLexeme(
"""123 -123 12.e 12.-10 12e. 12e-10 0.1 e-0""",
"123,-,123,12.,e,12.,-,10,12,e,.,12e-10,0.1,e,-,0,<EOF>",54))
        
    def test_55(self):
        """test mix"""
        self.assertTrue(TestLexer.checkLexeme(
"""0X123 -123 12.e 12.-10 12E. 12e-10 0.1 e-0""",
"0X123,-,123,12.,e,12.,-,10,12,Error Token E",55))
        
    def test_56(self):
        """test operator"""
        self.assertTrue(TestLexer.checkLexeme(
"""+ - * \\ \\. > <. <= >.""",
"+,-,*,\\,\\.,>,<.,<=,>.,<EOF>",56))
        
    def test_57(self):
        """test seperator"""
        self.assertTrue(TestLexer.checkLexeme(
"""  {} [] . : ; , ()""",
"{,},[,],.,:,;,,,(,),<EOF>",57))
        
    def test_58(self):
        """test Unterminated Comment"""
        self.assertTrue(TestLexer.checkLexeme(
""" **fucntion declare volleyball""",
"Unterminated Comment",58))
        
    def test_59(self):
        """test Unterminated Comment"""
        self.assertTrue(TestLexer.checkLexeme(
""" **fucntion declare volleyball** 
** 123456 ****""",
"Unterminated Comment",59))
        
    def test_60(self):
        """test Unterminated Comment"""
        self.assertTrue(TestLexer.checkLexeme(
""" c++ python java **fucntion declare volleyball""",
"c,+,+,python,java,Unterminated Comment",60))
        
    def test_61(self):
        """test Unterminated Comment"""
        self.assertTrue(TestLexer.checkLexeme(
""" ***************""",
"Unterminated Comment",61))
        
    def test_62(self):
        """test hexa"""
        self.assertTrue(TestLexer.checkLexeme(
"""0x123ABC 0X129Fk""",
"0x123ABC,0X129F,k,<EOF>",62))
        
    def test_63(self):
        """test octal"""
        self.assertTrue(TestLexer.checkLexeme(
"""0o123abc 0O129k""",
"0o123,abc,0O12,9,k,<EOF>",63))
        
    def test_64(self):
        """test ..."""
        self.assertTrue(TestLexer.checkLexeme(
"""Var: a,b,c,d,e;""",
"Var,:,a,,,b,,,c,,,d,,,e,;,<EOF>",64))
        
    def test_65(self):
        """test ..."""
        self.assertTrue(TestLexer.checkLexeme(
"""Var: a,b[6],d[7][10];""",
"Var,:,a,,,b,[,6,],,,d,[,7,],[,10,],;,<EOF>",65))
        
    def test_66(self):
        """test ..."""
        self.assertTrue(TestLexer.checkLexeme(
"""Var: a,f=7,b[6]={1,2,3,4,5,6},d[7][10];""",
"Var,:,a,,,f,=,7,,,b,[,6,],=,{,1,,,2,,,3,,,4,,,5,,,6,},,,d,[,7,],[,10,],;,<EOF>",66))
        
    def test_67(self):
        """test ..."""
        self.assertTrue(TestLexer.checkLexeme(
"""Var: check=True, a[2][2]={{},{1,2}};""",
"Var,:,check,=,True,,,a,[,2,],[,2,],=,{,{,},,,{,1,,,2,},},;,<EOF>",67))
        
    def test_68(self):
        """test ..."""
        self.assertTrue(TestLexer.checkLexeme(
"""string: "abc\\n fucntion '" variable\\t?" """,
"""string,:,abc\\n fucntion '" variable\\t?,<EOF>""",68))
        
    def test_69(self):
        """test ..."""
        self.assertTrue(TestLexer.checkLexeme(
"""123 0x123 0o34 **comment** "abc\\n" """,
"""123,0x123,0o34,abc\\n,<EOF>""",69))
        
    def test_70(self):
        """test ..."""
        self.assertTrue(TestLexer.checkLexeme(
"""x= (3.+.5e-10)\\k+foo();""",
"x,=,(,3.,+.,5e-10,),\,k,+,foo,(,),;,<EOF>",70))
        
    def test_71(self):
        """test ..."""
        self.assertTrue(TestLexer.checkLexeme(
"""
** this is comment**
Var: x;
Function: fact
    Parameter: n
    Body: 
        If n==0 Then 
            Return 1;
        Else
            Return n*fact(n-1);
        EndIf.
    EndBody.
    
Function: main
    Body:
        x=10;
        fact(x);
    EndBody. """,
"""Var,:,x,;,Function,:,fact,Parameter,:,n,Body,:,If,n,==,0,Then,Return,1,;,Else,Return,n,*,fact,(,n,-,1,),;,EndIf,.,EndBody,.,Function,:,main,Body,:,x,=,10,;,fact,(,x,),;,EndBody,.,<EOF>""",71))
        
    def test_72(self):
        """test ..."""
        self.assertTrue(TestLexer.checkLexeme(
"""Var: s="this is assignment 1 ppl", p[10]={1,2,3} """,
"Var,:,s,=,this is assignment 1 ppl,,,p,[,10,],=,{,1,,,2,,,3,},<EOF>",72))
        
    def test_73(self):
        """test ..."""
        self.assertTrue(TestLexer.checkLexeme(
"""v = (4. \. 3.) *. 3.14 *. r *. r *. r;""",
"v,=,(,4.,\.,3.,),*.,3.14,*.,r,*.,r,*.,r,;,<EOF>",73))
        
    def test_74(self):
        """test ..."""
        self.assertTrue(TestLexer.checkLexeme(
""" If bool_of_string ("True") Then
        a = int_of_string (read ());
        b = float_of_int (a) +. 2.0;
    EndIf.""",
"""If,bool_of_string,(,True,),Then,a,=,int_of_string,(,read,(,),),;,b,=,float_of_int,(,a,),+.,2.0,;,EndIf,.,<EOF>""",74))
        
    def test_75(self):
        """test ..."""
        self.assertTrue(TestLexer.checkLexeme(
""" For (i = 0, i < 10, 2) Do
        writeln(i);
    EndFor. """,
"""For,(,i,=,0,,,i,<,10,,,2,),Do,writeln,(,i,),;,EndFor,.,<EOF>""",75))
        
    def test_76(self):
        """test ..."""
        self.assertTrue(TestLexer.checkLexeme(
"""** this is comment **
** 
skip
**
string = "assignment is very difficult\\n but I never give up"
win = 10 +.1 \. (sum(m,n)*.2) -.lose\.f  """,
"""string,=,assignment is very difficult\\n but I never give up,win,=,10,+.,1,\.,(,sum,(,m,,,n,),*.,2,),-.,lose,\.,f,<EOF>""",76))
        
    def test_77(self):
        """test ..."""
        self.assertTrue(TestLexer.checkLexeme(
"""6343 -274 12.122e-10 0000000000.1e-100000000 0x12AFC 0o123
"declare function variable\\p" """,
"6343,-,274,12.122e-10,0000000000.1e-100000000,0x12AFC,0o123,Illegal Escape In String: declare function variable\\p",77))
        
    def test_78(self):
        """test ..."""
        self.assertTrue(TestLexer.checkLexeme(
"""12.
12.e05
12.e-05
12.05e05
12.05e-05
12.05
0.05
0.05e05
0.05e-05""",
"12.,12.e05,12.e-05,12.05e05,12.05e-05,12.05,0.05,0.05e05,0.05e-05,<EOF>",78))
        
    def test_79(self):
        """test ..."""
        self.assertTrue(TestLexer.checkLexeme(
"""a[3 + foo(2)] = a[b[2][3]] + 4;""",
"a,[,3,+,foo,(,2,),],=,a,[,b,[,2,],[,3,],],+,4,;,<EOF>",79))
        
    def test_80(self):
        """test ..."""
        self.assertTrue(TestLexer.checkLexeme(
""" **
*a
*b
** """,
"""<EOF>""",80))
        
    def test_81(self):
        """test ..."""
        self.assertTrue(TestLexer.checkLexeme(
""" **** **** **** **** **** **** **** **** **** *
**** **** **** **** **** **** **** **** ****""",
"*,<EOF>",81))
        
    def test_82(self):
        """test ..."""
        self.assertTrue(TestLexer.checkLexeme(
"""val or val VariableName : DataType = [Initial Value]""",
"val,or,val,Var,iableName,:,Error Token D",82))
        
    def test_83(self):
        """test ..."""
        self.assertTrue(TestLexer.checkLexeme(
""" "There\\'s a girl but I let her get away It """,
"""Unclosed String: There\\'s a girl but I let her get away It """,83))
        
    def test_84(self):
        """test..."""
        self.assertTrue(TestLexer.checkLexeme(
"""import run_

object demo {
   def main(args: array[string]) {
      4 times println("hello")
   }
}""",
"""import,run_,object,demo,{,def,main,(,args,:,array,[,string,],),{,4,times,println,(,hello,),},},<EOF>""",84))
        
    def test_85(self):
        """test ..."""
        self.assertTrue(TestLexer.checkLexeme(
"""import java.io._

class point(val xc: int, val yc: int) {
   var x: int = xc
   var y: int = yc
   
   def move(dx: int, dy: int) {
      x = x + dx
      y = y + dy
   }
}

object demo {
   def main(args: array[string]) {
      val point = new point(10, 20)
      printpoint

      def printpoint{
         println ("Point x location : " + point.x);
         println ("Point y location : " + point.y);
      }
   }
}""",
"import,java,.,io,.,Error Token _",85))
        
    def test_86(self):
        """test ..."""
        self.assertTrue(TestLexer.checkLexeme(
"""class Point(val xc: int, val yc: int) {
   var x: int = xc
   var y: int = yc
   
   def move(dx: int, dy: int) {
      x = x + dx
      y = y + dy
      println ("Point x location : " + x);
      println ("Point y location : " + y);
   }
}

class location(override val xc: int, override val yc: int,
   val zc :int) extends point(xc, yc){
   var z: int = zc

   def move(dx: int, dy: int, dz: int) {
      x = x + dx
      y = y + dy
      z = z + dz
      println ("Point x location : " + x);
      println ("Point y location : " + y);
      println ("Point z location : " + z);
   }
}

object demo {
   def main(args: array[string]) {
      val loc = new location(10, 20, 15);

      ** Move to a new location **
      loc.move(10, 10, 5);
   }
} """,
"class,Error Token P",86))
        
    def test_87(self):
        """test ..."""
        self.assertTrue(TestLexer.checkLexeme(
"""**=============================**
   **           HELLO             **
   **=============================**""",
"<EOF>",87))
    
    def test_88(self):
        """test ..."""
        self.assertTrue(TestLexer.checkLexeme(
"""package society {
   package professional {
      class Executive {
         private[professional] var workDetails = null
         private[society] var friends = null
         private[this] var secrets = null

         def help(another : executive) {
            println(another.workdetails)
            println(another.secrets) **ERROR**
         }
      }
   }
}""",
"package,society,{,package,professional,{,class,Error Token E",88))
        
    def test_89(self):
        """test ..."""
        self.assertTrue(TestLexer.checkLexeme(
"""import java.io.fileReader
import java.io.fileNotFoundException
import java.io.iOException

object Demo {
   def main(args: Array[String]) {
      try {
         val f = new FileReader("input.txt")
      } catch {
         case ex: FileNotFoundException => {
            println("Missing file exception")
         }
         
         case ex: IOException => {
            println("IO Exception")
         }
      } finally {
         println("Exiting finally...")
      }
   }
}
""",
"import,java,.,io,.,fileReader,import,java,.,io,.,fileNotFoundException,import,java,.,io,.,iOException,object,Error Token D",89))
        
    def test_90(self):
        """test ..."""
        self.assertTrue(TestLexer.checkLexeme(
""" here is the calendar:
   january 2008
mo tu we th fr sa su
    1  2  3  4  5  6
 7  8  9 10 11 12 13
14 15 16 17 18 19 20
21 22 23 24 25 26 27
28 29 30 31 """,
"here,is,the,calendar,:,january,2008,mo,tu,we,th,fr,sa,su,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,<EOF>",90))
        
    def test_91(self):
        """test ..."""
        self.assertTrue(TestLexer.checkLexeme(
"""-1 if x < y, 0 if x == y, or 1 if x > y""",
"-,1,if,x,<,y,,,0,if,x,==,y,,,or,1,if,x,>,y,<EOF>",91))
        
    def test_92(self):
        """test ..."""
        self.assertTrue(TestLexer.checkLexeme(
"""class Employee:
   **Common base class for all employees**
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print '"Name : '", self.name,  '", Salary: '", self.salary""",
"class,Error Token E",92))
        
    def test_93(self):
        """test ..."""
        self.assertTrue(TestLexer.checkLexeme(
""""This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = employee("Manni", 5000)""",
"""This would create first object of Employee class,emp1,=,Error Token E""",93))
        
    def test_94(self):
        """test ..."""
        self.assertTrue(TestLexer.checkLexeme(
"""emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee d"  Employee.empCount""",
"""emp1,.,displayEmployee,(,),emp2,.,displayEmployee,(,),print,Total Employee d,Error Token E""",94))
        
    def test_95(self):
        """test ..."""
        self.assertTrue(TestLexer.checkLexeme(
"""hasattr(emp1,"age")    **Returns true if 'age' attribute exists**""",
"""hasattr,(,emp1,,,age,),<EOF>""",95))
        
    def test_96(self):
        """test ..."""
        self.assertTrue(TestLexer.checkLexeme(
"""hasattr(emp1, "age")    **Returns true if 'age' attribute exists""",
"hasattr,(,emp1,,,age,),Unterminated Comment",96))
        
    def test_97(self):
        """test ..."""
        self.assertTrue(TestLexer.checkLexeme(
"""class parent:        **define parent class**
   parentAttr = 100

   def parentMethod(self):
      print "Calling parent method"

   def setAttr(self, attr):
      parent.parentAttr = attr

   def getAttr(self):
      print "Parent attribute :", parent.parentAttr

class child(parent): ** define child class **

   def childMethod(self):
      print "Calling child method"

c = Child()          ** instance of child**
c.childMethod()      **child calls its method**
c.parentMethod()     **calls parent's method**
c.setAttr(200)       **again call parent's method**
c.getAttr()          **again call parent's method**""",
"class,parent,:,parentAttr,=,100,def,parentMethod,(,self,),:,print,Calling parent method,def,setAttr,(,self,,,attr,),:,parent,.,parentAttr,=,attr,def,getAttr,(,self,),:,print,Parent attribute :,,,parent,.,parentAttr,class,child,(,parent,),:,def,childMethod,(,self,),:,print,Calling child method,c,=,Error Token C",97))
        
    def test_98(self):
        """test"""
        self.assertTrue(TestLexer.checkLexeme(
"""Calling child constructor""",
"Error Token C",98))
         
    def test_99(self):
        self.assertTrue(TestLexer.checkLexeme(
""" "This is a string containing tab \\t"
"He asked me: '"Where is John?'"" """,
"""This is a string containing tab \\t,He asked me: '"Where is John?'",<EOF>""",99))
        
    def test_100(self):
        self.assertTrue(TestLexer.checkLexeme(
"""** nbcsdch **
1+2+3+4;
b[i+3+4] = 10 ;
a[1-d-f] = 10 ;
a[1-d-f] = 10 ;
Function: foo
Parameter: a,c,a[5][6]
Body: 
    Var: i=0,a[i*i];
    while i<5 Do
        i = i + 1;
        a[i][i+2]=i*i;
    EndWhile.
    Return 0;
EndBody. """,
"1,+,2,+,3,+,4,;,b,[,i,+,3,+,4,],=,10,;,a,[,1,-,d,-,f,],=,10,;,a,[,1,-,d,-,f,],=,10,;,Function,:,foo,Parameter,:,a,,,c,,,a,[,5,],[,6,],Body,:,Var,:,i,=,0,,,a,[,i,*,i,],;,while,i,<,5,Do,i,=,i,+,1,;,a,[,i,],[,i,+,2,],=,i,*,i,;,EndWhile,.,Return,0,;,EndBody,.,<EOF>",100))


