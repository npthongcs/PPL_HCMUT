class M:
    def foo(self,i):
        print(i * 2) 

class N(M):
    pass

class Q(N):
    def foo(self,i):
        print(i * i)    
        
x = Q