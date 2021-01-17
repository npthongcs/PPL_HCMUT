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
        expect = str(Redeclared(Variable(),'a'))
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test_202(self):
        input = """
Var: a[10][10],b,c=1,d="hello world",b[10];
"""
        expect = str(Redeclared(Variable(),'b'))
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_203(self):
        input = """
Var: a,b[3]={1,2,3},e,f;
Var: g,read;
"""
        expect = str(Redeclared(Variable(),'read'))
        self.assertTrue(TestChecker.test(input, expect, 402))

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
        expect = str(Redeclared(Function(),'read'))
        self.assertTrue(TestChecker.test(input, expect, 403))

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
        expect = str(Redeclared(Function(),'foo'))
        self.assertTrue(TestChecker.test(input, expect, 404))

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
        expect = str(Redeclared(Function(),'foo'))
        self.assertTrue(TestChecker.test(input, expect, 405))

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
        expect = str(Redeclared(Variable(),'a'))
        self.assertTrue(TestChecker.test(input, expect, 406))

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
    Return;
EndBody.
"""
        expect = str(Redeclared(Parameter(),'a'))
        self.assertTrue(TestChecker.test(input, expect, 407))

    # test assignment statement

    def test_209(self):
        input = """
Var: a,b=10,c=1,d[3][3],e[2]={1.0,2.0};
Function: main
Parameter: a,c
Body:
    a = 1.2;
    a = b;
    Return;
EndBody.
"""
        expect = str(TypeMismatchInStatement(Assign(Id('a'),Id('b'))))
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_210(self):
        input = """
Var: a,b=10,c=1,d[3][3],e[2]={1.0,2.0},g="hello",f=False,u,v;
Function: main
Body:
    b = 1.2;
    Return;
EndBody.
"""
        expect = str(TypeMismatchInStatement(Assign(Id('b'),FloatLiteral(1.2))))
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_211(self):
        input = """
Var: a,b=10,c=1,d[3][3],e[2]={1.0,2.0},g="hello",f=False,u,v;
Function: main
Parameter: a,c
Body:
    Var: g,f;
    g = f + a + 100;
    c = f +. 10.0 -. 1.2e-10;
    Return;
EndBody.
"""
        expect = str(TypeMismatchInExpression(BinaryOp('+.',Id('f'),FloatLiteral(10.0))))
        self.assertTrue(TestChecker.test(input, expect, 410))

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
        expect = str(TypeMismatchInStatement(Assign(Id('b'),Id('d'))))
        self.assertTrue(TestChecker.test(input, expect, 411))

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
        expect = str(TypeMismatchInExpression(BinaryOp('+',Id('i'),Id('j'))))
        self.assertTrue(TestChecker.test(input, expect, 412))

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
        expect = str(TypeCannotBeInferred(Assign(Id('f'),CallExpr(Id('foo'),[IntLiteral(12)]))))
        self.assertTrue(TestChecker.test(input, expect, 413))

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
        expect = str(TypeMismatchInExpression(CallExpr(Id('foo'),[BooleanLiteral(False),BooleanLiteral(True),IntLiteral(1),FloatLiteral(1.2),Id('b')])))
        self.assertTrue(TestChecker.test(input, expect, 414))

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
        expect = str(Undeclared(Function(),'foo1'))
        self.assertTrue(TestChecker.test(input, expect, 415))

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
        expect = str(Undeclared(Identifier(),'k'))
        self.assertTrue(TestChecker.test(input, expect, 416))

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
        expect = str(TypeCannotBeInferred(Assign(Id('f'),CallExpr(Id('foo'),[CallExpr(Id('foo'),[CallExpr(Id('foo'),[])])]))))
        self.assertTrue(TestChecker.test(input, expect, 417))

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
        expect = str(TypeCannotBeInferred(Assign(Id('f'),CallExpr(Id('foo'),[CallExpr(Id('foo'),[CallExpr(Id('foo'),[IntLiteral(2)])])]))))
        self.assertTrue(TestChecker.test(input, expect, 418))

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
        expect = str(TypeCannotBeInferred(Assign(Id('f'),CallExpr(Id('foo'),[CallExpr(Id('foo'),[CallExpr(Id('foo'),[CallExpr(Id('foo1'),[])])])]))))
        self.assertTrue(TestChecker.test(input, expect, 419))

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
        expect = str(TypeCannotBeInferred(Assign(Id('f'),CallExpr(Id('foo'),[CallExpr(Id('foo'),[CallExpr(Id('foo'),[CallExpr(Id('foo1'),[])])])]))))
        self.assertTrue(TestChecker.test(input, expect, 420))

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
        expect = str(TypeCannotBeInferred(Assign(Id('u'),CallExpr(Id('foo'),[Id('f'),CallExpr(Id('foo'),[BooleanLiteral(True),BooleanLiteral(False)])]))))
        self.assertTrue(TestChecker.test(input, expect, 421))

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
        expect = str(Undeclared(Identifier(),'foo'))
        self.assertTrue(TestChecker.test(input, expect, 422))

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
        expect = str(Undeclared(Function(),'main'))
        self.assertTrue(TestChecker.test(input, expect, 423))

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
        expect = str(TypeMismatchInExpression(ArrayCell(Id('c'),[IntLiteral(10)])))
        self.assertTrue(TestChecker.test(input, expect, 424))

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
        expect = str(TypeMismatchInStatement(Assign(Id('u'),IntLiteral(1))))
        self.assertTrue(TestChecker.test(input, expect, 425))

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
        expect = str(TypeMismatchInExpression(CallExpr(Id('int_of_float'),[Id('f')])))
        self.assertTrue(TestChecker.test(input, expect, 426))

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
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id('d'),[IntLiteral(1),IntLiteral(2)]),Id('c'))))
        self.assertTrue(TestChecker.test(input, expect, 427))

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
        expect = str(TypeMismatchInExpression(BinaryOp('+',CallExpr(Id('foo'),[Id('a')]),CallExpr(Id('foo1'),[]))))
        self.assertTrue(TestChecker.test(input, expect, 428))

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
        expect = str(TypeMismatchInStatement(Assign(Id('f'),CallExpr(Id('foo1'),[]))))
        self.assertTrue(TestChecker.test(input, expect, 429))

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
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(CallExpr(Id('foo1'),[]),[IntLiteral(2)]),IntLiteral(1))))
        self.assertTrue(TestChecker.test(input, expect, 430))

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
        expect = str(TypeMismatchInExpression(ArrayCell(CallExpr(Id('foo1'),[]),[IntLiteral(2),IntLiteral(2)])))
        self.assertTrue(TestChecker.test(input, expect, 431))

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
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(CallExpr(Id('foo1'),[]),[IntLiteral(2)]),CallExpr(Id('foo1'),[]))))
        self.assertTrue(TestChecker.test(input, expect, 432))

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
        expect = str(TypeMismatchInExpression(CallExpr(Id('main'),[Id('f')])))
        self.assertTrue(TestChecker.test(input, expect, 433))

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
        expect = str(TypeCannotBeInferred(Assign(Id('c'),CallExpr(Id('foo1'),[CallExpr(Id('foo'),[CallExpr(Id('foo1'),[Id('b')])])]))))
        self.assertTrue(TestChecker.test(input, expect, 434))

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
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 435))

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
        expect = str(TypeMismatchInStatement(Assign(Id('b'),IntLiteral(1))))
        self.assertTrue(TestChecker.test(input, expect, 436))

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
        expect = str(TypeMismatchInStatement(CallStmt(Id('foo1'),[Id('c'),BooleanLiteral(False),ArrayCell(CallExpr(Id('foo2'),[]),[IntLiteral(2)]),CallExpr(Id('foo'),[CallExpr(Id('foo2'),[])]),ArrayCell(Id('f'),[IntLiteral(1),IntLiteral(2)])])))
        self.assertTrue(TestChecker.test(input, expect, 437))

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
        expect = str(TypeMismatchInExpression(ArrayCell(Id('f'),[IntLiteral(1),IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input, expect, 438))

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
        expect = str(TypeMismatchInStatement(Return(BinaryOp('+',ArrayCell(Id('e'),[IntLiteral(1),IntLiteral(2)]),ArrayCell(Id('b'),[IntLiteral(2)])))))
        self.assertTrue(TestChecker.test(input, expect, 439))

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
        expect = str(Undeclared(Function(),'printStr'))
        self.assertTrue(TestChecker.test(input, expect, 440))

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
    Return 0;
EndBody.
"""
        expect = str(Redeclared(Function(),'print'))
        self.assertTrue(TestChecker.test(input, expect, 441))

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
            print(string_of_int(i));
            printLn();
        ElseIf i<max-2 Then
        ElseIf i<max-2 Then
            max = max * 2;
            printStr("invalid i, please enter again");
        EndIf.
    Else Return "error, please check carefully again!";
    EndIf.
    Return ;
EndBody.
"""
        expect = str(Undeclared(Function(),'printStr'))
        self.assertTrue(TestChecker.test(input, expect, 442))

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
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_245(self):
        input = """
Function: main
        Parameter: global_var
        Body:
            global_var = 25+6-.2.5%3\\100 ;
        EndBody.
"""
        expect = str(TypeMismatchInExpression(BinaryOp('%',FloatLiteral(2.5),IntLiteral(3))))
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_246(self):
        input = """
Function: main
        Parameter: x, y
        Body:
        x = main(main(1));
        EndBody.
"""
        expect = str(TypeCannotBeInferred(Assign(Id('x'),CallExpr(Id('main'),[CallExpr(Id('main'),[IntLiteral(1)])]))))
        self.assertTrue(TestChecker.test(input, expect, 445))

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
        expect = str(TypeMismatchInExpression(CallExpr(Id('foo'),[FloatLiteral(0.0)])))
        self.assertTrue(TestChecker.test(input, expect, 446))

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
        expect = str(TypeMismatchInExpression(BinaryOp('||',Id('x'),BinaryOp('>',Id('x'),Id('y')))))
        self.assertTrue(TestChecker.test(input, expect, 447))

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
        expect = str(Undeclared(Identifier(),'move'))
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_250(self):
        input = """
Function: main
Parameter: x
Body:
    If main(main(main(1.2))) Then EndIf.
EndBody.
"""
        expect = str(TypeMismatchInExpression(CallExpr(Id('main'),[FloatLiteral(1.2)])))
        self.assertTrue(TestChecker.test(input, expect, 449))

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
        expect = str(TypeMismatchInExpression(CallExpr(Id('foo'),[FloatLiteral(1.2)])))
        self.assertTrue(TestChecker.test(input, expect, 450))

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
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 451))

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
        expect = str(TypeMismatchInStatement(Return(IntLiteral(2))))
        self.assertTrue(TestChecker.test(input, expect, 452))

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
        expect = str(TypeCannotBeInferred(Return(CallExpr(Id('foo'),[ArrayCell(CallExpr(Id('foo1'),[]),[IntLiteral(2)]),ArrayCell(Id('a'),[IntLiteral(3)]),BinaryOp('-',UnaryOp('-',IntLiteral(10)),IntLiteral(9))]))))
        self.assertTrue(TestChecker.test(input, expect, 453))

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
        expect = str(TypeMismatchInStatement(Assign(Id('c'),CallExpr(Id('main'),[]))))
        self.assertTrue(TestChecker.test(input, expect, 454))

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
        expect = str(TypeMismatchInStatement(Return(Id('b'))))
        self.assertTrue(TestChecker.test(input, expect, 455))

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
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 456))

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
        expect = str(TypeMismatchInExpression(CallExpr(Id('foo'),[Id('a')])))
        self.assertTrue(TestChecker.test(input, expect, 457))

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
        expect = str(TypeMismatchInExpression(BinaryOp('>',Id('d'),Id('test'))))
        self.assertTrue(TestChecker.test(input, expect, 458))

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
        expect = str(TypeMismatchInStatement(While(Id('test'),([],[CallStmt(Id('print'),[CallExpr(Id('string_of_bool'),[CallExpr(Id('main'),[])])])]))))
        self.assertTrue(TestChecker.test(input, expect, 459))

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
        expect = str(TypeMismatchInStatement(Return(StringLiteral('hello'))))
        self.assertTrue(TestChecker.test(input, expect, 460))

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
        expect = str(TypeMismatchInStatement(Return(StringLiteral('hello'))))
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_263(self):
        input = """
Function: main
Body:
Var: x, y, z;
x = True;
z = string_of_bool(y);
z = string_of_bool(!y && x);
z = string_of_bool();
EndBody.
"""
        expect = str(TypeMismatchInExpression(CallExpr(Id('string_of_bool'),[])))
        self.assertTrue(TestChecker.test(input, expect, 462))

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
        expect = str(TypeMismatchInStatement(While(Id('test'),([],[]))))
        self.assertTrue(TestChecker.test(input, expect, 463))

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
        expect = str(TypeMismatchInStatement(CallStmt(Id('read'),[IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input, expect, 464))

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
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id('b'),[IntLiteral(2),IntLiteral(2)]),FloatLiteral(3.4))))
        self.assertTrue(TestChecker.test(input, expect, 465))

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
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 466))

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
        expect = str(TypeMismatchInStatement(CallStmt(Id('foo'),[])))
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_269(self):
        input = """
Function: foo
Body:
Return;
EndBody.

Function: main
Body:
Var: i;
For (i = 0, True, foo()) Do
EndFor.
EndBody.
"""
        expect = str(TypeMismatchInStatement(For(Id('i'),IntLiteral(0),BooleanLiteral(True),CallExpr(Id('foo'),[]),([],[]))))
        self.assertTrue(TestChecker.test(input, expect, 468))

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
        expect = str(TypeMismatchInStatement(For(Id('i'),CallExpr(Id('foo'),[IntLiteral(0)]),BooleanLiteral(True),IntLiteral(1),([],[]))))
        self.assertTrue(TestChecker.test(input, expect, 469))

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
        expect = str(TypeMismatchInStatement(If([(CallExpr(Id('foo'), []), [], [
            CallStmt(Id('print'), [StringLiteral("Error VoidType!")])])], ([], []))))
        self.assertTrue(TestChecker.test(input, expect, 470))

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
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id('arr'),[Id('i')]),CallExpr(Id('foo'),[Id('i')]))))
        self.assertTrue(TestChecker.test(input, expect, 471))

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
        expect = str(TypeCannotBeInferred(Assign(ArrayCell(CallExpr(Id('foo'),[]),[IntLiteral(1),IntLiteral(2)]),IntLiteral(3))))
        self.assertTrue(TestChecker.test(input, expect, 472))

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
        expect = str(TypeMismatchInExpression(CallExpr(Id('foo1'),[Id('x')])))
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_275(self):
        input = """
Function: main
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
        expect = str(TypeMismatchInStatement(Return(CallExpr(Id('int_of_string'),[CallExpr(Id('read'),[])]))))
        self.assertTrue(TestChecker.test(input, expect, 474))

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
        expect = str(TypeMismatchInExpression(BinaryOp('>.',ArrayCell(CallExpr(Id('foo'),[]),[IntLiteral(0)]),Id('pi'))))
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test_277(self):
        input = """Function: foo
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
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(CallExpr(Id('foo'),[]),[Id('x')]),Id('i'))))
        self.assertTrue(TestChecker.test(input, expect, 476))

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
        expect = str(TypeMismatchInStatement(Return(Id('arr'))))
        self.assertTrue(TestChecker.test(input, expect, 477))

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
        expect = str(TypeMismatchInStatement(Return(Id('y'))))
        self.assertTrue(TestChecker.test(input, expect, 478))

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
        expect = str(TypeMismatchInStatement(Return(BinaryOp('*.',CallExpr(Id('float_to_int'),[Id('y')]),FloatLiteral(15.0)))))
        self.assertTrue(TestChecker.test(input, expect, 479))

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
        expect = str(TypeMismatchInStatement(Assign(Id('y'),CallExpr(Id('foo'),[Id('x')]))))
        self.assertTrue(TestChecker.test(input, expect, 480))

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
        expect = str(TypeMismatchInExpression(CallExpr(Id('foo'),[Id('x')])))
        self.assertTrue(TestChecker.test(input, expect, 481))

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
        expect = str(TypeMismatchInExpression(CallExpr(Id('double'),[Id('n')])))
        self.assertTrue(TestChecker.test(input, expect, 482))

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
        expect = str(TypeMismatchInExpression(BinaryOp('+.',FloatLiteral(1.0),ArrayCell(Id('x'),[ArrayCell(Id('x'),[IntLiteral(2)])]))))
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test_285(self):
        input = """
                    Function: main
					Body:
					Var: x[5], y[5];
					x = y;
					EndBody.
"""
        expect = str(TypeCannotBeInferred(Assign(Id('x'),Id('y'))))
        self.assertTrue(TestChecker.test(input, expect, 484))

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
        expect = str(TypeMismatchInStatement(CallStmt(Id('printLn'),[StringLiteral('Goodbye')])))
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test_287(self):
        input = """
                    Function: main
					Body:
					Var: x, y, z, t;
					x = int_of_string(read());
					y = 1.2 +. z +. float_to_int(z *. 1.5);
					EndBody.
"""
        expect = str(TypeMismatchInExpression(CallExpr(Id('float_to_int'),[BinaryOp('*.',Id('z'),FloatLiteral(1.5))])))
        self.assertTrue(TestChecker.test(input, expect, 486))

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
        expect = str(TypeMismatchInStatement(CallStmt(Id('bool_of_string'),[StringLiteral('1')])))
        self.assertTrue(TestChecker.test(input, expect, 487))

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
        expect = str(TypeMismatchInExpression(BinaryOp('*.',ArrayCell(Id('arr'),[BinaryOp('-',Id('size'),IntLiteral(1))]),FloatLiteral(1.5))))
        self.assertTrue(TestChecker.test(input, expect, 488))

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
        expect = str(TypeMismatchInExpression(BinaryOp('*.',ArrayCell(Id('arr'),[BinaryOp('-',Id('size'),IntLiteral(1))]),FloatLiteral(1.5))))
        self.assertTrue(TestChecker.test(input, expect, 489))

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
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id('arr'),[IntLiteral(1)]),ArrayCell(Id('idx'),[IntLiteral(3)]))))
        self.assertTrue(TestChecker.test(input, expect, 490))

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
        expect = str(TypeMismatchInStatement(Return(BinaryOp('\\.',CallExpr(Id('float_to_int'),[Id('x')]),CallExpr(Id('float_to_int'),[Id('y')])))))
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test_293(self):
        input = """
                    Var: x[5];
					Function: main
					Body:
					Var: y[5];
					y = x;
					EndBody.
"""
        expect = str(TypeCannotBeInferred(Assign(Id('y'),Id('x'))))
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test_294(self):
        input = """
                    Var: x[5] = {1,2,3,4,5};
					Function: main
					Body:
					Var: y[6];
					y = x;
					EndBody.
"""
        expect = str(TypeMismatchInStatement(Assign(Id('y'),Id('x'))))
        self.assertTrue(TestChecker.test(input, expect, 493))

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
        expect = str(TypeMismatchInExpression(BinaryOp('\\',Id('x'),FloatLiteral(5.0))))
        self.assertTrue(TestChecker.test(input, expect, 494))

    def test_296(self):
        input = """
                    Function: main
					Body:
					Var: arr[3][3] = {{1,2,3},{4,5,6},{7,8,9}};
					arr[2] = {1,4,7};
					EndBody.
"""
        expect = str(TypeMismatchInExpression(ArrayCell(Id('arr'),[IntLiteral(2)])))
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test_297(self):
        input = """
                    Function: main
					Body:
					Var: x,y,z,t;
					z = (x >. 1.0) && (y == 0);
					t = x +. y +. 1.0;
					EndBody.        
"""
        expect = str(TypeMismatchInExpression(BinaryOp('+.',Id('x'),Id('y'))))
        self.assertTrue(TestChecker.test(input, expect, 496))

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
        expect = str(TypeMismatchInExpression(BinaryOp('+',Id('x'),Id('y'))))
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test_299(self):
        input = """
Var:x;        
"""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test_300(self):
        input = """
                    Function: main
					Body:
					Var: arr[3][3] = {{1,2,3},{4,5,6},{7,8,9}};
					arr[2][0] = {1,4,7};
					EndBody.
"""
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id('arr'),[IntLiteral(2),IntLiteral(0)]),ArrayLiteral([IntLiteral(1),IntLiteral(4),IntLiteral(7)]))))
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_301(self):
        input = """
                       Function: main
            Body:
                Var: a;
                a = 1 + foo(3.5);
            EndBody.
            Function: foo
            Parameter: x
            Body:
                Return x + 5;
            EndBody.
    """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 500))
