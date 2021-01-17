from abc import ABC

class Expr(ABC): 
    pass

class Var(Expr): 
    def __init__(self,s):
        self.name = s

class Number(Expr): 
    def __init__(self,n): 
        self.num = n
    def dprint(self): 
        print(self.num)

class UnOp(Expr): 
    def __init__(self,s,exp): 
        self.operator = s
        self.arg = exp
        
class BinOp(Expr):
    def __init__(self,s,exp1,exp2): 
        self.operator =s 
        self.left = exp1
        self.right = exp2
        
    def eval(self):
        if (type(self.left).__name__ != 'Var'): 
            x = self.left
        elif (type(self.left).__name__ != 'BinOp'):
            x = self.left.eval()
        else: x = 1
        if (type(self.right).__name__ != 'Var'): 
            y = self.right
        else: y = 1
        if self.operator == "+": 
            return Number(x+y)
        if self.operator == "-": 
            return Number(x-y)
        if self.operator == "*": 
            return Number(x*y)
        if self.operator == "/": 
            return Number((x/y))

 
#t= BinOp("-",Var('x'),Var('y'))           
t = BinOp("*",BinOp("+",1,0.2),3) 
t.eval() 