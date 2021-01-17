import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    
    def test_201(self):
        """ test declare variable """
        input = """Var: a; """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
        
    def test_202(self):
        """ test declare variable """
        input = """Var: a[10];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))
        
    def test_203(self):
        """ test declare variable """
        input = """Var: aa,c,b,d,w;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))
        
    def test_204(self):
        """ test declare variable """
        input = """Var: a,c[10],b,e,f[10][10][10];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))
        
    def test_205(self):
        """ test declare variable """
        input = """Var: a=4,c,d[10]={1,2,3,4};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))
        
    def test_206(self):
        """ test declare variable """
        input = """Var: a={1,2,3}, b="function", f=0x123, f[3]={"abc","def","xyz"};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))
        
    def test_207(self):
        """ test declare variable """
        input = """Var: a,b=7,c=0o346,d[0o12][0x10]={{1,2,3},{4,5,6}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))
        
    def test_208(self):
        """ test declare variable """
        input = """Var: a,b[10],c[10][10],d[10][10][10],f=12.0e-10,g=0,l="hello eveybody",m=0x12AF,n=0O123,q[3]={1,2,3},test=True,check=False;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))
        
    def test_209(self):
        """ test declare variable """
        input = """Var a,b,c,d;"""
        expect = "Error on line 1 col 4: a"
        self.assertTrue(TestParser.checkParser(input,expect,209))
        
    def test_210(self):
        """ test declare variable """
        input = """Var: a[10]={True,False,True}, check[23]={"abc",0x123,0X123,0o12,0O12,True,False,12.0e-100000,1000}; """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,210))
        
    def test_211(self):
        """ test declare variable """
        input = """Var: a,b[10],c[10][10],d[10][10][10],f=12.0e-10,g=0,l="hello eveybody",m=0x12AF,n=0O123,q[3]={1,2,3},test=True,check=False,;"""
        expect = "Error on line 1 col 123: ;"
        self.assertTrue(TestParser.checkParser(input,expect,211))
        
    def test_212(self):
        """ test declare variable """
        input = """Var: ;"""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input,expect,212))
        
    def test_213(self):
        """ test declare variable """
        input = """var: a;"""
        expect = "Error on line 1 col 0: var"
        self.assertTrue(TestParser.checkParser(input,expect,213))
        
    def test_214(self):
        """ test declare variable """
        input = """Var: a"""
        expect = "Error on line 1 col 6: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,214))
        
    def test_215(self):
        """ test declare variable """
        input = """Var: a[];"""
        expect = "Error on line 1 col 7: ]"
        self.assertTrue(TestParser.checkParser(input,expect,215))
        
    def test_216(self):
        """ test declare variable """
        input = """Var: a=y;"""
        expect = "Error on line 1 col 7: y"
        self.assertTrue(TestParser.checkParser(input,expect,216))
        
    def test_217(self):
        """ test declare variable """
        input = """
Var: a[10];
Var: a,b,c,d=6,f=10,g=0xABCD;
Var: a[10][11]={{1,2,3},{1,2,3}};
Var: a=100, c= 12.10e10;
Var: a[10][10][10][10][10][10][10][10][10][10][10][10];
Var: a=True, b=False, c="this is declare varibale";"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,217))
        
    def test_218(self):
        """ test declare variable """
        input = """Var: a[x];"""
        expect = "Error on line 1 col 7: x"
        self.assertTrue(TestParser.checkParser(input,expect,218))
        
    def test_219(self):
        """ test declare function """
        input = """
Function: foo
    Parameter: a,b,c[10],d[100][100]
    Body:
        Var: a[10];
        Var: a,b,c,d=6,f=10,g=0xABCD;
        Var: a[10][11]={{1,2,3},{1,2,3}};
        Var: a=100, c= 12.10e10;
        Var: a[10][10][10][10][10][10][10][10][10][10][10][10];
        Var: a=True, b=False, c="this is declare varibale";
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,219))
        
    def test_220(self):
        """ test declare function """
        input = """
Function: foo
    Parameter: a,b=5,c[10],d[10][10]
    Body:
    EndBody.
        """
        expect = "Error on line 3 col 18: ="
        self.assertTrue(TestParser.checkParser(input,expect,220))
        
    def test_221(self):
        """ test declare function """
        input = """
Function: foo
    Parameter: a,b,c[10],d[10][10]
    Body:
    EndBody
        """
        expect = "Error on line 6 col 8: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,221))
        
    def test_222(self):
        """ test declare function """
        input = """
Function: foo
    Parameter: 
    Body:
    EndBody.
        """
        expect = "Error on line 4 col 4: Body"
        self.assertTrue(TestParser.checkParser(input,expect,222))
        
    def test_223(self):
        """ test assignment statement """
        input = """
Function: foo
    Body:
        Var: a,c,s[10],v;
        v = (4. \\. 3.) *. 3.14 *. r *. r *. r;
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,223))
        
    def test_224(self):
        """ test assignment statement """
        input = """
Function: foo
    Body:
        a=!(a>1) || ((b-a)>(b+a));
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,224))
        
    def test_225(self):
        """ test assignment statement """
        input = """
Function: foo
    Body:
        Var: a,v,d[10][10];
        a=a+b+c+s+f+s-1-3-2\\4\\13*234322;
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,225))
        
    def test_226(self):
        """ test assignment statement """
        input = """
Function: foo
    Body:
        Var: a,c,s[10],v;
        v = 12. +. 10.1e-10 *. 10. \\. 0.01e19 -. 1000000.00001e-19999999;
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,226))
        
    def test_227(self):
        """ test assignment statement """
        input = """
Function: foo
    Body:
        a[3+foo(3)]=a%b-9;
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,227))
        
    def test_228(self):
        """ test assignment statement """
        input = """
Function: foo
    Body:
        Var: a,c,s[10],v;
        v = 12. +. 10.1e-10 *. 10. \\. 0.01e19 -. 1000000.00001e-19999999;
        check = !(a>.c) || (a<=.f) || (e =/= g) && (1>2) && (foo(2)>foo(3));
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,228))
        
    def test_229(self):
        """ test assignment statement """
        input = """
Function: foo
    Body:
        check = a+c-f\\2*foo(f) - a[foo(3)+f-foo(9)]-ab[func(a-b-b)];
        test = (check>=food) || (check != 0) || (d>=.f) || (w<=.s) || (a=/=v);
        a[3 + foo(2)] = a[b[2][3]] + 4;
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,229))
        
    def test_230(self):
        """ test assignment statement """
        input = """
Function: foo
    Body:
        Var: a,b,c;
        a = foo(x+y\\g*q) % foo(x-1);
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,230))
        
    def test_231(self):
        """ test assignment statement """
        input = """
Function: foo
Parameter: i
    Body:
        Return foo(i-1);
    EndBody.
        
Function: main
    Body:
        Var: a,b,c;
        a = foo(b) - c;
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,231))
        
    def test_232(self):
        """ test call function statement """
        input = """
Function: foo
Parameter: i
    Body:
        Return foo(i-1);
    EndBody.
        
Function: main
    Body:
        Var: a,b,c;
        foo(n-k%q);
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,232))
        
    def test_233(self):
        """ test ... """
        input = """
Function: foo
    Body:
        Var: r = 10., v;
        a = float_of_int(a);
        v = (4. \. 3.) *. 3.14 *. r *. r *. r;
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,233))
        
    def test_234(self):
        """ test if """
        input = """
Var: a,b,c=10,d[3]={1,2,3};
Function: foo
Parameter: i,j,m,n
    Body:
        i = 0;
        If n>1 Then 
            n = n-1;
            i = i+1;
            m = m+i;
        Else Return m;   
        EndIf. 
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,234))
        
    def test_235(self):
        """ test if """
        input = """
Var: a,b,c=10,d[3]={1,2,3};
Function: foo
Parameter: i,j,m,n
    Body:
        If n>1000 Then m = m*n;
        ElseIf (n>100) && (n<1000) Then m=m*m-n*2;
        ElseIf (n>10) && (n<100) Then m=m\\n+2;
        Else m=0;
        EndIf.
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,235))
        
    def test_236(self):
        """ test if """
        input = """
Var: a,b,c=10,d[3]={1,2,3};
Function: foo
Parameter: i,j,m,n
    Body:
        If n>1000 Then 
            If i>0 Then 
                If j<10 Then
                    a[i][j]=n*i*j;
        Else n=0;    
        EndIf.
        EndIf.
        EndIf.
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,236))
        
    def test_237(self):
        """ test if """
        input = """
Var: a,b,c=10,d[3]={1,2,3};
Function: foo
Parameter: i,j,m,n
    Body:
        If n>1000 Then 
            If i>0 Then 
                If j<10 Then
                    a[i][j]=n*i*j;
        Else n=0;    
        EndIf.
        EndIf.
    EndBody.
        """
        expect = "Error on line 13 col 4: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,237))
        
    def test_238(self):
        """ test if """
        input = """
Var: a,b,c=10,d[3]={1,2,3};
Function: foo
Parameter: i,j,m,n
    Body:
        i = 0;
        If n>1 Then 
            n = n-1;
            i = i+1;
            m = m+i;
        EndIf. 
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,238))
        
    def test_239(self):
        """ test if """
        input = """
Var: a,b,c=10,d[3]={1,2,3};
Function: foo
Parameter: i,j,m,n
    Body:
        i = 0;
        If n>1
            n = n-1;
            i = i+1;
            m = m+i;
        Else Return m;   
        EndIf. 
    EndBody.
        """
        expect = "Error on line 8 col 12: n"
        self.assertTrue(TestParser.checkParser(input,expect,239))
        
    def test_240(self):
        """ test if """
        input = """
Function: foo
    Parameter: i,j,m,n
    Body:
        If (foo(i-1)>=foo(i+1)) Then
            foo(n%i-a[foo(i\\4)]);
        Else Return 1;
        EndIf. 
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,240))
        
    def test_241(self):
        """ test for """
        input = """
Function: main
    Parameter: i,j,m,n
    Body:
        Var: i,j,k,m,n,a[10][10];
        For (i=0 , i<10, 1) Do
            n = n+1;
        EndFor.
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,241))
        
    def test_242(self):
        """ test for """
        input = """
Function: main
    Parameter: i,j,m,n,k
    Body:
        Var: i,j,k,m,n,a[10][10];
        For (i=n*m , (i<m) && (i>n) , k*k) Do
            n = n+1;
            k = k-2;
            m = m+k;
            n = n-k;
        EndFor.
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,242))
        
    def test_243(self):
        """ test for """
        input = """
Function: main
    Parameter: i,j,m,n,k
    Body:
        Var: i,j,k,m,n,a[10][10];
        For (i=n*m , (i<m) && (i>n) , k*k) Do
            If n % i == 0 Then  
                foo(i);
            Else foo(i+1);
            EndIf.
        If i!=0 Then Return i;
        Else Return 0;
        EndIf.
        EndFor.
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,243))
        
    def test_244(self):
        """ test for """
        input = """
Function: main
    Parameter: i,j,temp
    Body:
        Var: i,j,k,m,n,a[10][10];
        For (i=1,i<n,1) Do
            For (j=i+1,j<=n,1) Do
            If (a[i]>a[j]) Then
                temp = a[j];
                a[j]=a[i];
                a[i]=temp;
            EndIf.
        EndFor.
        EndFor.    
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,244))
        
    def test_245(self):
        """ test for """
        input = """
Function: main
    Parameter: i,j,temp
    Body:
        Var: i,j,k,m,n,a[10][10];
        For (i=1,i<n,1)
            For (j=i+1,j<=n,1) Do
            If (a[i]>a[j]) Then
                temp = a[j];
                a[j]=a[i];
                a[i]=temp;
            EndIf.
        EndFor.
        EndFor.    
    EndBody.
        """
        expect = "Error on line 7 col 12: For"
        self.assertTrue(TestParser.checkParser(input,expect,245))
        
    def test_246(self):
        """ test for """
        input = """
Function: main
    Parameter: i,j,temp
    Body:
        Var: i,j,k,m,n,a[10][10];
        For (i=1,i<n,) Do
            For (j=i+1,j<=n,1) Do
            If (a[i]>a[j]) Then
                temp = a[j];
                a[j]=a[i];
                a[i]=temp;
            EndIf.
        EndFor.
        EndFor.    
    EndBody.
        """
        expect = "Error on line 6 col 21: )"
        self.assertTrue(TestParser.checkParser(input,expect,246))
        
    def test_247(self):
        """ test for """
        input = """
Function: main
    Parameter: i,j,temp
    Body:
        Var: i,j,k,m,n,a[10][10];
        For (i=1,i<n,10) Do
            print(i);
        EndFor.    
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,247))
        
    def test_248(self):
        """ test for """
        input = """
Function: foo
Parameter:i
    Body:
        Return n * foo(n-1);
    EndBody.
        
Function: main
    Parameter: i,j,temp
    Body:
        Var: i,j,k,m,n,a[10][10];
        For (i=1,i<n,2) Do
            For (j=foo(3),j<=n,1) Do
            If (a[i]>a[j]) Then
                temp = a[j];
                a[j]=a[i];
                a[i]=temp;
            EndIf.
        EndFor.
        EndFor.
        For (i=0,i<n,1) Do
            writeln(a[i]);
            foo(a[i]);
        EndFor.    
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,248))
        
    def test_249(self):
        """ test while """
        input = """
Function: main
    Body:
          While n<10 Do 
            write(n);
            n = n-1;
        EndWhile.
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,249))
        
    def test_250(self):
        """ test while """
        input = """
Function: main
    Body:
          While (n<10) && (m>0) && (check!=False) Do 
            write(n);
            m = 1.2 +. n \\. i *. a[b[1][3]];
            If m*n!=0 Then
                m =n+m;
                n = random(m,n);
            Else m = k; n= p;
            EndIf.
            n = n-1;
        EndWhile.
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,250))
        
    def test_251(self):
        """ test while """
        input = """
Function: main
    Body:
          While (n<10) && (m>0) && (check!=False) Do 
            write(n);
            m = 1.2 +. n \\. i *. a[b[1][3]];
            If m*n!=0 Then
                While (m>10000) && (m<=foo(z)) Do
                m =n+m;
                m=swap(m,a[m]);
                recursive(a[m]-foo(3));
                EndWhile.
                n = random(m,n);
            Else m = k; n= p;
            EndIf.
            n = n-1;
        EndWhile.
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,251))
        
    def test_252(self):
        """ test while """
        input = """
Function: main
    Body:
          While (n<10) && (m>0) && (check!=False) Do 
            write(n);
            m = 1.2 +. n \\. i *. a[b[1][3]];
            If m*n!=0 Then
                While (m>10000) && (m<=foo(z))
                m =n+m;
                m=swap(m,a[m]);
                recursive(a[m]-foo(3));
                EndWhile.
                n = random(m,n);
            Else m = k; n= p;
            EndIf.
            n = n-1;
        EndWhile.
    EndBody.
        """
        expect = "Error on line 9 col 16: m"
        self.assertTrue(TestParser.checkParser(input,expect,252))
        
    def test_253(self):
        """ test while """
        input = """
Function: main
    Body:
        ** test simple while**
          While 1 Do 
            **Nothing ke ke ke ke ke**
        EndWhile.
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,253))
        
    def test_254(self):
        """ test while """
        input = """
Function: main
    Body:
        While (n>1) Do
            While (m>1) Do
                While (k<foo(a[n][b])) Do
                    While (f!= 11-k) Do
                        ** Nothing **
        EndWhile.
        EndWhile.
        EndWhile.
        EndWhile.
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,254))
        
    def test_255(self):
        """ test while """
        input = """
Function: main
    Body:
        While (n>1) Do
            While (m>1) Do
                While (k<foo(a[n][b])) Do
                    While (f!= 11-k) Do
                        ** Nothing **
        EndWhile.
        EndWhile.
        EndWhile.
    EndBody.
        """
        expect = "Error on line 12 col 4: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,255))
        
    def test_256(self):
        """ test while """
        input = """
Function: main
    Body:
        While (n>1) Do
            While (m>1) do
                While (k<foo(a[n][b])) Do
                    While (f!= 11-k) Do
                        ** Nothing **
        EndWhile.
        EndWhile.
        EndWhile.
        EndWhile.
    EndBody.
        """
        expect = "Error on line 5 col 24: do"
        self.assertTrue(TestParser.checkParser(input,expect,256))
        
    def test_257(self):
        """ test while """
        input = """
Function: main
    Body:
          While  Do 
        EndWhile.
    EndBody.
        """
        expect = "Error on line 4 col 17: Do"
        self.assertTrue(TestParser.checkParser(input,expect,257))
        
    def test_258(self):
        """ test if """
        input = """
Var: a,b,c=10,d[3]={1,2,3};
Function: foo
Parameter: i,j,m,n
    Body:
        If n>1000 Then m = m*n;
        ElseIf (n>100) && (n<1000) Then m=m*m-n*2;
        ElseIf (n>10) && (n<100) Then m=m\\n+2;
        Else m=0;
        Else n=0;
        EndIf.
    EndBody.
        """
        expect = "Error on line 10 col 8: Else"
        self.assertTrue(TestParser.checkParser(input,expect,258))
        
    def test_259(self):
        """ test do while """
        input = """
Function: foo
Parameter: i,j,m,n
    Body:
        Do a=i+1;
        While a<10 EndDo.
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,259))
        
    def test_260(self):
        """ test do while """
        input = """
Function: foo
Parameter: i,j,m,n
    Body:
        Do 
            Var: a,v,e;
            For (i=0,i<m+n,k) Do
                write(i);
            EndFor.
            a=a[foo(i)-f] +. 2. -. 2.109e-109;
            check= !(a==b) || (a<=.m+j-f) && (e=/=i);
        While a<10 EndDo.
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,260))
        
    def test_261(self):
        """ test do while """
        input = """
Function: foo
    Body:
        Do 
            While a!=b Do
                a=foo(j);
                b=arr[a];
                b=recursive(b-foo[a[b]]);
            EndWhile.
        While (a>b) && (b<foo[j]) && True EndDo.
        Return foo(-b);
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,261))
        
    def test_262(self):
        """ test do while """
        input = """
Function: foo
    Body:
        Do 
           If foo(g)-foo(j)>0 Then 
            Var: i,k,m;
            k=foo(g)*foo(j);
            i=k%m;
            m=foo(a[i]);
           EndIf. 
        While (a>b) && (b<foo[j]) EndDo.
        Return foo(-b)-foo(i)-foo(h);
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,262))
        
    def test_263(self):
        """ test do while """
        input = """
Function: foo
    Body:
        Do 
           If foo(g)-foo(j)>0 Then 
            Var: i,k,m;
            k=foo(g)*foo(j);
            i=k%m;
            m=foo(a[i]);
           EndIf. 
        While (a>b) && (b<foo[j]) EndDo.
        Return foo(-b)-foo(i)-foo(h);
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,263))
        
    def test_264(self):
        """ test do while """
        input = """
Function: foo
    Body:
        Do 
        While (a>b) && (b<foo[j]) EndDo.
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,264))
        
    def test_265(self):
        """ test do while """
        input = """
Function: foo
    Body:
        Do 
        While EndDo.
    EndBody.
        """
        expect = "Error on line 5 col 14: EndDo"
        self.assertTrue(TestParser.checkParser(input,expect,265))
        
    def test_266(self):
        """ test do while """
        input = """
Function: foo
    Body:
        Do 
            a= a[foo-a[a[i]]];
            Var: a,c,d;
        While True EndDo.
    EndBody.
        """
        expect = "Error on line 6 col 12: Var"
        self.assertTrue(TestParser.checkParser(input,expect,266))
        
    def test_267(self):
        """ test while """
        input = """
Function: foo
    Body:
        While True Do
            a= a[foo-a[a[i]]];
            Var: a,c,d;
        EndWhile.
    EndBody.
        """
        expect = "Error on line 6 col 12: Var"
        self.assertTrue(TestParser.checkParser(input,expect,267))
        
    def test_268(self):
        """ test for """
        input = """
Function: foo
    Body:
        For (i=0,i<10,1) Do
            a= a[foo-a[a[i]]];
            Var: a,c,d;
        EndFor.
    EndBody.
        """
        expect = "Error on line 6 col 12: Var"
        self.assertTrue(TestParser.checkParser(input,expect,268))
        
    def test_269(self):
        """ test do while """
        input = """
Function: foo
    Body:
        Do 
            Do
                Do
                    Do
                    While True EndDo.
                While False EndDo.
            While False EndDo.
        While False EndDo.        
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,269))
        
    def test_270(self):
        """ test declare """
        input = """
Var: a,b,c=10,d[f]={1,2,3};
Function: foo
Parameter: i,j,m,n
    Body:
        If n>1000 Then m = m*n;
        ElseIf (n>100) && (n<1000) Then m=m*m-n*2;
        ElseIf (n>10) && (n<100) Then m=m\\n+2;
        Else m=0;
        EndIf.
    EndBody.
        """
        expect = "Error on line 2 col 16: f"
        self.assertTrue(TestParser.checkParser(input,expect,270))
        
    def test_271(self):
        """ test declare """
        input = """
Var: a,b,c=10,d[-12.0]={1,2,3};
Function: foo
Parameter: i,j,m,n
    Body:
        If n>1000 Then m = m*n;
        ElseIf (n>100) && (n<1000) Then m=m*m-n*2;
        ElseIf (n>10) && (n<100) Then m=m\\n+2;
        Else m=0;
        EndIf.
    EndBody.
        """
        expect = "Error on line 2 col 16: -"
        self.assertTrue(TestParser.checkParser(input,expect,271))
        
    def test_272(self):
        """ test while """
        input = """
Function: main
    Body:
          While (n<10) && (m>0) && (check!=False) Do 
            write(n);
            m = 1.2 +. n \\. i *. a[b[1][3]];
            If m*n!=0 Then
                While (m>10000) && (m<=foo(z)) Do
                m =n+m;
                m=swap(m,a[m]);
                recursive(a[m]++foo(3));
                EndWhile.
                n = random(m,n);
            Else m = k; n= p;
            EndIf.
            n = n-1;
        EndWhile.
    EndBody.
        """
        expect = "Error on line 11 col 31: +"
        self.assertTrue(TestParser.checkParser(input,expect,272))
        
    def test_273(self):
        """ test while """
        input = """
Var: a,b=9,c[10]={1,2,3};
Function: foo
Parameter: i,j,a,b
    Body:
        While True Do
            Var: a,c,d;
            a= a[foo-a[a[i]+foo(check[a[b[j]]])]];
        EndWhile.
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,273))
        
    def test_274(self):
        """ test break do while """
        input = """
Function: foo
    Body:
        Do Break;
        While (a>b) && (b<foo[j]) EndDo.
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,274))
        
    def test_275(self):
        """ test break for """
        input = """
Function: main
    Parameter: i,j,temp
    Body:
        Var: i,j,k,m,n,a[10][10];
        For (i=1,i<n,1) Do
            For (j=i+1,j<=n,1) Do
            If (a[i]>a[j]) Then
                temp = a[j];
                a[j]=a[i];
                Break;
                a[i]=temp;
            EndIf.
        EndFor.
            Break;
        EndFor.    
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,275))
        
    def test_276(self):
        """ test break while """
        input = """
Function: main
    Body:
          While (n<10) && (m>0) && (check!=False) Do 
            write(n);
            m = 1.2 +. n \\. i *. a[b[1][3]];
            If m*n!=0 Then
                m =n+m;
                n = random(m,n);
            Else m = k; n= p;
            EndIf.
            Break;
            n = n-1;
        EndWhile.
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,276))
        
    def test_277(self):
        """ test break do while """
        input = """
Function: foo
    Body:
        Do Break;
            Do Break;
                Do Break;
                    Do Break;
                    While True EndDo.
                While False EndDo.
            While False EndDo.
        While False EndDo.        
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,277))
        
    def test_278(self):
        """ test continue do while """
        input = """
Function: foo
    Body:
        Do Continue;
        While (a>b) && (b<foo[j]) EndDo.
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,278))
        
    def test_279(self):
        """ test continue for """
        input = """
Function: main
    Parameter: i,j,temp
    Body:
        Var: i,j,k,m,n,a[10][10];
        For (i=1,i<n,1) Do
            For (j=i+1,j<=n,1) Do
            If (a[i]>a[j]) Then
                temp = a[j];
                a[j]=a[i];
                Break;
                a[i]=temp;
            EndIf.
        EndFor.
            Continue;
        EndFor.    
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,279))
        
    def test_280(self):
        """ test continue while """
        input = """
Function: main
    Body:
          While (n<10) && (m>0) && (check!=False) Do 
            write(n);
            m = 1.2 +. n \\. i *. a[b[1][3]];
            If m*n!=0 Then
                m =n+m;
                n = random(m,n);
            Else m = k; n= p;
            EndIf.
            Continue;
            n = n-1;
        EndWhile.
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,280))
        
    def test_281(self):
        """ test break do while """
        input = """
Function: foo
    Body:
        Do Break;
            Do Continue;
                Do Break;
                    Do Break;
                    While True EndDo.
                While False EndDo.
            While False EndDo.
        While False EndDo.        
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,281))
        
    def test_282(self):
        """ test call function """
        input = """
Function: foo
    Body:
        foo (2 + x, 4. \. y);
        goo ();
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,282))
        
    def test_283(self):
        """ test call function """
        input = """
Function: foo
    Body:
        foo (2 + x, 4. \. y);
        goo (foo (2 + x, 4. \. y));
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,283))
        
    def test_284(self):
        """ test call function """
        input = """
Function: foo
    Body:
        foo (2 + x, 4. \. y);
        goo (foo (2 + x, 4. \. y));
        func(func()-.goo (foo (2 + x, 4. \. y)) % foo(foo(f-g+.4.),func()-.goo (foo (2 + x, 4. \. y))));
        recursive(1.2 +. n \\. i *. a[b[1][3]],func(func()-.goo (foo (2 + x, 4. \. y)) % foo(foo(f-g+.4.),func()-.goo (foo (2 + x, 4. \. y)))),a[foo(i)-f] +. 2. -. 2.109e-109
        \\.foo(n%i-a[foo(i\\4)]));
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,284))
        
    def test_285(self):
        """ test call function"""
        input = """
Function: main
    Body:
          While (n<10) && (m>0) && (check!=False) Do 
            write(n);
            m = 1.2 +. n \\. i *. a[b[1][3]];
            If m*n!=0 Then
                While (m>10000) && (m<=foo(z)) Do
                m =n+m;
                m=swap(m,a[m]);
                foo (2 + x, 4. \. y);
                goo (foo (2 + x, 4. \. y));
                func(func()-.goo (foo (2 + x, 4. \. y)) % foo(foo(f-g+.4.),func()-.goo (foo (2 + x, 4. \. y))));
                recursive(1.2 +. n \\. i *. a[b[1][3]],func(func()-.goo (foo (2 + x, 4. \. y)) % foo(foo(f-g+.4.),func()-.goo (foo (2 + x, 4. \. y)))),a[foo(i)-f] +. 2. -. 2.109e-109
                    \\.foo(n%i-a[foo(i\\4)]));
                recursive(a[m]-foo(3));
                EndWhile.
                n = random(m,n);
            Else m = k; n= p;
            EndIf.
            n = n-1;
        EndWhile.
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,285))
        
    def test_286(self):
        """ test call function """
        input = """
Function: fOO_123
Parameter:i
    Body:
        Return n * foo(n-1);
    EndBody.
        
Function: main
    Parameter: i,j,temp
    Body:
        Var: i,j,k,m,n,a[10][10];
        For (i=1,i<n,2) Do
            recursive(1.2);
            For (j=foo(3),j<=n,1) Do
            If (a[i]>a[j]) Then
                temp = a[j];
                a[j]=a[i];
                a[i]=temp;
            EndIf.
        EndFor.
        EndFor.
        For (i=0,i<n,1) Do
            writeln(a[i]);
            foo(a[i]);
        EndFor.    
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,286))
        
    def test_287(self):
        """ test call function """
        input = """
Function: foo
    Body:
        Return foo (2 + x, 4. \. y);
        Return goo (foo (2 + x, 4. \. y));
        Return func(func()-.goo (foo (2 + x, 4. \. y)) % foo(foo(f-g+.4.),func()-.goo (foo (2 + x, 4. \. y))));
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,287))
        
    def test_288(self):
        """ test call function """
        input = """
Function: foo
    Body:
        Return foo (2 + x, 4. \. y);
        Return goo (foo (2 + x, 4. \. y));
        return func(func()-.goo (foo (2 + x, 4. \. y)) % foo(foo(f-g+.4.),func()-.goo (foo (2 + x, 4. \. y))));
    EndBody.
        """
        expect = "Error on line 6 col 15: func"
        self.assertTrue(TestParser.checkParser(input,expect,288))
        
    def test_289(self):
        """ test break do while """
        input = """
Function: foo
    Body:
        Do Break;
            Do Continue;
                Do break;
                    Do Break;
                    While True EndDo.
                While False EndDo.
            While False EndDo.
        While False EndDo.        
    EndBody.
        """
        expect = "Error on line 6 col 24: ;"
        self.assertTrue(TestParser.checkParser(input,expect,289))
        
    def test_290(self):
        """ test call function"""
        input = """
Function: main
    Body:
          While (n<10) && (m>0) && (check!=False) Do 
            write(n);
            m = 1.2 +. n \\. i *. a[b[1][3]];
            If m*n!=0 Then
                While (m>10000) && (m<=foo(z)) Do
                m =n+m;
                m=swap(m,a[m]);
                foo (2 + x, 4. \. y);
                goo (foo (2 + x, 4. \. y,));
                func(func()-.goo (foo (2 + x, 4. \. y)) % foo(foo(f-g+.4.),func()-.goo (foo (2 + x, 4. \. y))));
                 recursive(1.2 +. n \\. i *. a[b[1][3]],func(func()-.goo (foo (2 + x, 4. \. y)) % foo(foo(f-g+.4.),func()-.goo (foo (2 + x, 4. \. y)))),a[foo(i)-f] +. 2. -. 2.109e-109
                    \\.foo(n%i-a[foo(i\\4)]));
                recursive(a[m]-foo(3));
                EndWhile.
                n = random(m,n);
            Else m = k; n= p;
            EndIf.
            n = n-1;
        EndWhile.
    EndBody.
        """
        expect = "Error on line 12 col 41: )"
        self.assertTrue(TestParser.checkParser(input,expect,290))
        
    def test_291(self):
        """ test ..."""
        input = """
Var: a,b,c=10,d=12.e-10,f[10][10]={1,2,3,4},g[0x10][0o10]={{1,2,3},{0x12,0XABC,0X12AF},{0o12,0O7,0o1}};

Function: foo1
Parameter: i,j
    Body: 
        Var: m=0,n=0x12;
        While (True) || (i>=1) && (j<=m*n) Do
            If (i*j =/= m*n%i*j) Then
                i = foo2(foo1(1)\\.foo3(a[i]-foo4()));
                Break;
            Else Continue; 
            EndIf.       
        EndWhile.
    EndBody.
    
Function: foo2
Parameter: i,j,k,m,n,check
    Body: 
        Var: a={1,2,3}, b="function", f=0x123, f[3]={"abc","def","xyz"};
        
    EndBody.
    
Function: foo3
    Body: 
        Var: check = True;
        For (i=foo1(-foo(2)),i!=foo6(-foo7(7)+foo4(4)),foo5(foo1 (2 + x, 4. \. y))) Do
            While (check!=False) && (i*-foo1(a[i])) Do
                If (!check) Then Break; EndIf.            
            EndWhile.
            a[i][j]=1.0e10 +. -19.e-10 \\. -foo1(-foo2(-foo3(-foo4(-foo5(-foo6))))) -. foo7(foo7()-.foo2 (foo2 (2 + x, 4. \. y)) % foo5(foo4(f-g+.4.),func()-.goo (foo (2 + x, 4. \. y))));
            string = "Assignment PPL is very difficult";
            recursive(1.2 +. n \\. i *. a[b[1][3]],func(func()-.goo (foo (2 + x, 4. \. y)) % foo(foo(f-g+.4.),func()-.goo (foo (2 + x, 4. \. y)))),a[foo(i)-f] +. 2. -. 2.109e-109
                    \\.foo(n%i-a[foo(i\\4)]));
            check = (test && True) || (!boolean) && (a<=.b+.1.);
        EndFor.
    EndBody.
    
Function: foo4
Parameter: array[10][10][10][10][10][10][10][10][10][10][10][10]
    Body: 
        If i>=0 Then Break;
        Else Return foo4(i) * foo4(i+1);
        EndIf.
    EndBody.
    
Function: foo5
    Body: 
        Var: i,j,k,m,n,a[10][10];
        For (i=1,i<n,2) Do
            foo1(foo2(foo3(foo4(foo5(foo6(foo7))))));
            For (j=foo(3),j<=n,1) Do
            If (a[i]>a[j]) Then
                temp = a[j];
                a[j]=a[i];
                a[i]=temp;
            EndIf.
        EndFor.
        EndFor.
        For (i=0,i<n,1) Do
            writeln(a[i]);
            foo(a[i]);
        EndFor.  
    EndBody.
    
Function: foo6
    Body: 
        Var: i,j,k,m,n,a[10][10];
        For (i=1,i<n,1) Do
            For (j=i+1,j<=n,1) Do
            If (a[i]>a[j]) Then
                temp = a[j];
                a[j]=a[i];
                Break;
                a[i]=temp;
            EndIf.
        EndFor.
            Break;
        EndFor. 
    EndBody.
    
Function: foo7
    Body: 
        Do 
           If foo(g)-foo(j)>0 Then 
            Var: i,k,m;
            k=foo(g)*foo(j);
            i=k%m;
            m=foo(a[i]);
           EndIf. 
        While (a>b) && (b<foo[j]) EndDo.
        Return foo(-b)-foo(i)-foo(h);
    EndBody.
    
Function: main
    Body: 
        ** ** ** ** ** ** ** ** ** **
        **   ke ke ke ke ke ke ke  **
        **          nothing        **
        **           (^_^)         **
        ** ** ** ** ** ** ** ** ** **
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,291))
        
    def test_292(self):
        """ test ..."""
        input = """
Function: foo1
Parameter: i,j
    Body: 
        Var: m=0,n=0x12;
        While (True) || (i>=1) && (j<=m*n) Do
            If (i*j =/= m*n%i*j) Then
                i = foo2(foo1(1)\\.foo3(a[i]-foo4()));
                Break;
            Else Continue; 
            EndIf.       
        EndWhile.
    EndBody.
Var: a,b,c=10,d=12.e-10,f[10][10]={1,2,3,4},g[0x10][0o10]={{1,2,3},{0x12,0XABC,0X12AF},{0o12,0O07,0o00001}};    
Function: foo2
Parameter: i,j,k,m,n,check
    Body: 
        Var: a={1,2,3}, b="function", f=0x123, f[3]={"abc","def","xyz"};
        
    EndBody.
    
Function: foo3
    Body: 
        Var: check = True;
        For (i=foo1(-foo(2)),i!=foo6(-foo7(7)+foo4(4)),foo5(foo1 (2 + x, 4. \. y))) Do
            While (check!=False) && (i*-foo1(a[i])) Do
                If (!check) Then Break; EndIf.            
            EndWhile.
            a[i][j]=1.0e10 +. -19.e-10 \\. -foo1(-foo2(-foo3(-foo4(-foo5(-foo6))))) -. foo7(foo7()-.foo2 (foo2 (2 + x, 4. \. y)) % foo5(foo4(f-g+.4.),func()-.goo (foo (2 + x, 4. \. y))));
            string = "Assignment PPL is very difficult";
            recursive(1.2 +. n \\. i *. a[b[1][3]],func(func()-.goo (foo (2 + x, 4. \. y)) % foo(foo(f-g+.4.),func()-.goo (foo (2 + x, 4. \. y)))),a[foo(i)-f] +. 2. -. 2.109e-109
                    \\.foo(n%i-a[foo(i\\4)]));
            check = (test && True) || (!boolean) && (a<=.b+.1.);
        EndFor.
    EndBody.
    
Function: foo4
Parameter: array[10][10][10][10][10][10][10][10][10][10][10][10]
    Body: 
        If i>=0 Then Break;
        Else Return foo4(i) * foo4(i+1);
        EndIf.
    EndBody.
    
Function: foo5
    Body: 
        Var: i,j,k,m,n,a[10][10];
        For (i=1,i<n,2) Do
            foo1(foo2(foo3(foo4(foo5(foo6(foo7))))));
            For (j=foo(3),j<=n,1) Do
            If (a[i]>a[j]) Then
                temp = a[j];
                a[j]=a[i];
                a[i]=temp;
            EndIf.
        EndFor.
        EndFor.
        For (i=0,i<n,1) Do
            writeln(a[i]);
            foo(a[i]);
        EndFor.  
    EndBody.
    
Function: foo6
    Body: 
        Var: i,j,k,m,n,a[10][10];
        For (i=1,i<n,1) Do
            For (j=i+1,j<=n,1) Do
            If (a[i]>a[j]) Then
                temp = a[j];
                a[j]=a[i];
                Break;
                a[i]=temp;
            EndIf.
        EndFor.
            Break;
        EndFor. 
    EndBody.
    
Function: foo7
    Body: 
        Do 
           If foo(g)-foo(j)>0 Then 
            Var: i,k,m;
            k=foo(g)*foo(j);
            i=k%m;
            m=foo(a[i]);
           EndIf. 
        While (a>b) && (b<foo[j]) EndDo.
        Return foo(-b)-foo(i)-foo(h);
    EndBody.
    
Function: main
    Body: 
        ** ** ** ** ** ** ** ** ** **
        **   ke ke ke ke ke ke ke  **
        **          nothing        **
        **           (^_^)         **
        ** ** ** ** ** ** ** ** ** **
    EndBody.
        """
        expect = "Error on line 14 col 0: Var"
        self.assertTrue(TestParser.checkParser(input,expect,292))
        
    def test_293(self):
        """ test ..."""
        input = """
Var: a,b,c=10,d=12.e-10,f[10][10]={1,2,3,4},g[0x10][0o10]={{1,2,3},{0x12,0XABC,0X12AF},{0o12,0O7,0o1}};

Function: foo1
Parameter: i,j
    Body: 
        Var: m=0,n=0x12;
        While (True) || (i>=1) && (j<=m*n) Do
            If (i*j =/= m*n%i*j) Then
                i = foo2(foo1(1)\\.foo3(a[i]-foo4()));
                Break;
            Else Continue; 
            EndIf.       
        EndWhile.
    EndBody.
    
Function: foo2
Parameter: i,j,k,m,n,check
    Body: 
        Var: a={1,2,3}, b="function", f=0x123, f[3]={"abc","def","xyz"};
        
    EndBody.
    
Function: foo3
    Body: 
        Var: check = True;
        For (i=foo1(-foo(2)),i!=foo6(-foo7(7)+foo4(4)),foo5(foo1 (2 + x, 4. \. y))) Do
            While (check!=False) && (i*-foo1(a[i])) Do
                If (!check) Then Break; EndIf.            
            EndWhile.
            a[i][j]=1.0e10 +. -19.e-10 \\. -foo1(-foo2(-foo3(-foo4(-foo5(-foo6))))) -. foo7(foo7()-.foo2 (foo2 (2 + x, 4. \. y)) % foo5(foo4(f-g+.4.),func()-.goo (foo (2 + x, 4. \. y))));
            string = "Assignment PPL is very difficult";
            recursive(1.2 +. n \\. i *. a[b[1][3]],func(func()-.goo (foo (2 + x 4. \. y)) % foo(foo(f-g+.4.),func()-.goo (foo (2 + x, 4. \. y)))),a[foo(i)-f] +. 2. -. 2.109e-109
                    \\.foo(n%i-a[foo(i\\4)]));
            check = (test && True) || (!boolean) && (a<=.b+.1.);
        EndFor.
    EndBody.
    
Function: foo4
Parameter: array[10][10][10][10][10][10][10][10][10][10][10][10]
    Body: 
        If i>=0 Then Break;
        Else Return foo4(i) * foo4(i+1);
        EndIf.
    EndBody.
    
Function: foo5
    Body: 
        Var: i,j,k,m,n,a[10][10];
        For (i=1,i<n,2) Do
            foo1(foo2(foo3(foo4(foo5(foo6(foo7))))));
            For (j=foo(3),j<=n,1) Do
            If (a[i]>a[j]) Then
                temp = a[j];
                a[j]=a[i];
                a[i]=temp;
            EndIf.
        EndFor.
        EndFor.
        For (i=0,i<n,1) Do
            writeln(a[i]);
            foo(a[i]);
        EndFor.  
    EndBody.
    
Function: foo6
    Body: 
        Var: i,j,k,m,n,a[10][10];
        For (i=1,i<n,1) Do
            For (j=i+1,j<=n,1) Do
            If (a[i]>a[j]) Then
                temp = a[j];
                a[j]=a[i];
                Break;
                a[i]=temp;
            EndIf.
        EndFor.
            Break;
        EndFor. 
    EndBody.
    
Function: foo7
    Body: 
        Do 
           If foo(g)-foo(j)>0 Then 
            Var: i,k,m;
            k=foo(g)*foo(j);
            i=k%m;
            m=foo(a[i]);
           EndIf. 
        While (a>b) && (b<foo[j]) EndDo.
        Return foo(-b)-foo(i)-foo(h);
    EndBody.
    
Function: main
    Body: 
        ** ** ** ** ** ** ** ** ** **
        **   ke ke ke ke ke ke ke  **
        **          nothing        **
        **           (^_^)         **
        ** ** ** ** ** ** ** ** ** **
    EndBody.
        """
        expect = "Error on line 33 col 79: 4."
        self.assertTrue(TestParser.checkParser(input,expect,293))
        
    def test_294(self):
        """ test ..."""
        input = """
Var: a,b,c=10,d=12.e-10,f[10][10]={1,2,3,4},g[0x10][0o10]={{1,2,3},{0x12,0XABC,0X12AF},{0o12,0O7,0o1}};

Function: foo1
Parameter: i,j
    Body: 
        Var: m=0,n=0x12;
        While (True) || (i>=1) && (j<=m*n) Do
            If (i*j =/= m*n%i*j) Then
                i = foo2(foo1(1)\\.foo3(a[i]-foo4()));
                Break;
            Else Continue; 
            EndIf.       
        EndWhile.
    EndBody.
    
Function: foo2
Parameter: i,j,k,m,n,check
    Body: 
        Var: a={1,2,3}, b="function", f=0x123, f[3]={"abc","def","xyz"};
        
    EndBody.
    
Function: foo3
    Body: 
        Var: check = True;
        For (i=foo1(-foo(2)),i!=foo6(-foo7(7)+foo4(4)),foo5(foo1 (2 + x, 4. \. y))) Do
            While (check!=False) && (i*-foo1(a[i])) Do
                If (!check) Then Break; EndIf.            
            EndWhile.
            a[i][j]=1.0e10 +. -19.e-10 \\. -foo1(-foo2(-foo3(-foo4(-foo5(-foo6))))) -. foo7(foo7()-.foo2 (foo2 (2 + x, 4. \. y)) % foo5(foo4(f-g+.4.),func()-.goo (foo (2 + x, 4. \. y))));
            string = "Assignment PPL is very difficult";
            recursive(1.2 +. n \\. i *. a[b[1][3]],func(func()-.goo (foo (2 + x, 4. \. y)) % foo(foo(f-g+.4.),func()-.goo (foo (2 + x, 4. \. y)))),a[foo(i)-f] +. 2. -. 2.109e-109
                    \\.foo(n%i-a[foo(i\\4)]));
            check = (test && True) || (!boolean) && (a<=.b+.1.);
        EndFor.
    EndBody.
    
Function: foo4
Parameter: array[10][10][10][10][10][10][10][10][10][10][10][10]
    Body: 
        If i>=0 Then Break;
        Else Return foo4(i) * foo4(i+1);
        EndIf.
    EndBody.
    
Function: foo5
    Body: 
        Var: i,j,k,m,n,a[10][10];
        For (i=1,i<n,2) Do
            foo1(foo2(foo3(foo4(foo5(foo6(foo7))))));
            For (j=foo(3),j<=n,1) Do
            If (a[i]>a[j]) Then
                temp = a[j];
                a[j]=a[i];
                a[i]=temp;
            EndIf.
        EndFor.
        EndFor.
        For (i=0,i<n,1) Do
            writeln(a[i]);
            foo(a[i]);
        EndFor.  
    EndBody.
    
Function: foo6
    Body: 
        Var: i,j,k,m,n,a[10][10];
        For (i=1,i<n,1) Do
            For (j=i+1,j<=n,1) Do
            If (a[i]>a[j]) Then
                temp = a[j];
                a[j]=a[i];
                Break;
                a[i]=temp;
        EndFor.
            Break;
        EndFor. 
    EndBody.
    
Function: foo7
    Body: 
        Do 
           If foo(g)-foo(j)>0 Then 
            Var: i,k,m;
            k=foo(g)*foo(j);
            i=k%m;
            m=foo(a[i]);
           EndIf. 
        While (a>b) && (b<foo[j]) EndDo.
        Return foo(-b)-foo(i)-foo(h);
    EndBody.
    
Function: main
    Body: 
        ** ** ** ** ** ** ** ** ** **
        **   ke ke ke ke ke ke ke  **
        **          nothing        **
        **           (^_^)         **
        ** ** ** ** ** ** ** ** ** **
    EndBody.
        """
        expect = "Error on line 76 col 8: EndFor"
        self.assertTrue(TestParser.checkParser(input,expect,294))
        
    def test_295(self):
        """ test ..."""
        input = """
Var: a,b,c=10,d=12.e-10,f[10][10]={1,2,3,4},g[0x10][0o10]={{1,2,3},{0x12,0XABC,0X12AF},{0o12,0O7,0o1}};

Function: foo1
Parameter: i,j
    Body: 
        Var: m=0,n=0x12;
        While (True) || (i>=1) && (j<=m*n) Do
            If (i*j =/= m*n%i*j) Then
                i = foo2(foo1(1)\\.foo3(a[i]-foo4()));
                Break;
            Else Continue; 
            EndIf.       
        EndWhile.
    EndBody.
    
Function: foo2
Parameter: i,j,k,m,n,check
    Body: 
        Var: a={1,2,3}, b="function", f=0x123, f[3]={"abc","def","xyz"};
        
    EndBody.
    
Function: foo3
    Body: 
        Var: check = True;
        For (i=foo1(-foo(2)),i!=foo6(-foo7(7)+foo4(4)),foo5(foo1 (2 + x, 4. \. y))) Do
            While (check!=False) && (i*-foo1(a[i])) Do
                If (!check) Then Break; EndIf.            
            EndWhile.
            a[i][j]=1.0e10 +. -19.e-10 \\. -foo1(-foo2(-foo3(-foo4(-foo5(-foo6))))) -. foo7(foo7()-.foo2 (foo2 (2 + x, 4. \. y)) % foo5(foo4(f-g+.4.),func()-.goo (foo (2 + x, 4. \. y))));
            string = "Assignment PPL is very difficult";
            recursive(1.2 +. n \\. i *. a[b[1][3]],func(func()-.goo (foo (2 + x, 4. \. y)) % foo(foo(f-g+.4.),func()-.goo (foo (2 + x, 4. \. y)))),a[foo(i)-f] +. 2. -. 2.109e-109
                    \\.foo(n%i-a[foo(i\\4)]));
            check = (test && True) || (!boolean) && (a<=.b+.1.);
        EndFor.
    EndBody.
    
Function: foo4
Parameter: array[10][10][10][10][10][10][10][10][10][10][10][10]
    Body: 
        If i>=0 Then Break;
        Else Return foo4(i) * foo4(i+1);
        EndIf.
    EndBody.
    
Function: foo5
    Body: 
        Var: i,j,k,m,n,a[10][10];
        For (i=1,i<n,2) Do
            foo1(foo2(foo3(foo4(foo5(foo6(foo7)))));
            For (j=foo(3),j<=n,1) Do
            If (a[i]>a[j]) Then
                temp = a[j];
                a[j]=a[i];
                a[i]=temp;
            EndIf.
        EndFor.
        EndFor.
        For (i=0,i<n,1) Do
            writeln(a[i]);
            foo(a[i]);
        EndFor.  
    EndBody.
    
Function: foo6
    Body: 
        Var: i,j,k,m,n,a[10][10];
        For (i=1,i<n,1) Do
            For (j=i+1,j<=n,1) Do
            If (a[i]>a[j]) Then
                temp = a[j];
                a[j]=a[i];
                Break;
                a[i]=temp;
            EndIf.
        EndFor.
            Break;
        EndFor. 
    EndBody.
    
Function: foo7
    Body: 
        Do 
           If foo(g)-foo(j)>0 Then 
            Var: i,k,m;
            k=foo(g)*foo(j);
            i=k%m;
            m=foo(a[i]);
           EndIf. 
        While (a>b) && (b<foo[j]) EndDo.
        Return foo(-b)-foo(i)-foo(h);
    EndBody.
    
Function: main
    Body: 
        ** ** ** ** ** ** ** ** ** **
        **   ke ke ke ke ke ke ke  **
        **          nothing        **
        **           (^_^)         **
        ** ** ** ** ** ** ** ** ** **
    EndBody.
        """
        expect = "Error on line 51 col 51: ;"
        self.assertTrue(TestParser.checkParser(input,expect,295))
        
    def test_296(self):
        """ test ..."""
        input = """
Var: a,b,c=10,d=12.e-10,f[10][10]={1,2,3,4},g[0x10][0o10]={{1,2,3},{0x12,0XABC,0X12AF},{0o12,0O7,0o1}};

Function: foo1
Parameter: i,j
    Body: 
        Var: m=0,n=0x12;
        While (True) || (i>=1) && (j<=m*n) Do
            If (i*j =/= m*n%i*j) Then
                i = foo2(foo1(1)\\.foo3(a[i]-foo4()));
                Break;
            Else Continue; 
            EndIf.       
        EndWhile.
    EndBody.
    
Function: foo2
Parameter: i,j,k,m,n,check
    Body: 
        Var: a={1,2,3}, b="function", f=0x123, f[3]={"abc","def","xyz"};
        
    EndBody.
    
Function: foo3
    Body: 
        Var: check = True;
        For (i=foo1(-foo(2)),i!=foo6(-foo7(7)+foo4(4)),foo5(foo1 (2 + x, 4. \. y))) Do
            While (check!=False) && (i*-foo1(a[i])) Do
                If (!check) Then Break; EndIf.            
            EndWhile.
            a[i][j]=1.0e10 +. -19.e-10 \\. -foo1(-foo2(-foo3(-foo4(-foo5(-foo6))))) -. foo7(foo7()-.foo2 (foo2 (2 + x, 4. \. y)) % foo5(foo4(f-g+.4.),func()-.goo (foo (2 + x, 4. \. y))));
            string = "Assignment PPL is very difficult";
            recursive(1.2 +. n \\. i *. a[b[1][3]],func(func()-.goo (foo (2 + x, 4. \. y)) % foo(foo(f-g+.4.),func()-.goo (foo (2 + x, 4. \. y)))),a[foo(i)-f] +. 2. -. 2.109e-109
                    \\.foo(n%i-a[foo(i\\4)]));
            check = (test && True) || (!boolean) && (a<=.b+.1.);
        EndFor.
    EndBody.
    
Function: foo4
Parameter: array[10][10][10][10][10][10][10][10][10][10][10][10]
    Body: 
        If i>=0 Then Break;
        Else Return foo4(i) * foo4(i+1);
        EndIf.
    EndBody.
    
Function: foo5
    Body: 
        var: i,j,k,m,n,a[10][10];
        For (i=1,i<n,2) Do
            foo1(foo2(foo3(foo4(foo5(foo6(foo7))))));
            For (j=foo(3),j<=n,1) Do
            If (a[i]>a[j]) Then
                temp = a[j];
                a[j]=a[i];
                a[i]=temp;
            EndIf.
        EndFor.
        EndFor.
        For (i=0,i<n,1) Do
            writeln(a[i]);
            foo(a[i]);
        EndFor.  
    EndBody.
    
Function: foo6
    Body: 
        Var: i,j,k,m,n,a[10][10];
        For (i=1,i<n,1) Do
            For (j=i+1,j<=n,1) Do
            If (a[i]>a[j]) Then
                temp = a[j];
                a[j]=a[i];
                Break;
                a[i]=temp;
            EndIf.
        EndFor.
            Break;
        EndFor. 
    EndBody.
    
Function: foo7
    Body: 
        Do 
           If foo(g)-foo(j)>0 Then 
            Var: i,k,m;
            k=foo(g)*foo(j);
            i=k%m;
            m=foo(a[i]);
           EndIf. 
        While (a>b) && (b<foo[j]) EndDo.
        Return foo(-b)-foo(i)-foo(h);
    EndBody.
    
Function: main
    Body: 
        ** ** ** ** ** ** ** ** ** **
        **   ke ke ke ke ke ke ke  **
        **          nothing        **
        **           (^_^)         **
        ** ** ** ** ** ** ** ** ** **
    EndBody.
        """
        expect = "Error on line 49 col 11: :"
        self.assertTrue(TestParser.checkParser(input,expect,296))
        
    def test_297(self):
        """ test ..."""
        input = """
Var: a,b,c=10,d=12.e-10,f[10][10]={1,2,3,4},g[0x10][0o10]={{1,2,3},{0x12,0XABC,0X12AF},{0o12,0O7,0o1}};

Function: foo1
Parameter: i,j
    Body: 
        Var: m=0,n=0x12;
        While (True) || (i>=1) && (j<=m*n) Do
            If (i*j =/= m*n%i*j) Then
                i = foo2(foo1(1)\\.foo3(a[i]-foo4()));
                Break;
            Else Continue; 
            EndIf.       
        EndWhile.
    EndBody.
    
Function: foo2
Parameter: i,j,k,m,n,check
    Body: 
        Var: a={1,2,3}, b="function", f=0x123, f[3]={"abc","def","xyz"};
        
    EndBody.
    
Function: foo3
    Body: 
        Var: check = True;
        For (i=foo1(-foo(2)),i!=foo6(-foo7(7)+foo4(4)),foo5(foo1 (2 + x, 4. \. y))) Do
            While (check!=False) && (i*-foo1(a[i])) Do
                If (!check) Then Break; EndIf.            
            EndWhile.
            a[i][j]=1.0e10 +. -19.e-10 \\. -foo1(-foo2(-foo3(-foo4(-foo5(-foo6))))) -. foo7(foo7()-.foo2 (foo2 (2 + x, 4. \. y)) % foo5(foo4(f-g+.4.),func()-.goo (foo (2 + x, 4. \. y))));
            string = "Assignment PPL is very difficult";
            recursive(1.2 +. n \\. i *. a[b[1][3]],func(func()-.goo (foo (2 + x, 4. \. y)) % foo(foo(f-g+.4.),func()-.goo (foo (2 + x, 4. \. y)))),a[foo(i)-f] +. 2. -. 2.109e-109
                    \\.foo(n%i-a[foo(i\\4)]));
            check = (test && True) || (!boolean) && (a<=.b+.1.);
        EndFor.
    EndBody.
    
Function: foo4
Parameter: array[10][10][10][10][10][10][10][10][10][10][10][10]
    Body: 
        If i>=0 Then Break;
        Else Return foo4(i) * foo4(i+1);
        EndIf.
    EndBody.
    
Function: foo5
    Body: 
        Var: i,j,k,m,n,a[10][10];
        For (i=1,i<n,2) Do
            foo1(foo2(foo3(foo4(foo5(foo6(foo7))))));
            For (j=foo(3),j<=n,1) Do
            If (a[i]>a[j]) Then
                temp = a[j];
                a[j]=a[i];
                a[i]=temp;
            EndIf.
        EndFor.
        EndFor.
        For (i=0,i<n,1) Do
            writeln(a[i]);
            foo(a[i]);
        EndFor.  
    EndBody.
    
Function: foo6
    Body: 
        Var: i,j,k,m,n,a[10][10];
        For (i=1,i<n,1) Do
            For (j=i+1,j<=n,1) Do
            If (a[i]>a[j]) Then
                temp = a[j];
                a[j]=a[i];
                Break;
                a[i]=temp;
            EndIf.
        EndFor.
            Break;
        EndFor. 
    EndBody.
    
Function: foo7
    Body: 
        Do 
           If foo(g)-foo(j)>0 Then 
            Var: i,k,m;
            k=foo(g)*foo(j);
            i=k%m;
            m=foo(a[i]);
           EndIf. 
        While (a>b) && (b<foo[j]) EndDo.
        Return foo(-b)-foo(i)-foo(h);
    EndBody.
    
Function: main
    Body: 
        ** ** ** ** ** ** ** ** ** **
        **   ke ke ke ke ke ke ke  **
        **          nothing        **
        **           (^_^)         **
        ** ** ** ** ** ** ** ** ** ***
    EndBody.
        """
        expect = "Error on line 101 col 37: *"
        self.assertTrue(TestParser.checkParser(input,expect,297))
        
    def test_298(self):
        """ test ..."""
        input = """
Var: a,b,c=10,d=12.e-10,f[10][10]={1,2,3,4},g[0x10][0o10]={{1,2,3},{0x12,0XABC,0X12AF},{0o12,0O7,0o1}};

Function: foo1
Parameter: i,j
    Body: 
        Var: m=0,n=0x12;
        While (True) || (i>=1) && (j<=m*n) Do
            If (i*j =/= m*n%i*j) Then
                i = foo2(foo1(1)\\.foo3(a[i]-foo4()));
                Break;
            Else Continue; 
            EndIf.       
        EndWhile.
    EndBody.
    
Function: foo2
Parameter: i,j,k,m,n,check
    Body: 
        Var: a={1,2,3}, b="function", f=0x123, f[3]={"abc","def","xyz"};
        
    EndBody.
    
Function: foo3
    Body: 
        Var: check = True;
        For (i=foo1(-foo(2)),i!=foo6(-foo7(7)+foo4(4)),foo5(foo1 (2 + x, 4. \. y))) Do
            While (check!=False) && (i*-foo1(a[i])) Do
                If (!check) Then Break; EndIf.            
            EndWhile.
            a[i][j]=1.0e10 +. -19.e-10 \\. -foo1(-foo2(-foo3(-foo4(-foo5(-foo6))))) -. foo7(foo7()-.foo2 (foo2 (2 + x, 4. \. y)) % foo5(foo4(f-g+.4.),func()-.goo (foo (2 + x, 4. \. y))));
            string = "Assignment PPL is very difficult";
            recursive(1.2 +. n \\. i *. a[b[1][3]],func(func()-.goo (foo (2 + x, 4. \. y)) % foo(foo(f-g+.4.),func()-.goo (foo (2 + x, 4. \. y)))),a[foo(i)-f] +. 2. -. 2.109e-109
                    \\.foo(n%i-a[foo(i\\4)]));
            check = (test && True) || (!boolean) && (a<=.b+.1.);
        EndFor.
    EndBody.
    
Function: foo4
Parameter: array[10][10][10][10][10][10][10][10][10][10][10][10]
    Body: 
        If i>=0 Then Break;
        Else Return foo4(i) * foo4(i+1);
        EndIf.
    EndBody.
    
Function: foo5
    Body: 
        Var: i,j,k,m,n,a[10][10];
        For (i=1,i<n,2) Do
            foo1(foo2(foo3(foo4(foo5(foo6(foo7))))));
            For (j=foo(3),j<=n,1) Do
            If (a[i]>a[j]) Then
                temp = a[j];
                a[j]=a[i];
                a[i]=temp;
            EndIf.
        EndFor.
        EndFor.
        For (i=0,i<n,1) Do
            writeln(a[i]);
            foo(a[i]);
        EndFor.  
    EndBody.
    
Function: foo6
Parameter: 
    Body: 
        Var: i,j,k,m,n,a[10][10];
        For (i=1,i<n,1) Do
            For (j=i+1,j<=n,1) Do
            If (a[i]>a[j]) Then
                temp = a[j];
                a[j]=a[i];
                Break;
                a[i]=temp;
            EndIf.
        EndFor.
            Break;
        EndFor. 
    EndBody.
    
Function: foo7
    Body: 
        Do 
           If foo(g)-foo(j)>0 Then 
            Var: i,k,m;
            k=foo(g)*foo(j);
            i=k%m;
            m=foo(a[i]);
           EndIf. 
        While (a>b) && (b<foo[j]) EndDo.
        Return foo(-b)-foo(i)-foo(h);
    EndBody.
    
Function: main
    Body: 
        ** ** ** ** ** ** ** ** ** **
        **   ke ke ke ke ke ke ke  **
        **          nothing        **
        **           (^_^)         **
        ** ** ** ** ** ** ** ** ** **
    EndBody.
        """
        expect = "Error on line 68 col 4: Body"
        self.assertTrue(TestParser.checkParser(input,expect,298))
        
    def test_299(self):
        """ test ..."""
        input = """
Var: a,b,c=10,d=12.e-10,f[10][10]={1,2,3,4},g[0x10][0o10]={{1,2,3},{0x12,0XABC,0X12AF},{0o12,0O7,0o1}};

Function: foo1
Parameter: i,j
    Body: 
        Var: m=0,n=0x12;
        While (True) || (i>=1) && (j<=m*n) Do
            If (i*j =/= m*n%i*j) Then
                i = foo2(foo1(1)\\.foo3(a[i]-foo4()));
                Break;
            Else Continue; 
            EndIf.       
        EndWhile.
    EndBody.
    
Function: foo2
Parameter: i,j,k,m,n,check
    Body: 
        Var: a={1,2,3}, b="function, f=0x123, f[3]={"abc","def","xyz"};
        
    EndBody.
    
Function: foo3
    Body: 
        Var: check = True;
        For (i=foo1(-foo(2)),i!=foo6(-foo7(7)+foo4(4)),foo5(foo1 (2 + x, 4. \. y))) Do
            While (check!=False) && (i*-foo1(a[i])) Do
                If (!check) Then Break; EndIf.            
            EndWhile.
            a[i][j]=1.0e10 +. -19.e-10 \\. -foo1(-foo2(-foo3(-foo4(-foo5(-foo6))))) -. foo7(foo7()-.foo2 (foo2 (2 + x, 4. \. y)) % foo5(foo4(f-g+.4.),func()-.goo (foo (2 + x, 4. \. y))));
            string = "Assignment PPL is very difficult";
            recursive(1.2 +. n \\. i *. a[b[1][3]],func(func()-.goo (foo (2 + x, 4. \. y)) % foo(foo(f-g+.4.),func()-.goo (foo (2 + x, 4. \. y)))),a[foo(i)-f] +. 2. -. 2.109e-109
                    \\.foo(n%i-a[foo(i\\4)]));
            check = (test && True) || (!boolean) && (a<=.b+.1.);
        EndFor.
    EndBody.
    
Function: foo4
Parameter: array[10][10][10][10][10][10][10][10][10][10][10][10]
    Body: 
        If i>=0 Then Break;
        Else Return foo4(i) * foo4(i+1);
        EndIf.
    EndBody.
    
Function: foo5
    Body: 
        Var: i,j,k,m,n,a[10][10];
        For (i=1,i<n,2) Do
            foo1(foo2(foo3(foo4(foo5(foo6(foo7))))));
            For (j=foo(3),j<=n,1) Do
            If (a[i]>a[j]) Then
                temp = a[j];
                a[j]=a[i];
                a[i]=temp;
            EndIf.
        EndFor.
        EndFor.
        For (i=0,i<n,1) Do
            writeln(a[i]);
            foo(a[i]);
        EndFor.  
    EndBody.
    
Function: foo6
    Body: 
        Var: i,j,k,m,n,a[10][10];
        For (i=1,i<n,1) Do
            For (j=i+1,j<=n,1) Do
            If (a[i]>a[j]) Then
                temp = a[j];
                a[j]=a[i];
                Break;
                a[i]=temp;
            EndIf.
        EndFor.
            Break;
        EndFor. 
    EndBody.
    
Function: foo7
    Body: 
        Do 
           If foo(g)-foo(j)>0 Then 
            Var: i,k,m;
            k=foo(g)*foo(j);
            i=k%m;
            m=foo(a[i]);
           EndIf. 
        While (a>b) && (b<foo[j]) EndDo.
        Return foo(-b)-foo(i)-foo(h);
    EndBody.
    
Function: main
    Body: 
        ** ** ** ** ** ** ** ** ** **
        **   ke ke ke ke ke ke ke  **
        **          nothing        **
        **           (^_^)         **
        ** ** ** ** ** ** ** ** ** **
    EndBody.
        """
        expect = "Error on line 20 col 53: abc"
        self.assertTrue(TestParser.checkParser(input,expect,299))
        
    def test_300(self):
        """ test ..."""
        input = """
Var: a,b,c=10,d=12.e-10,f[10][10]={1,2,3,4},g[0x10][0o10]={{1,2,3},{0x12,0XABC,0X12AF},{0o12,0O7,0o1}};

Function: foo1
Parameter: i,j
    Body: 
        Var: m=0,n=0x12;
        While (True) || (i>=1) && (j<=m*n) Do
            If (i*j =/= m*n%i*j) Then
                i = foo2(foo1(1)\\.foo3(a[i]-foo4()));
                Break;
            Else Continue; 
            EndIf.       
        EndWhile.
    EndBody.
    
Function: foo2
Parameter: i,j,k,m,n,check
    Body: 
        Var: a={1,2,3}, b="function", f=0x123, f[3]={"abc","def","xyz"};
        
    EndBody.
    
Function: foo3
    Body: 
        Var: check = True;
        For (i=foo1(-foo(2)),i!=foo6(-foo7(7)+foo4(4)),foo5(foo1 (2 + x, 4. \. y))) Do
            While (check!=False) && (i*-foo1(a[i])) Do
                If (!check) Then Break; EndIf.            
            EndWhile.
            a[i][j]=1.0e10 +. -19.e-10 \\. -foo1(-foo2(-foo3(-foo4(-foo5(-foo6))))) -. foo7(foo7()-.foo2 (foo2 (2 + x, 4. \. y)) % foo5(foo4(f-g+.4.),func()-.goo (foo (2 + x, 4. \. y))));
            string = "Assignment PPL is very difficult";
            recursive(1.2 +. n \\. i *. a[b[1][3]],func(func()-.goo (foo (2 + x, 4. \. y)) % foo(foo(f-g+.4.),func()-.goo (foo (2 + x, 4. \. y)))),a[foo(i)-f] +. 2. -. 2.109e-109
                    \\.foo(n%i-a[foo(i\\4)]));
            check = (test && True) || (!boolean) && (a<=.b+.1.);
        EndFor.
    EndBody.
    
Function: foo4
Parameter: array[10][10][10][10][10][10][10][10][10][10][10][10]
    Body: 
        If i>=0 Then Break;
        Else Return foo4(i) * foo4(i+1);
        EndIf.
    EndBody.
    
Function: foo5
    Body: 
        Var: i,j,k,m,n,a[10][10];
        For (i=1,i<n,2) Do
            foo1(foo2(foo3(foo4(foo5(foo6(foo7))))));
            For (j=foo(3),j<=n,1) Do
            If (a[i]>a[j]) Then
                temp = a[j];
                a[j]=a[i];
                a[i]=temp;
            EndIf.
        EndFor.
        EndFor.
        For (i=0,i<n,1) Do
            writeln(a[i]);
            foo(a[i]);
        EndFor.  
    EndBody.
    
Function: foo6
    Body: 
        Var: i,j,k,m,n,a[10][10];
        For (i=1,i<n,1) Do
            For (j=i+1,j<=n,1) Do
            If (a[i]>a[j]) Then
                temp = a[j];
                a[j]==a[i];
                Break;
                a[i]=temp;
            EndIf.
        EndFor.
            Break;
        EndFor. 
    EndBody.
    
Function: foo7
    Body: 
        Do 
           If foo(g)-foo(j)>0 Then 
            Var: i,k,m;
            k=foo(g)*foo(j);
            i=k%m;
            m=foo(a[i]);
           EndIf. 
        While (a>b) && (b<foo[j]) EndDo.
        Return foo(-b)-foo(i)-foo(h);
    EndBody.
    
Function: main
    Body: 
        ** ** ** ** ** ** ** ** ** **
        **   ke ke ke ke ke ke ke  **
        **          nothing        **
        **           (^_^)         **
        ** ** ** ** ** ** ** ** ** **
    EndBody.
        """
        expect = "Error on line 73 col 20: =="
        self.assertTrue(TestParser.checkParser(input,expect,300))
        
    
        
    
        
        
    
        
        
        
        
  

    
        
    
        
    
    
 #   def test_wrong_miss_close(self):
  #      """Miss variable"""
  #      input = """Var: ;"""
 #       expect = "Error on line 1 col 5: ;"
  #      self.assertTrue(TestParser.checkParser(input,expect,211)) 