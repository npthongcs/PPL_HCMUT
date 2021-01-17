from functools import reduce

class StaticCheck(Visitor):
    
    def visitProgram(self,ctx:Program,o:object):
        reduce(lambda acc,ele: [acc[0] + [self.visit(ele,acc)] , acc[1] + [self.visit(ele,acc)] ],ctx.decl,[[],[]])

    def visitVarDecl(self,ctx:VarDecl,o:object):
        if list(filter(lambda x: x.name == ctx.name,o[0])): 
            raise RedeclaredVariable(ctx.name)
        else: return ctx

    def visitConstDecl(self,ctx:ConstDecl,o:object):
        if list(filter(lambda x: x.name == ctx.name,o[0])): 
            raise RedeclaredConstant(ctx.name)
        else: return ctx

    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        if list(filter(lambda x: x.name == ctx.name,o[0])): 
            raise RedeclaredFunction(ctx.name)
        lst = reduce(lambda acc,ele: [acc[0]+[self.visit(ele,acc)],acc[1]+[self.visit(ele,acc)]],ctx.param+ctx.body[0],[[],o[1]+[ctx]])
        for x in ctx.body[1]: 
            self.visit(x,lst[1])
        return ctx  
    
    def visitIntType(self,ctx:IntType,o:object):pass

    def visitFloatType(self,ctx:FloatType,o:object):pass

    def visitIntLit(self,ctx:IntLit,o:object):pass


    def visitId(self,ctx:Id,o:object):
        lst = list(filter(lambda x:x.name==ctx.name,o)) 
        if len(lst)==0:
            raise UndeclaredIdentifier(ctx.name)
        
# =========================================        
        
from functools import reduce

class StaticCheck(Visitor):
    
    def visitProgram(self,ctx:Program,o:object):
        o=[[]]
        for x in ctx.decl:
            self.visit(x,o)

    def visitVarDecl(self,ctx:VarDecl,o:object):
        if list(filter(lambda x: x == ctx.name,o[0])): 
            raise RedeclaredVariable(ctx.name)
        o[0]+=[ctx.name]

    def visitConstDecl(self,ctx:ConstDecl,o:object):
        if list(filter(lambda x: x == ctx.name,o[0])): 
            raise RedeclaredConstant(ctx.name)
        o[0]+=[ctx.name]

    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        if list(filter(lambda x: x == ctx.name,o[0])): 
            raise RedeclaredFunction(ctx.name)
        o[0]+=[ctx.name]
        o =[[]] +o
        for x in ctx.param+ctx.body[0]: 
            self.visit(x,o)
        for x in ctx.body[1]: 
            self.visit(x,o)
    
    def visitIntType(self,ctx:IntType,o:object):pass

    def visitFloatType(self,ctx:FloatType,o:object):pass

    def visitIntLit(self,ctx:IntLit,o:object):pass


    def visitId(self,ctx:Id,o:object):
        for x in o:
            if ctx.name in x:
                return
        raise UndeclaredIdentifier(ctx.name)
        