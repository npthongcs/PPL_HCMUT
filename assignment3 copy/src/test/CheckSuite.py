import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):

    # test redeclared variable

#     def test_201(self):
#         input = """
# Var: a,b,c,a;
# """
#         expect = ' '
#         self.assertTrue(TestChecker.test(input, expect, 201))
#
#     def test_202(self):
#         input = """
# Var: a[10][10],b,c=1,d="hello world",b[10];
# """
#         expect = ' '
#         self.assertTrue(TestChecker.test(input, expect, 202))
#
#     def test_203(self):
#         input = """
# Var: a,b[3]={1,2,3},e,f;
# Var: g,read;
# """
#         expect = ' '
#         self.assertTrue(TestChecker.test(input, expect, 203))
#
#     # test redeclared function
#
#     def test_204(self):
#         input = """
# Function: main
# Body:
# EndBody.
# Function: read
# Body:
# EndBody.
# Function: foo
# Body:
# EndBody.
# """
#         expect = ' '
#         self.assertTrue(TestChecker.test(input, expect, 204))
#
#     def test_205(self):
#         input = """
# Function: main
# Body:
# EndBody.
# Function: foo
# Body:
# EndBody.
# Function: foo
# Body:
# EndBody.
# """
#         expect = ' '
#         self.assertTrue(TestChecker.test(input, expect, 205))
#
#     def test_206(self):
#         input = """
# Var: foo,a[10];
# Function: main
# Body:
# EndBody.
# Function: sum
# Body:
# EndBody.
# Function: foo
# Body:
# EndBody.
# """
#         expect = ' '
#         self.assertTrue(TestChecker.test(input, expect, 206))
#
#     # redeclared variable, parameter
#
#     def test_207(self):
#         input = """
# Var: a,b=10,c=1;
# Function: main
# Parameter: a,b,c
# Body:
#     Var: a;
# EndBody.
# Function: foo
# Parameter: a
# Body:
# EndBody.
# """
#         expect = ' '
#         self.assertTrue(TestChecker.test(input, expect, 207))
#
#     def test_208(self):
#         input = """
# Var: a,b=10,c=1;
# Function: main
# Parameter: a,b,c,a
# Body:
# EndBody.
# Function: foo
# Parameter: a
# Body:
# EndBody.
# """
#         expect = ' '
#         self.assertTrue(TestChecker.test(input, expect, 208))
#
#     # test assignment statement
#
#     def test_209(self):
#         input = """
# Var: a,b=10,c=1,d[3][3],e[2]={1.0,2.0};
# Function: main
# Parameter: a,c
# Body:
#     a = 1.2;
#     a = b;
# EndBody.
# """
#         expect = ' '
#         self.assertTrue(TestChecker.test(input, expect, 209))
#
#     def test_210(self):
#         input = """
# Var: a,b=10,c=1,d[3][3],e[2]={1.0,2.0},g="hello",f=False,u,v;
# Function: main
# Body:
#     b = 1.2;
# EndBody.
# """
#         expect = ' '
#         self.assertTrue(TestChecker.test(input, expect, 210))
#
#     def test_211(self):
#         input = """
# Var: a,b=10,c=1,d[3][3],e[2]={1.0,2.0},g="hello",f=False,u,v;
# Function: main
# Parameter: a,c
# Body:
#     Var: g,f;
#     g = f + a + 100;
#     c = f +. 10.0 -. 1.2e-10;
# EndBody.
# """
#         expect = ' '
#         self.assertTrue(TestChecker.test(input, expect, 211))
#
#     def test_212(self):
#         input = """
# Var: a,b=10,c=1,d[3][3],e[2]={1.0,2.0},g="hello",f=False,u,v;
# Function: main
# Parameter: a
# Body:
#     Var: g,f;
#     b = d;
# EndBody.
# """
#         expect = ' '
#         self.assertTrue(TestChecker.test(input, expect, 212))
#
#     def test_213(self):
#         input = """
# Var: a,b=10,c=1,d[3][3],e[2]={1.0,2.0},g="hello",f=False,u,v;
# Function: main
# Parameter: a,c,i,j,k,m,n
# Body:
#     c = 1.2;
#     i = c;
#     n = i + j;
# EndBody.
# """
#         expect = ' '
#         self.assertTrue(TestChecker.test(input, expect, 213))
#
#     def test_214(self):
#         input = """
# Var: a,b=10,c=1,d[3][3],e[2]={1.0,2.0},g="hello",f=False,u,v;
# Function: main
# Parameter: a,c
# Body:
#     Var: g,f;
#     f = foo(12);
# EndBody.
#
# Function: foo
# Parameter: a
# Body:
# EndBody.
# """
#         expect = ' '
#         self.assertTrue(TestChecker.test(input, expect, 214))
#
#     def test_215(self):
#         input = """
# Var: a,b=10,c=1,d[3][3],e[2]={1.0,2.0},g,f=False,u,v;
# Function: main
# Parameter: a,c
# Body:
#     Var: g,f;
#     f = foo(False,True,1,1.2,b) + 1;
# EndBody.
#
# Function: foo
# Parameter: a,b,c,d
# Body:
# EndBody.
# """
#         expect = ' '
#         self.assertTrue(TestChecker.test(input, expect, 215))
#
#     # test undeclared function / variable
#
#     def test_216(self):
#         input = """
# Var: a,b=10,c=1,d[3][3],e[2]={1.0,2.0},g,f=False,u,v;
# Function: main
# Parameter: a,c
# Body:
#     Var: g,f;
#     f = foo1(False,True,1,1.2) + 1;
# EndBody.
#
# Function: foo
# Parameter: a,b,c,d
# Body:
# EndBody.
# """
#         expect = ' '
#         self.assertTrue(TestChecker.test(input, expect, 216))
#
#     def test_217(self):
#         input = """
# Var: a,b=10,c=1,d[3][3],e[2]={1.0,2.0},g,f=False,u,v;
# Function: main
# Parameter: a,c
# Body:
#     Var: g,f;
#     f = foo(False,True,k,b) + 1;
# EndBody.
#
# Function: foo
# Parameter: a,b,c,d
# Body:
# EndBody.
# """
#         expect = ' '
#         self.assertTrue(TestChecker.test(input, expect, 217))
#
#     # test call function
#
#     def test_218(self):
#         input = """
# Var: a,b=10,c=1,d[3][3],e[2]={1.0,2.0},g,f=False,u,v;
# Function: main
# Parameter: a,c
# Body:
#     Var: g,f;
#     f = foo(foo(foo()));
# EndBody.
#
# Function: foo
# Parameter: a
# Body:
# EndBody.
# """
#         expect = ' '
#         self.assertTrue(TestChecker.test(input, expect, 218))
#
#     def test_219(self):
#         input = """
# Var: a,b=10,c=1,d[3][3],e[2]={1.0,2.0},g,f=False,u,v;
# Function: main
# Parameter: a,c
# Body:
#     Var: g,f;
#     f = foo(foo(foo(2)));
#     f = u +. v;
# EndBody.
#
# Function: foo
# Parameter: a
# Body:
# EndBody.
# """
#         expect = ' '
#         self.assertTrue(TestChecker.test(input, expect, 219))
#
#     def test_220(self):
#         input = """
# Var: a,b=10,c=1,d[3][3],e[2]={1.0,2.0},g,f=False,u,v;
# Function: main
# Parameter: a,c
# Body:
#     Var: g,f;
#     f = foo(foo(foo(foo1())));
# EndBody.
#
# Function: foo
# Parameter: a
# Body:
# EndBody.
#
# Function: foo1
# Body:
# EndBody.
# """
#         expect = ' '
#         self.assertTrue(TestChecker.test(input, expect, 220))
#
#     def test_221(self):
#         input = """
# Var: a,b=10,c=1,d[3][3],e[2]={1.0,2.0},g,f=False,u,v;
# Function: main
# Parameter: a,c
# Body:
#     Var: g,f;
#     b = a + foo1();
#     f = foo(foo(foo(foo1())));
# EndBody.
#
# Function: foo
# Parameter: a
# Body:
#     a = 1.2;
# EndBody.
#
# Function: foo1
# Body:
# EndBody.
# """
#         expect = ' '
#         self.assertTrue(TestChecker.test(input, expect, 221))
#
#     def test_222(self):
#         input = """
# Var: a,b=10,c=1,d[3][3],e[2]={1.0,2.0},g,f=False,u,v;
# Function: main
# Parameter: a,c
# Body:
#     Var: g,f;
#     f = f % b;
#     u = foo(f,foo(True,False));
# EndBody.
#
# Function: foo
# Parameter: a,c
# Body:
# EndBody.
#
# Function: foo1
# Body:
# EndBody.
# """
#         expect = ' '
#         self.assertTrue(TestChecker.test(input, expect, 222))
#
#     def test_223(self):
#         input = """
# Var: a,b=10,c=1,d[3][3],e[2]={1.0,2.0},g,f=False,u,v;
# Function: main
# Parameter: a,c
# Body:
#     Var: g,f;
#     f = foo;
# EndBody.
#
# Function: foo
# Parameter: a
# Body:
# EndBody.
#
# Function: foo1
# Body:
# EndBody.
# """
#         expect = ' '
#         self.assertTrue(TestChecker.test(input, expect, 223))
#
#     def test_224(self):
#         input = """
# Var: a,b=10,c=1,d[3][3],e[2]={1.0,2.0},g,f=False,u,v;
# Function: main
# Parameter: a,c,main
# Body:
#     Var: g,f;
#     f = main()+1;
# EndBody.
#
# Function: foo
# Parameter: a
# Body:
# EndBody.
#
# Function: foo1
# Body:
# EndBody.
# """
#         expect = ' '
#         self.assertTrue(TestChecker.test(input, expect, 224))
#
#     def test_225(self):
#         input = """
# Var: a,b=10,c=1,d[3][3],e[2]={1.0,2.0},g,f=False,u,v;
# Function: main
# Parameter: a,c
# Body:
#     Var: g,f;
#     b = c[10];
# EndBody.
#
# Function: foo
# Parameter: a
# Body:
# EndBody.
#
# Function: foo1
# Body:
# EndBody.
# """
#         expect = ' '
#         self.assertTrue(TestChecker.test(input, expect, 225))
#
#     def test_226(self):
#         input = """
# Var: a,b=10,c=1,d[3][3],e[2]={1.0,2.0},g,f=False,u,v;
# Function: main
# Parameter: a,c
# Body:
#     Var: g,f;
#     u =1.2;
# EndBody.
#
# Function: foo
# Parameter: a
# Body:
# EndBody.
#
# Function: foo1
# Body:
#     u = 1;
# EndBody.
# """
#         expect = ' '
#         self.assertTrue(TestChecker.test(input, expect, 226))
#
#     def test_227(self):
#         input = """
# Var: a,b=10,c=1,d[3][3],e[2]={1.0,2.0},g,f=False,u,v;
# Function: main
# Parameter: a,c
# Body:
#     Var: g,f;
#     f = b + d[1][1];
#     d[3][2] = int_of_float(f);
# EndBody.
#
# Function: foo
# Parameter: a
# Body:
# EndBody.
#
# Function: foo1
# Body:
# EndBody.
# """
#         expect = ' '
#         self.assertTrue(TestChecker.test(input, expect, 227))
#
#     def test_228(self):
#         input = """
# Var: a,b=10,c=1.2,d[3][3],e[2]={1.0,2.0},g,f=False,u,v;
# Function: main
# Parameter: a,c
# Body:
#     d[3][2] = float_to_int(c);
#     d[1][2] = c;
# EndBody.
#
# Function: foo
# Parameter: a
# Body:
# EndBody.
#
# Function: foo1
# Body:
# EndBody.
# """
#         expect = ' '
#         self.assertTrue(TestChecker.test(input, expect, 228))
#
#     def test_229(self):
#         input = """
# Var: a,b=10,c=1.2,d[3][3],e[2]={1.0,2.0},g,f=False,u,v;
# Function: foo1
# Body:
#     a = 1.2;
#     Return int_of_float(a)>b;
# EndBody.
#
# Function: main
# Parameter: a,c
# Body:
#     a = foo1() && False;
#     a = foo(a) + foo1();
# EndBody.
#
# Function: foo
# Parameter: a
# Body:
# EndBody.
# """
#         expect = ' '
#         self.assertTrue(TestChecker.test(input, expect, 229))
#
#     def test_230(self):
#         input = """
# Var: a,b=10,c=1.2,d[3][3],e[2]={1.0,2.0},g,f=False,u,v;
# Function: foo1
# Body:
#     a = 12;
#     Return a;
# EndBody.
#
# Function: main
# Parameter: c
# Body:
#     c = foo(e[1]) + 1;
# EndBody.
#
# Function: foo
# Parameter: f
# Body:
#     f = foo1();
# EndBody.
# """
#         expect = ' '
#         self.assertTrue(TestChecker.test(input, expect, 230))
#
#     def test_231(self):
#         input = """
# Var: a,b=10,c=1.2,d[3][3],e[2]={1.0,2.0},g,f=False,u,v;
# Function: foo1
# Body:
#     Return e;
# EndBody.
#
# Function: main
# Parameter: c
# Body:
#     foo1()[2] = 1;
# EndBody.
#
# Function: foo
# Parameter: i,j,k
# Body:
#
# EndBody.
# """
#         expect = ' '
#         self.assertTrue(TestChecker.test(input, expect, 231))
#
#     def test_232(self):
#         input = """Var: a,b=10,c=1.2,d[3][3],e[2]={1.0,2.0},g,f=False,u,v;
# Function: foo1
# Body:
#     Return e;
# EndBody.
#
# Function: main
# Parameter: c
# Body:
#     foo1()[2][2] = 1.2;
# EndBody.
#
# Function: foo
# Parameter: i,j,k
# Body:
#
# EndBody.
# """
#         expect = ' '
#         self.assertTrue(TestChecker.test(input, expect, 232))
#
#     def test_233(self):
#         input = """
# Var: a,b=10,c=1.2,d[3][3],e[2]={1.0,2.0},g,f=False,u,v;
# Function: foo1
# Body:
#     Return e;
# EndBody.
#
# Function: main
# Parameter: c
# Body:
#     foo1()[2] = foo1();
# EndBody.
#
# Function: foo
# Parameter: i,j,k
# Body:
#
# EndBody.
# """
#         expect = ' '
#         self.assertTrue(TestChecker.test(input, expect, 233))
#
#     # if statement
#
#     def test_234(self):
#         input = """
# Var: a,b=10,c=1.2,d[3][3],e[2]={1.0,2.0},g,f=False,u,v;
# Function: foo1
# Body:
#     Return e;
# EndBody.
#
# Function: main
# Parameter: c
# Body:
#     If b==2 Then
#         main(main(f));
#     EndIf.
# EndBody.
#
# Function: foo
# Parameter: i,j,k
# Body:
#
# EndBody.
# """
#         expect = ' '
#         self.assertTrue(TestChecker.test(input, expect, 234))
#
#     def test_235(self):
#         input = """
# Var: a,b=10,c=1.2,d[3][3],e[2]={1.0,2.0},g,f=False,u,v;
# Function: foo1
# Parameter: i
# Body:
#     Return e;
# EndBody.
#
# Function: main
# Parameter: c
# Body:
#     c = foo1(foo(foo1(b)));
#     If c Then
#     EndIf.
# EndBody.
#
# Function: foo
# Parameter: i
# Body:
#
# EndBody.
# """
#         expect = ' '
#         self.assertTrue(TestChecker.test(input, expect, 235))
#
#     def test_236(self):
#         input = """
# Var: a,b=10,c=1.2,d[3][3],e[2]={1.0,2.0},g,f=False,u,v;
# Function: foo1
# Parameter: i
# Body:
#     Return e;
# EndBody.
#
# Function: main
# Parameter: c
# Body:
#     If True Then
#         Var: c,a,b;
#         c= 1.2;
#     EndIf.
#     c = 10;
# EndBody.
#
# Function: foo
# Parameter: i
# Body:
#
# EndBody.
# """
#         expect = ' '
#         self.assertTrue(TestChecker.test(input, expect, 236))
#
#     def test_237(self):
#         input = """
# Var: a,b=10,c=1.2,d[3][3],e[2]={1.0,2.0},g,f=False,u,v;
# Function: foo1
# Parameter: i
# Body:
#     Return e;
# EndBody.
#
# Function: main
# Parameter: c,b
# Body:
#     If True Then
#         Var: c,a,b;
#         c= 1.2;
#         Return c;
#     EndIf.
#     Return b;
#     b = 1;
# EndBody.
#
# Function: foo
# Parameter: i
# Body:
#
# EndBody.
# """
#         expect = ' '
#         self.assertTrue(TestChecker.test(input, expect, 237))
#
#     def test_238(self):
#         input = """
# Var: a,b=10,c=1.2,d[3][3],e[2]={1.0,2.0},g,f=False,u,v;
# Function: foo1
# Parameter: i1,i2,i3,i4,i5
# Body:
# EndBody.
#
# Function: foo2
# Body:
#     Var: a[2]={1.2,10.};
#     Return a;
# EndBody.
#
# Function: main
# Parameter: c,b
# Body:
#     If True Then
#         Var: c=1,a=1.2,b=True,f[2][2]={{1,2},{1,2}};
#         foo1(c,e[2],foo2()[2],foo(foo2()),f[1][2]);
#         If a>.float_to_int(c) Then
#             Var: c,a;
#             foo1(c,False,foo2()[2],foo(foo2()),f[1][2]);
#         EndIf.
#         Return c;
#     EndIf.
#     Return b;
# EndBody.
#
# Function: foo
# Parameter: i
# Body:
# EndBody.
# """
#         expect = ' '
#         self.assertTrue(TestChecker.test(input, expect, 238))
#
#     def test_239(self):
#         input = """
# Var: a,b=10,c=1.2,d[3][3],e[2]={1.0,2.0},g,f=False,u,v;
# Function: foo1
# Parameter: i1,i2,i3,i4,i5
# Body:
# EndBody.
#
# Function: foo2
# Body:
#     Var: a[2]={1.2,10.};
#     Return a;
# EndBody.
#
# Function: main
# Parameter: c,b
# Body:
#     If True Then
#         Var: c=1,a=1.2,b=True,f[2][2]={{1,2},{1,2}};
#         If a>.float_to_int(c) Then
#             foo();
#             Return a;
#         EndIf.
#         Return float_to_int(c);
#     EndIf.
#     Return float_to_int(f[1][1]);
# EndBody.
#
# Function: foo
# Body:
#     Return main(1,1);
# EndBody.
# """
#         expect = ' '
#         self.assertTrue(TestChecker.test(input, expect, 239))
#
#     def test_240(self):
#         input = """
# Var: a,b=1,d=1.2,e[2][2];
# Function: main
# Body:
#     Var: b=1.2;
#     If b>.d Then
#         Return d;
#     Else
#         Var: b[2]={17,19};
#         Return e[1][2] + b[2];
#     EndIf.
# EndBody.
# """
#         expect = ' '
#         self.assertTrue(TestChecker.test(input, expect, 240))
#
#     def test_241(self):
#         input = """
# Var: n;
# Function: main
# Body:
#     Var: m,a,c,b;
#     n = read();
#     a = bool_of_string(n);
#     If a Then
#         Var: max=0,i,j;
#         j = read();
#         i = int_of_string(j);
#         If i>max Then
#             i = i+1;
#             printStr(string_of_int(i));
#             printLn();
#         Else
#             printStrLn("invalid i, please enter again");
#         EndIf.
#     Else Return "error, please check carefully again!";
#     EndIf.
#     Return ;
# EndBody.
# """
#         expect = ' '
#         self.assertTrue(TestChecker.test(input, expect, 241))
#
#     def test_242(self):
#         input = """
# Function : print
# Parameter : x
# Body:
#     Return;
# EndBody.
#
# Function: m
# Body:
#     Var : value = 12345;
#     Return value;
# EndBody.
#
# Function: main
# Parameter : x, y
# Body:
#     print(m);
#     Return 0;
# EndBody.
# """
#         expect = ' '
#         self.assertTrue(TestChecker.test(input, expect, 242))
#
#     def test_243(self):
#         input = """
# Var: n;
# Function: main
# Body:
#     Var: m,a,c,b;
#     n = read();
#     a = bool_of_string(n);
#     If a Then
#         Var: max=0,i,j;
#         j = read();
#         i = int_of_string(j);
#         If i>max Then
#             i = i+1;
#             printStr(string_of_int(i));
#             printLn();
#         ElseIf i<max-2 Then
#         ElseIf i<max-2 Then
#             max = max * 2;
#             printStrLn("invalid i, please enter again");
#         EndIf.
#     Else Return "error, please check carefully again!";
#     EndIf.
#     Return ;
# EndBody.
# """
#         expect = ' '
#         self.assertTrue(TestChecker.test(input, expect, 243))
#
#     def test_244(self):
#         input = """
# Function: main
# Parameter: a,x
# Body:
#     x = x + foo(foo(x));
# EndBody.
#
# Function: foo
# Parameter: x
# Body:
# EndBody.
# """
#         expect = ' '
#         self.assertTrue(TestChecker.test(input, expect, 244))
#
#     def test_245(self):
#         input = """
# Function: main
#         Parameter: global_var
#         Body:
#             global_var = 25+6-.2.5%3\\100 ;
#         EndBody.
# """
#         expect = ' '
#         self.assertTrue(TestChecker.test(input, expect, 245))

#     def test_246(self):
#         input = """
# Function: main
#         Parameter: x, y
#         Body:
#         x = main(main(1));
#         EndBody.
# """
#         expect = ' '
#         self.assertTrue(TestChecker.test(input, expect, 246))
#
#     def test_247(self):
#         input = """
# Var: a[1] = {0};
#
# Function: foo
#     Parameter: x
#     Body:
#         Return a;
#     EndBody.
#
# Function: main
#     Body:
#         foo(0)[0] = foo(0.0)[0];
#     EndBody.
# """
#         expect = ' '
#         self.assertTrue(TestChecker.test(input, expect, 247))
#
#     def test_248(self):
#         input = """
# Function: foo
#         Parameter: x
#         Body:
#         x=1.1;
#         Return { True };
#         EndBody.
#
#         Function: main
#         Parameter: x, y
#         Body:
#         foo(x)[0] = x || (x>y);
#         EndBody.
# """
#         expect = ' '
#         self.assertTrue(TestChecker.test(input, expect, 248))

    def test_249(self):
        input = """
Var: show;
            Function: move
            Parameter : x
            Body:
                Var: i;
                x = 5 + show;
                For (i = 0, i < 10, 2) Do
                    print("Hello");
                EndFor.
                Return 0;
            EndBody.

            Function: main
            Parameter : x
            Body:
                x = 5 + move;
            EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 249))

    def test_250(self):
        input = """
Function: main
Parameter: x
Body:
    If main(main(5)) Then EndIf. 
EndBody.       
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 250))
    #
    # def test_251(self):
    #     input = " "
    #     expect = ' '
    #     self.assertTrue(TestChecker.test(input, expect, 251))
    #
    # def test_252(self):
    #     input = " "
    #     expect = ' '
    #     self.assertTrue(TestChecker.test(input, expect, 252))
    #
    # def test_253(self):
    #     input = " "
    #     expect = ' '
    #     self.assertTrue(TestChecker.test(input, expect, 253))
    #
    # def test_254(self):
    #     input = " "
    #     expect = ' '
    #     self.assertTrue(TestChecker.test(input, expect, 254))
    #
    # def test_255(self):
    #     input = " "
    #     expect = ' '
    #     self.assertTrue(TestChecker.test(input, expect, 255))
    #
    # def test_256(self):
    #     input = " "
    #     expect = ' '
    #     self.assertTrue(TestChecker.test(input, expect, 256))
    #
    # def test_257(self):
    #     input = " "
    #     expect = ' '
    #     self.assertTrue(TestChecker.test(input, expect, 257))
    #
    # def test_258(self):
    #     input = " "
    #     expect = ' '
    #     self.assertTrue(TestChecker.test(input, expect, 258))
    #
    # def test_259(self):
    #     input = " "
    #     expect = ' '
    #     self.assertTrue(TestChecker.test(input, expect, 259))
    #
    # def test_260(self):
    #     input = " "
    #     expect = ' '
    #     self.assertTrue(TestChecker.test(input, expect, 260))
    #
    # def test_261(self):
    #     input = " "
    #     expect = ' '
    #     self.assertTrue(TestChecker.test(input, expect, 261))
    #
    # def test_262(self):
    #     input = " "
    #     expect = ' '
    #     self.assertTrue(TestChecker.test(input, expect, 262))
    #
    # def test_263(self):
    #     input = " "
    #     expect = ' '
    #     self.assertTrue(TestChecker.test(input, expect, 263))
    #
    # def test_264(self):
    #     input = " "
    #     expect = ' '
    #     self.assertTrue(TestChecker.test(input, expect, 264))
    #
    # def test_265(self):
    #     input = " "
    #     expect = ' '
    #     self.assertTrue(TestChecker.test(input, expect, 265))
    #
    # def test_266(self):
    #     input = " "
    #     expect = ' '
    #     self.assertTrue(TestChecker.test(input, expect, 266))
    #
    # def test_267(self):
    #     input = " "
    #     expect = ' '
    #     self.assertTrue(TestChecker.test(input, expect, 267))
    #
    # def test_268(self):
    #     input = " "
    #     expect = ' '
    #     self.assertTrue(TestChecker.test(input, expect, 268))
    #
    # def test_269(self):
    #     input = " "
    #     expect = ' '
    #     self.assertTrue(TestChecker.test(input, expect, 269))
    #
    # def test_270(self):
    #     input = " "
    #     expect = ' '
    #     self.assertTrue(TestChecker.test(input, expect, 270))
    #
    # def test_271(self):
    #     input = " "
    #     expect = ' '
    #     self.assertTrue(TestChecker.test(input, expect, 271))
    #
    # def test_272(self):
    #     input = " "
    #     expect = ' '
    #     self.assertTrue(TestChecker.test(input, expect, 272))
    #
    # def test_273(self):
    #     input = " "
    #     expect = ' '
    #     self.assertTrue(TestChecker.test(input, expect, 273))
    #
    # def test_274(self):
    #     input = " "
    #     expect = ' '
    #     self.assertTrue(TestChecker.test(input, expect, 274))
    #
    # def test_275(self):
    #     input = " "
    #     expect = ' '
    #     self.assertTrue(TestChecker.test(input, expect, 275))
    #
    # def test_276(self):
    #     input = " "
    #     expect = ' '
    #     self.assertTrue(TestChecker.test(input, expect, 276))
    #
    # def test_277(self):
    #     input = " "
    #     expect = ' '
    #     self.assertTrue(TestChecker.test(input, expect, 277))
    #
    # def test_278(self):
    #     input = " "
    #     expect = ' '
    #     self.assertTrue(TestChecker.test(input, expect, 278))
    #
    # def test_279(self):
    #     input = " "
    #     expect = ' '
    #     self.assertTrue(TestChecker.test(input, expect, 279))
    #
    # def test_280(self):
    #     input = " "
    #     expect = ' '
    #     self.assertTrue(TestChecker.test(input, expect, 280))
    #
    # def test_281(self):
    #     input = " "
    #     expect = ' '
    #     self.assertTrue(TestChecker.test(input, expect, 281))
    #
    # def test_282(self):
    #     input = " "
    #     expect = ' '
    #     self.assertTrue(TestChecker.test(input, expect, 282))
    #
    # def test_283(self):
    #     input = " "
    #     expect = ' '
    #     self.assertTrue(TestChecker.test(input, expect, 283))
    #
    # def test_284(self):
    #     input = " "
    #     expect = ' '
    #     self.assertTrue(TestChecker.test(input, expect, 284))
    #
    # def test_285(self):
    #     input = " "
    #     expect = ' '
    #     self.assertTrue(TestChecker.test(input, expect, 285))
    #
    # def test_286(self):
    #     input = " "
    #     expect = ' '
    #     self.assertTrue(TestChecker.test(input, expect, 286))
    #
    # def test_287(self):
    #     input = " "
    #     expect = ' '
    #     self.assertTrue(TestChecker.test(input, expect, 287))
    #
    # def test_288(self):
    #     input = " "
    #     expect = ' '
    #     self.assertTrue(TestChecker.test(input, expect, 288))
    #
    # def test_289(self):
    #     input = " "
    #     expect = ' '
    #     self.assertTrue(TestChecker.test(input, expect, 289))
    #
    # def test_290(self):
    #     input = " "
    #     expect = ' '
    #     self.assertTrue(TestChecker.test(input, expect, 290))
    #
    # def test_291(self):
    #     input = " "
    #     expect = ' '
    #     self.assertTrue(TestChecker.test(input, expect, 291))
    #
    # def test_292(self):
    #     input = " "
    #     expect = ' '
    #     self.assertTrue(TestChecker.test(input, expect, 292))
    #
    # def test_293(self):
    #     input = " "
    #     expect = ' '
    #     self.assertTrue(TestChecker.test(input, expect, 293))
    #
    # def test_294(self):
    #     input = " "
    #     expect = ' '
    #     self.assertTrue(TestChecker.test(input, expect, 294))
    #
    # def test_295(self):
    #     input = " "
    #     expect = ' '
    #     self.assertTrue(TestChecker.test(input, expect, 295))
    #
    # def test_296(self):
    #     input = " "
    #     expect = ' '
    #     self.assertTrue(TestChecker.test(input, expect, 296))
    #
    # def test_297(self):
    #     input = " "
    #     expect = ' '
    #     self.assertTrue(TestChecker.test(input, expect, 297))
    #
    # def test_298(self):
    #     input = " "
    #     expect = ' '
    #     self.assertTrue(TestChecker.test(input, expect, 298))
    #
    # def test_299(self):
    #     input = " "
    #     expect = ' '
    #     self.assertTrue(TestChecker.test(input, expect, 299))
    #
    # def test_300(self):
    #     input = " "
    #     expect = ' '
    #     self.assertTrue(TestChecker.test(input, expect, 300))

    # def test_undeclared_function(self):
    #     """Simple program: main"""
    #     input = """Function: main
    #                Body:
    #                     foo();
    #                EndBody."""
    #     expect = str(Undeclared(Function(),"foo"))
    #     self.assertTrue(TestChecker.test(input,expect,400))
    #
    # def test_diff_numofparam_stmt(self):
    #     """Complex program"""
    #     input = """Function: main
    #                Body:
    #                     printStrLn();
    #                 EndBody."""
    #     expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
    #     self.assertTrue(TestChecker.test(input,expect,401))
    #
    # def test_diff_numofparam_expr(self):
    #     """More complex program"""
    #     input = """Function: main
    #                 Body:
    #                     printStrLn(read(4));
    #                 EndBody."""
    #     expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
    #     self.assertTrue(TestChecker.test(input,expect,402))
    #
    # def test_undeclared_function_use_ast(self):
    #     """Simple program: main """
    #     input = Program([FuncDecl(Id("main"),[],([],[
    #         CallExpr(Id("foo"),[])]))])
    #     expect = str(Undeclared(Function(),"foo"))
    #     self.assertTrue(TestChecker.test(input,expect,403))
    #
    # def test_diff_numofparam_expr_use_ast(self):
    #     """More complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],([],[
    #                 CallStmt(Id("printStrLn"),[
    #                     CallExpr(Id("read"),[IntLiteral(4)])
    #                     ])]))])
    #     expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
    #     self.assertTrue(TestChecker.test(input,expect,404))
    #
    # def test_diff_numofparam_stmt_use_ast(self):
    #     """Complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],([],[
    #                 CallStmt(Id("printStrLn"),[])]))])
    #     expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
    #     self.assertTrue(TestChecker.test(input,expect,405))
