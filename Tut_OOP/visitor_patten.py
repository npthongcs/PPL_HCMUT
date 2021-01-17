class Expr(object):
    def accept(self, visitor):
        method_name = 'visit_{}'.format(self.__class__.__name__.lower())
        visit = getattr(visitor, method_name)
        return visit(self)

class Visitor: pass
    
class IntLit(Expr): 
    def __init__(self,n):
        self.intnum = n
        
class Eval(Visitor): 
    def visit_intlit(self,i): 
        return i.intnum     
    def vist_floatlit(self,i): 
        return i.floatnum
    def visit_binexp(self,s): 
        if s.operator == '+':  return s.left.accept(self)+s.right.accept(self)
        if s.operator == '-':  return s.left.accept(self)-s.right.accept(self)
        if s.operator == '*':  return s.left.accept(self)*s.right.accept(self)
        if s.operator == '/':  return s.left.accept(self)/s.right.accept(self)
    def visit_unexp(self,s): 
        if s.operator=='-': return -(s.arg.accep(self))
        if s.operator=='+': return (s.arg.accep(self))   
        
class PrintPrefix(Visitor):          
    def visit_upexp(self,s): 
        return '.'+s.operator+' '+s.arg.accept(self)
    def visit_binexp(self,s): 
        return s.operator+' '+str(s.left.accept(self))+' '+str(s.right.accept(self))
    def visit_intlit(self,i): 
        return i.intnum
    def visit_floatlit(self,i): 
        return i.floatlit 
    
class PrintPostfix(Visitor):          
    def visit_upexp(self,s): 
        return s.arg.accept(self)+' .'+s.operator
    def visit_binexp(self,s): 
        return str(s.left.accept(self))+' '+str(s.right.accept(self))+' '+s.operator
    def visit_intlit(self,i): 
        return i.intnum
    def visit_floatlit(self,i): 
        return i.floatlit    
        
class FloatLit(Expr):
    def __init__(self,n):
        self.floatnum = n
        
class BinExp(Expr):
    def __init__(self,exp1,s,exp2): 
        self.operator =s 
        self.left = exp1
        self.right = exp2

class UnExp(Expr): 
    def __init__(self,s,exp): 
        self.operator =s
        self.arg=exp


#t = BinExp(IntLit(3),'+',BinExp(IntLit(4),'*',FloatLit(2.0)))
x1 = BinExp(IntLit(2),'+',IntLit(4))
print(x1.accept(PrintPostfix()))
    
    