import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):

    # test redeclared variable

    def test_201(self):
        input = """
Var: a,b,c,a;
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 201))

    def test_202(self):
        input = """
Var: a[10][10],b,c=1,d="hello world",b[10];
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 202))

    def test_203(self):
        input = """
Var: a,b[3]={1,2,3},e,f;
Var: g,read;
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 203))

    # test redeclared function

    def test_204(self):
        input = """
Function: main
Body:
EndBody.
Function: read
Body:
EndBody.
Function: foo
Body:
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 204))

    def test_205(self):
        input = """
Function: main
Body:
EndBody.
Function: foo
Body:
EndBody.
Function: foo
Body:
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 205))

    def test_206(self):
        input = """
Var: foo,a[10];
Function: main
Body:
EndBody.
Function: sum
Body:
EndBody.
Function: foo
Body:
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 206))

    # redeclared variable, parameter

    def test_207(self):
        input = """
Var: a,b=10,c=1;
Function: main
Parameter: a,b,c
Body:
    Var: a;
EndBody.
Function: foo
Parameter: a
Body:
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 207))

    def test_208(self):
        input = """
Var: a,b=10,c=1;
Function: main
Parameter: a,b,c,a
Body:
EndBody.
Function: foo
Parameter: a
Body:
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 208))

    # test assignment statement

    def test_209(self):
        input = """
Var: a,b=10,c=1,d[3][3],e[2]={1.0,2.0};
Function: main
Parameter: a,c
Body:
    a = 1.2;
    a = b;
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 209))

    def test_210(self):
        input = """
Var: a,b=10,c=1,d[3][3],e[2]={1.0,2.0},g="hello",f=False,u,v;
Function: main
Body:
    b = 1.2;
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 210))

    def test_211(self):
        input = """
Var: a,b=10,c=1,d[3][3],e[2]={1.0,2.0},g="hello",f=False,u,v;
Function: main
Parameter: a,c
Body:
    Var: g,f;
    g = f + a + 100;
    c = f +. 10.0 -. 1.2e-10;
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 211))

    def test_212(self):
        input = """
Var: a,b=10,c=1,d[3][3],e[2]={1.0,2.0},g="hello",f=False,u,v;
Function: main
Parameter: a
Body:
    Var: g,f;
    b = d;
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 212))

    def test_213(self):
        input = """
Var: a,b=10,c=1,d[3][3],e[2]={1.0,2.0},g="hello",f=False,u,v;
Function: main
Parameter: a,c,i,j,k,m,n
Body:
    c = 1.2;
    i = c;
    n = i + j;
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 213))

    def test_214(self):
        input = """
Var: a,b=10,c=1,d[3][3],e[2]={1.0,2.0},g="hello",f=False,u,v;
Function: main
Parameter: a,c
Body:
    Var: g,f;
    f = foo(12);
EndBody.

Function: foo
Parameter: a
Body:
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 214))
#
    def test_215(self):
        input = """
Var: a,b=10,c=1,d[3][3],e[2]={1.0,2.0},g,f=False,u,v;
Function: main
Parameter: a,c
Body:
    Var: g,f;
    f = foo(False,True,1,1.2,b) + 1;
EndBody.

Function: foo
Parameter: a,b,c,d
Body:
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 215))

    # test undeclared function / variable

    def test_216(self):
        input = """
Var: a,b=10,c=1,d[3][3],e[2]={1.0,2.0},g,f=False,u,v;
Function: main
Parameter: a,c
Body:
    Var: g,f;
    f = foo1(False,True,1,1.2) + 1;
EndBody.

Function: foo
Parameter: a,b,c,d
Body:
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 216))

    def test_217(self):
        input = """
Var: a,b=10,c=1,d[3][3],e[2]={1.0,2.0},g,f=False,u,v;
Function: main
Parameter: a,c
Body:
    Var: g,f;
    f = foo(False,True,k,b) + 1;
EndBody.

Function: foo
Parameter: a,b,c,d
Body:
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 217))

    # test call function

    def test_218(self):
        input = """
Var: a,b=10,c=1,d[3][3],e[2]={1.0,2.0},g,f=False,u,v;
Function: main
Parameter: a,c
Body:
    Var: g,f;
    f = foo(foo(foo()));
EndBody.

Function: foo
Parameter: a
Body:
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 218))

    def test_219(self):
        input = """
Var: a,b=10,c=1,d[3][3],e[2]={1.0,2.0},g,f=False,u,v;
Function: main
Parameter: a,c
Body:
    Var: g,f;
    f = foo(foo(foo(2)));
EndBody.

Function: foo
Parameter: a
Body:
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 219))

    def test_220(self):
        input = """
Var: a,b=10,c=1,d[3][3],e[2]={1.0,2.0},g,f=False,u,v;
Function: main
Parameter: a,c
Body:
    Var: g,f;
    f = foo(foo(foo(foo1())));
EndBody.

Function: foo
Parameter: a
Body:
EndBody.

Function: foo1
Body:
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 220))

    def test_221(self):
        input = """
Var: a,b=10,c=1,d[3][3],e[2]={1.0,2.0},g,f=False,u,v;
Function: main
Parameter: a,c
Body:
    Var: g,f;
    b = a + foo1();
    f = foo(foo(foo(foo1())));
EndBody.

Function: foo
Parameter: a
Body:
    a = 1.2;
EndBody.

Function: foo1
Body:
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 221))

    def test_222(self):
        input = """
Var: a,b=10,c=1,d[3][3],e[2]={1.0,2.0},g,f=False,u,v;
Function: main
Parameter: a,c
Body:
    Var: g,f;
    f = f % b;
    u = foo(f,foo(True,False));
EndBody.

Function: foo
Parameter: a,c
Body:
EndBody.

Function: foo1
Body:
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 222))

    def test_223(self):
        input = """
Var: a,b=10,c=1,d[3][3],e[2]={1.0,2.0},g,f=False,u,v;
Function: main
Parameter: a,c
Body:
    Var: g,f;
    f = foo;
EndBody.

Function: foo
Parameter: a
Body:
EndBody.

Function: foo1
Body:
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 223))

    def test_224(self):
        input = """
Var: a,b=10,c=1,d[3][3],e[2]={1.0,2.0},g,f=False,u,v;
Function: main
Parameter: a,c,main
Body:
    Var: g,f;
    f = main()+1;
EndBody.

Function: foo
Parameter: a
Body:
EndBody.

Function: foo1
Body:
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 224))

    def test_225(self):
        input = """
Var: a,b=10,c=1,d[3][3],e[2]={1.0,2.0},g,f=False,u,v;
Function: main
Parameter: a,c
Body:
    Var: g,f;
    b = c[10];
EndBody.

Function: foo
Parameter: a
Body:
EndBody.

Function: foo1
Body:
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 225))

    def test_226(self):
        input = """
Var: a,b=10,c=1,d[3][3],e[2]={1.0,2.0},g,f=False,u,v;
Function: main
Parameter: a,c
Body:
    Var: g,f;
    u =1.2;
EndBody.

Function: foo
Parameter: a
Body:
EndBody.

Function: foo1
Body:
    u = 1;
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 226))

    def test_227(self):
        input = """
Var: a,b=10,c=1,d[3][3],e[2]={1.0,2.0},g,f=False,u,v;
Function: main
Parameter: a,c
Body:
    Var: g,f;
    f = b + d[1][1];
    d[3][2] = int_of_float(f);
EndBody.

Function: foo
Parameter: a
Body:
EndBody.

Function: foo1
Body:
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 227))

    def test_228(self):
        input = """
Var: a,b=10,c=1.2,d[3][3],e[2]={1.0,2.0},g,f=False,u,v;
Function: main
Parameter: a,c
Body:
    d[3][2] = float_to_int(c);
    d[1][2] = c;
EndBody.

Function: foo
Parameter: a
Body:
EndBody.

Function: foo1
Body:
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 228))

    def test_229(self):
        input = """
Var: a,b=10,c=1.2,d[3][3],e[2]={1.0,2.0},g,f=False,u,v;
Function: foo1
Body:
    a = 1.2;
    Return int_of_float(a)>b;
EndBody.

Function: main
Parameter: a,c
Body:
    a = foo1() && False;
    a = foo(a) + foo1();
EndBody.

Function: foo
Parameter: a
Body:
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 229))

    def test_230(self):
        input = """
Var: a,b=10,c=1.2,d[3][3],e[2]={1.0,2.0},g,f=False,u,v;
Function: foo1
Body:
    a = 12;
    Return a;
EndBody.

Function: main
Parameter: c
Body:
    c = foo(e[1]) + 1;
EndBody.

Function: foo
Parameter: f
Body:
    f = foo1();
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 230))

    def test_231(self):
        input = """
Var: a,b=10,c=1.2,d[3][3],e[2]={1.0,2.0},g,f=False,u,v;
Function: foo1
Body:
    Return e;
EndBody.

Function: main
Parameter: c
Body:
    foo1()[2] = 1;
EndBody.

Function: foo
Parameter: i,j,k
Body:

EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 231))

    def test_232(self):
        input = """Var: a,b=10,c=1.2,d[3][3],e[2]={1.0,2.0},g,f=False,u,v;
Function: foo1
Body:
    Return e;
EndBody.

Function: main
Parameter: c
Body:
    foo1()[2][2] = 1.2;
EndBody.

Function: foo
Parameter: i,j,k
Body:

EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 232))

    def test_233(self):
        input = """
Var: a,b=10,c=1.2,d[3][3],e[2]={1.0,2.0},g,f=False,u,v;
Function: foo1
Body:
    Return e;
EndBody.

Function: main
Parameter: c
Body:
    foo1()[2] = foo1();
EndBody.

Function: foo
Parameter: i,j,k
Body:

EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 233))

    # if statement

    def test_234(self):
        input = """
Var: a,b=10,c=1.2,d[3][3],e[2]={1.0,2.0},g,f=False,u,v;
Function: foo1
Body:
    Return e;
EndBody.

Function: main
Parameter: c
Body:
    If b==2 Then
        main(main(f));
    EndIf.
EndBody.

Function: foo
Parameter: i,j,k
Body:

EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 234))

    def test_235(self):
        input = """
Var: a,b=10,c=1.2,d[3][3],e[2]={1.0,2.0},g,f=False,u,v;
Function: foo1
Parameter: i
Body:
    Return e;
EndBody.

Function: main
Parameter: c
Body:
    c = foo1(foo(foo1(b)));
    If c Then
    EndIf.
EndBody.

Function: foo
Parameter: i
Body:
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 235))

    def test_236(self):
        input = """
Var: a,b=10,c=1.2,d[3][3],e[2]={1.0,2.0},g,f=False,u,v;
Function: foo1
Parameter: i
Body:
    Return e;
EndBody.

Function: main
Parameter: c
Body:
    If True Then
        Var: c,a,b;
        c= 1.2;
    EndIf.
    c = 10;
EndBody.

Function: foo
Parameter: i
Body:

EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 236))

    def test_237(self):
        input = """
Var: a,b=10,c=1.2,d[3][3],e[2]={1.0,2.0},g,f=False,u,v;
Function: foo1
Parameter: i
Body:
    Return e;
EndBody.

Function: main
Parameter: c,b
Body:
    If True Then
        Var: c,a,b;
        c= 1.2;
        Return c;
    EndIf.
    Return b;
    b = 1;
EndBody.

Function: foo
Parameter: i
Body:

EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 237))

    def test_238(self):
        input = """
Var: a,b=10,c=1.2,d[3][3],e[2]={1.0,2.0},g,f=False,u,v;
Function: foo1
Parameter: i1,i2,i3,i4,i5
Body:
EndBody.

Function: foo2
Body:
    Var: a[2]={1.2,10.};
    Return a;
EndBody.

Function: main
Parameter: c,b
Body:
    If True Then
        Var: c=1,a=1.2,b=True,f[2][2]={{1,2},{1,2}};
        foo1(c,e[2],foo2()[2],foo(foo2()),f[1][2]);
        If a>.float_to_int(c) Then
            Var: c,a;
            foo1(c,False,foo2()[2],foo(foo2()),f[1][2]);
        EndIf.
        Return c;
    EndIf.
    Return b;
EndBody.

Function: foo
Parameter: i
Body:
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 238))

    def test_239(self):
        input = """
Var: a,b=10,c=1.2,d[3][3],e[2]={1.0,2.0},g,f=False,u,v;
Function: foo1
Parameter: i1,i2,i3,i4,i5
Body:
EndBody.

Function: foo2
Body:
    Var: a[2]={1.2,10.};
    Return a;
EndBody.

Function: main
Parameter: c,b
Body:
    If True Then
        Var: c=1,a=1.2,b=True,f[2][2]={{1,2},{1,2}};
        If a>.float_to_int(c) Then
            foo();
            Return a;
        EndIf.
        Return float_to_int(c);
    EndIf.
    Return float_to_int(f[1][1]);
EndBody.

Function: foo
Body:
    Return main(1,1);
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 239))

    def test_240(self):
        input = """
Var: a,b=1,d=1.2,e[2][2];
Function: main
Body:
    Var: b=1.2;
    If b>.d Then
        Return d;
    Else
        Var: b[2]={17,19};
        Return e[1][2] + b[2];
    EndIf.
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 240))

    def test_241(self):
        input = """
Var: n;
Function: main
Body:
    Var: m,a,c,b;
    n = read();
    a = bool_of_string(n);
    If a Then
        Var: max=0,i,j;
        j = read();
        i = int_of_string(j);
        If i>max Then
            i = i+1;
            printStr(string_of_int(i));
            printLn();
        Else
            printStrLn("invalid i, please enter again");
        EndIf.
    Else Return "error, please check carefully again!";
    EndIf.
    Return ;
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 241))

    def test_242(self):
        input = """
Function : print
Parameter : x
Body:
    Return;
EndBody.

Function: m
Body:
    Var : value = 12345;
    Return value;
EndBody.

Function: main
Parameter : x, y
Body:
    print(m);
    Return 0;
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 242))

    def test_243(self):
        input = """
Var: n;
Function: main
Body:
    Var: m,a,c,b;
    n = read();
    a = bool_of_string(n);
    If a Then
        Var: max=0,i,j;
        j = read();
        i = int_of_string(j);
        If i>max Then
            i = i+1;
            printStr(string_of_int(i));
            printLn();
        ElseIf i<max-2 Then
        ElseIf i<max-2 Then
            max = max * 2;
            printStrLn("invalid i, please enter again");
        EndIf.
    Else Return "error, please check carefully again!";
    EndIf.
    Return ;
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 243))

    def test_244(self):
        input = """
Function: main
Parameter: a,x
Body:
    x = x + foo(foo(x));
EndBody.

Function: foo
Parameter: x
Body:
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 244))

    def test_245(self):
        input = """
Function: main
        Parameter: global_var
        Body:
            global_var = 25+6-.2.5%3\\100 ;
        EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 245))

    def test_246(self):
        input = """
Function: main
        Parameter: x, y
        Body:
        x = main(main(1));
        EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 246))

    def test_247(self):
        input = """
Var: a[1] = {0};

Function: foo
    Parameter: x
    Body:
        Return a;
    EndBody.

Function: main
    Body:
        foo(0)[0] = foo(0.0)[0];
    EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 247))

    def test_248(self):
        input = """
Function: foo
        Parameter: x
        Body:
        x=1.1;
        Return { True };
        EndBody.

        Function: main
        Parameter: x, y
        Body:
        foo(x)[0] = x || (x>y);
        EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 248))

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
    If main(main(main(1.2))) Then EndIf.
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 250))

    def test_251(self):
        input = """
Var: x[5][10], y = False, z = True;
            Function: foo
                Parameter: t
                Body:
                    t = 1;
                    t= foo(foo(1.2));
                EndBody.

            Function: main
                Parameter: t
                Body:
                    t = 1;
                    t = foo(1);
                EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 251))

    def test_252(self):
        input = """
Var: x[5] = {1,2,3,4,5};
        Function: sum
            Parameter: x[5]
                Body:
                    Var: sum = 0, i;
                    For (i = 0 , i < 5, 1) Do
                        sum = sum + i;
                    EndFor.
                    Return sum;
                EndBody.
        Function: main
            Body:
                Var: y;
                y = sum(x);
                printStrLn(string_of_int(y));
                Return;
            EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 252))

    def test_253(self):
        input = """
Var: x, a,b ,c;
        Function: main
        Body:
        If main() Then
        EndIf.
        Return 2;
        EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 253))

    def test_254(self):
        input = """
Var: a[3]={1.2,1.3,1.4},b,c;
Function: foo1
Body:
    Return {1,2,3,4,5,6};
EndBody.

Function: main
Body:
    Return foo(foo1()[2],a[3],-10-9);
EndBody.

Function: foo
Parameter: a,b,c
Body:
    c = main();
    Return;
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 254))

    def test_255(self):
        input = """
Var: a[3]={1.2,1.3,1.4},b,c;
Function: foo1
Body:
    Return {1,2,3,4,5,6};
EndBody.

Function: main
Body:
    foo(foo1()[2],a[3],-10-9);
    Return ;
EndBody.

Function: foo
Parameter: a,b,c
Body:
    c = main();
    Return;
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 255))

    def test_256(self):
        input = """
Var: f[3][3]={{1,2,3},{4,5,6},{7,8,9}};
Function: main
Parameter: a,b,c
Body:
    For (a = 1, (a>10) && (a<20), a) Do
        b = a * a * a - a\\10 + f[2][1];
        print(string_of_int(b));
        If (b!=c) && (b>b%c) Then
            Var: a,c;
            a = read();
            c = float_of_string(a);
            Return c;
        ElseIf (b==c) && (b<c%b) Then
            Return b;
            Break;
        EndIf.
    EndFor.
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 256))

    def test_257(self):
        input = """
Function: foo
Parameter: x
Body:
    If x==0 Then
        Return 1;
    Else Return x * foo(x-1);
    EndIf.
EndBody.

Function: main
Body:
    Var: a,b;
    a= read();
    b= int_of_string(a);
    print(string_of_int(foo(b)));
    Return;
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 257))

    def test_258(self):
        input = """
Function: foo
Parameter: x
Body:
    If x==0 Then
        Return 1;
    Else Return x * foo(x-1);
    EndIf.
EndBody.

Function: main
Body:
    Var: a,b;
    a= read();
    print(string_of_int(foo(a)));
    Return;
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 258))

    def test_259(self):
        input = """
Var: a=10,b=1.2,c,d[2]={True,False};
Function: foo
Body:
    Return d;
EndBody.

Function: main
Body:
    Var: test;
    While test Do
        Var: d=1;
        print(string_of_bool(foo()[1]));
        For (d=1, d>test, d) Do
            print(string_of_int(d));
        EndFor.
    EndWhile.
    Return;
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 259))

    def test_260(self):
        input = """
Function: main
Body:
    Var: test=1;
    While test Do
        print(string_of_bool(main()));
    EndWhile.
    Return True;
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 260))

    def test_261(self):
        input = """
Function: main
Body:
    Var: test;
    While test Do
        print(string_of_bool(main()));
    EndWhile.
    Return "hello";
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 261))

    def test_262(self):
        input = """
Function: main
Body:
    Var: test;
    Do
        print(string_of_bool(main()));
    While test
    EndDo.
    Return "hello";
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 262))

    def test_263(self):
        input = """
Function: main
Body:
    Var: test;
    Do
        test = 1;
        print(string_of_bool(main()));
    While test
    EndDo.
    Return False;
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 263))

    def test_264(self):
        input = """
Function: main
Body:
    Var: test;
    While test Do
        Var: test;
        test = test + test;
        test = main() + main();
        While test Do
        EndWhile.
    EndWhile.
    Return 1;
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 264))

    def test_265(self):
        input = """
Function: main
Body:
    Var: test;
    While test Do
        Var: test;
        test = test + test;
        test = main() + main();
        read(4);
    EndWhile.
    Return 1;
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 265))

    def test_266(self):
        input = """
Function: main
Body:
    Var: a[5]={1,2,3,4,5},b[3][3];
    a[3 + foo(2)] = a[b[2][3]] + 4;
    b[2][2] = 3.4;
    Return ;
EndBody.

Function: foo
Parameter: a
Body:
    Return a*a;
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 266))

    def test_267(self):
        input = """
Function: foo1
Body:
    Return;
EndBody.

Function: main
Body:
    foo(foo1());
EndBody.

Function: foo
Parameter: x
Body:
    Return;
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 267))

    def test_268(self):
        input = """
Function: foo
    Body:
        Var: r = 10., v, a,b;
        b= float_to_int(a);
        v = (4. \\. 3.) *. 3.14 *. r *. r *. r;
        Return v;
    EndBody.

Function: main
Body:
    foo();
    Return ;
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 268))

    def test_269(self):
        input = """
Function: foo
Body:
    Return;
EndBody.
Function: main
Body:
    Var: i;
    For (i = 0, 1>2, foo()) Do
    EndFor.
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 269))

    def test_270(self):
        input = """
Function: foo
Parameter: x
Body:
    Return;
EndBody.

Function: main
Body:
    Var: i;
    For (i = foo(0), True, 1) Do
    EndFor.
EndBody."""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 270))

    def test_271(self):
        input = """
Function: foo
Body:
    Return;
EndBody.

Function: main
Body:
    If foo() Then
        print("Error VoidType!");
    EndIf.
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 271))

    def test_272(self):
        input = """
Function: foo
Parameter: x
Body:
    Return;
EndBody.

Function: main
Body:
    Var: arr[10];
    Var: i;
    For (i = 0, i < 10, 2) Do
        arr[i] = foo(i);
    EndFor.
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 272))

    def test_273(self):
        input = """
Function: main
Body:
    foo()[1][2] = 3;
EndBody.

Function: foo
Body:
    Return {{1,2,3},{4,5,6}};
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 273))

    def test_274(self):
        input = """
Function:main
Body:
    Var: x = 1;
    x = foo1({1,2,3});
    foo(foo1(foo2()));
EndBody.

Function: foo1
Parameter: x[3]
Body:
    Var: i,arr[3],max;
    max = -999;
    For (i = 0, i < 3, 1) Do
        arr[i] = x[i] * i;
        If max < arr[i] Then
            max = arr[i];
        EndIf.
    EndFor.
    Return max;
EndBody.

Function: foo2
Body:
    Var: arr[3];
    Var: i;
    For (i = 0, i < 3, 1) Do
        arr[i] = i*2;
    EndFor.
    Return arr;
EndBody.

Function: foo
Parameter: x
Body:
    While int_of_string(read()) > 5 Do
    EndWhile.
    Return;
    Return foo1(x);
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 274))

    def test_275(self):
        input = """
Function:main
Body:
    Var: x = 1;
    x = foo1({1,2,3});
    foo(foo1(foo2()));
EndBody.

Function: foo1
Parameter: x[3]
Body:
    Var: i,arr[3],max;
    max = -999;
    For (i = 0, i < 3, 1) Do
        arr[i] = x[i] * i;
        If max < arr[i] Then
            max = arr[i];
        EndIf.
    EndFor.
    Return max;
EndBody.

Function: foo2
Body:
    Return int_of_string(read());
EndBody.

Function: foo
Parameter: x
Body:
EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 275))

    def test_276(self):
        input = """
Function: foo
					Body:
						Var: arr[5];
						Return arr;
					EndBody.

					Function: main
					Body:
						Var: arr[5] = {0,0,0,0,0}, i, pi = 3.14;
						For (i = 0, i < 5, 1) Do
							foo()[i] = arr[i];
						EndFor.
						If foo()[0] >. pi Then
							Return pi;
						EndIf.
						Return foo()[0];
					EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 276))

    def test_277(self):
        input = """
Function: foo
					Body:
						Var: arr[5];
						Return arr;
					EndBody.

					Function: main
					Body:
						Var: i;
						For (i = 0, i < 5, 1) Do
							If foo()[i] Then
								Var: x;
								x = int_of_string(string_of_bool(foo()[i]));
								foo()[x] = i;
							EndIf.
						EndFor.
						Return 0;
					EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 277))

    def test_278(self):
        input = """
Function: main
					Body:
						Var: x;
						x = 1 - foo(foo(foo(foo(x))));
					EndBody.

					Function: foo
					Parameter: x
					Body:
						Var: arr[5];
						Var: i;
						For (i = 0, i < 5, 1) Do
							arr[i] = x * i;
						EndFor.
						Return arr;
					EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 278))

    def test_279(self):
        input = """
Function: main
					Body:
					Var: x, y;
					x = int_of_string(read());
					If (x > -3) && (x < 0) Then
						Var: y;
						y = x * (-30);
						Return y;
					ElseIf (x >= 0) && (x <= 3) Then
						Var: y;
						y = float_to_int(x) *. 3.0;
						Return y;
					Else
						Var: y;
						y = bool_of_string("True") && y;
					EndIf.
					Return y + 1;
					EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 279))

    def test_280(self):
        input = """
Function: main
					Body:
					Var: arr[8][8];
					Var: i;
					For (i = 0, i < 8, 1) Do
						Var: j;
						For (j = 0, j < 8, 1) Do
							If i == j Then
								arr[i][j] = i + j;
							Else
								arr[i][j] = foo(i, j);
							EndIf.
						EndFor.
					EndFor.
					EndBody.

					Function: foo
					Parameter: x, y
					Body:
						If x < y Then
							Return float_to_int(y) *. 15.0;
						EndIf.
						Return x;
					EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 280))

    def test_281(self):
        input = """
                    Function: main
					Body:
						Var: x;
						x = int_of_string(read());
						If x > 10 Then
							Var: y = 0;
							y = foo(x);
							If y > 10 Then
								Var: x;
								x = foo(y);
								If x > 10 Then
									Var: y;
									y = 1.5;
									y = foo(x);
								EndIf.
							EndIf.
						Else
							print(string_of_int(x));
						EndIf.
					EndBody.

					Function: foo
					Parameter: x
					Body:
					EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 281))

    def test_282(self):
        input = """
Function: main
					Body:
					Var: i, arr[10], newarr[10];
					For (i = 0, i < 10, 1) Do
						If arr[i] < 0 Then
							Var: x, j;
							x = arr[i];
							For (j = 0, j < 10, 1) Do
								newarr[j] = arr[i];
								newarr[j] = foo(x);
							EndFor.
							Return newarr;
						Else
							Var: x;
							print("Read number: x = ");
							x = read();
							Return notfoo(x);
						EndIf.
					EndFor.
					EndBody.

					Function: foo
					Parameter: x
					Body:
						Return x + 20;
					EndBody.

					Function: notfoo
					Parameter: x
					Body:
						Var: i, newarr[10];
						For (i = 0, i < 10, 1) Do
							newarr[10] = foo(x);
						EndFor.
						Return newarr;
					EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 282))

    def test_283(self):
        input = """
Function: double
					Parameter: x
					Body:
						Return 2.0 *. x;
					EndBody.

					Function: main
					Body:
						Var: n;
						n = int_of_string(read());
						print("n * 8 = ");
						printStrLn(string_of_float(double(double(double(n)))));
					EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 283))

    def test_284(self):
        input = """
Function: main
					Body:
					Var: x[5], y[5] = {1,2,3,4,5}, z;
					x = y;
					z = 1 + x[4];
					z = 1.0 +. x[x[2]];
					EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 284))

    def test_285(self):
        input = """
Function: main
					Body:
					Var: x[5], y[5];
					x = y;
					EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 285))

    def test_286(self):
        input = """
Function: main
					Body:
					Var: x, y, z;
					print("Read number n = ");
					x = read();
					printLn();
					y = int_of_string(x);
					z = y*y + 2*y + 1;
					print("(n + 1)^2 = ");
					print(string_of_int(z));
					printLn("Goodbye");
					EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 286))

    def test_287(self):
        input = """
Function: main
					Body:
					Var: x, y, z, t;
					x = int_of_string(read());
					y = 1.2 +. z +. float_to_int(z *. 1.5);
					EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 287))

    def test_288(self):
        input = """
Function: main
					Body:
					Var: x, y, z;
					If bool_of_string(x) && bool_of_string(y) Then
						z = bool_of_string("True");
						z = True && (!bool_of_string("False"));
						Return bool_of_string(x);
					EndIf.
						bool_of_string("1");
					EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 288))

    def test_289(self):
        input = """
Function: main
					Parameter: arr[5], size
					Body:
						arr = {0,1,2,3,4};
						Do
							print(string_of_int(arr[size - 1] + 2*arr[size - 1]));
							size = size - 1;
							arr[size - 1] = arr[size - 1] *. 1.5;
						While (size > 0) && (arr[size - 1] < 10)
						EndDo.
					EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 289))

    def test_290(self):
        input = """
Function: main
					Parameter: arr[5], size
					Body:
						arr = {0,1,2,3,4};
						While (size > 0) && (arr[size - 1] < 10) Do
							print(string_of_int(arr[size - 1] + 2*arr[size - 1]));
							size = size - 1;
							arr[size - 1] = arr[size - 1] *. 1.5;
						EndWhile.
					EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 290))

    def test_291(self):
        input = """
Function: main
					Parameter: arr[5]
					Body:
						Var: idx[5] = {0,1,2,3,4};
						Var: i = 0;
						For (i = idx[i], i < 5, idx[i + 1]) Do
							print(string_of_int(i*i*idx[i*i]));
						EndFor.
						arr[0] = 1.0;
						arr[1] = idx[3];
					EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 291))

    def test_292(self):
        input = """
Function: main
					Body:
					Var: x[3];
					If x[1] < x[2] Then
						x[2] = x[1];
						x[1] = 1;
					Else
						x[1] = x[2];
						x[2] = 0;
					EndIf.
					x[0] = foo(x[1], x[2]);
					EndBody.

					Function: foo
					Parameter: x, y
					Body:
						Return float_to_int(x) \. float_to_int(y);
					EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 292))

    def test_293(self):
        input = """
Var: x[5];
					Function: main
					Body:
					Var: y[5];
					y = x;
					EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 293))

    def test_294(self):
        input = """
Var: x[5] = {1,2,3,4,5};
					Function: main
					Body:
					Var: y[6];
					y = x;
					EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 294))

    def test_295(self):
        input = """
Function: main
					Body:
					Var: i, arr[5];
					For (i = 0, i < 5, 1) Do
						If foo(i) > 5 Then
							print(string_of_int(i));
						Else
							arr[foo(i)] = i;
						EndIf.
					EndFor.
					EndBody.

					Function: foo
					Parameter: x
					Body:
						x = x \\ 5.;
					EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 295))

    def test_296(self):
        input = """
Function: main
					Body:
					Var: arr[3][3] = {{1,2,3},{4,5,6},{7,8,9}};
					arr[2] = {1,4,7};
					EndBody.
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 296))

    def test_297(self):
        input = """
Function: main
					Body:
					Var: x,y,z,t;
					z = (x >. 1.0) && (y == 0);
					t = x +. y +. 1.0;
					EndBody.        
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 297))

    def test_298(self):
        input = """
Function: main
					Parameter: x, y
					Body:
					x = 1;
					x = foo(1, 2.0);
					EndBody.

					Function: foo
					Parameter: x, y
					Body:
					Var: z;
					z = x + y;
					EndBody.        
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 298))

    def test_299(self):
        input = """
Var:x;        
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 299))

    def test_300(self):
        input = """
Function: main
					Body:
					Var: arr[3][3] = {{1,2,3},{4,5,6},{7,8,9}};
					arr[2][0] = {1,4,7};
					EndBody.        
"""
        expect = ' '
        self.assertTrue(TestChecker.test(input, expect, 300))
