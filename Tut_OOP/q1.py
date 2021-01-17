from abc import ABC

class Expr(ABC): pass
    
class IntLit(Expr): 
    def __init__(self,n):
        self.intnum = n
    def eval(self): 
        return self.intnum
    def printPrefix(self): 
        return str(self.intnum)+' '
        
class FloatLit(Expr):
    def __init__(self,n):
        self.floatnum = n
    def eval(self): 
        return self.floatnum
    def printPrefix(self): 
        return str(self.floatnum)+' '
        
        
class BinExp(Expr):
    def __init__(self,exp1,s,exp2): 
        self.operator =s 
        self.left = exp1
        self.right = exp2
        
    def eval(self): 
        if self.operator == '+':  return self.left.eval()+self.right.eval()
        if self.operator == '-':  return self.left.eval()-self.right.eval()
        if self.operator == '*':  return self.left.eval()*self.right.eval()
        if self.operator == '/':  return self.left.eval()/self.right.eval()
    
    def printPrefix(self): 
        return self.operator+' '+self.left.printPrefix()+self.right.printPrefix()
        
        
        
class UnExp(Expr): 
    def __init__(self,s,exp): 
        self.operator =s
        self.arg=exp
    def eval(self):
        if self.operator=='-': return -(self.arg.eval())
        if self.operator=='-': return (self.arg.eval())    
    def printPrefix(self): 
        return self.operator+'. '+self.arg.printPrefix()

x1=IntLit(4)       
x2=UnExp('-',x1)
x3=IntLit(3)
x4=IntLit(2)
x5=BinExp(x3,'*',x4)
x6=BinExp(x2,'+',x5)

#t = BinExp(IntLit(3),'+',BinExp(IntLit(4),'*',FloatLit(2.0)))
print(x6.printPrefix())
    
    