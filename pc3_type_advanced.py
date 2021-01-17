from functools import reduce

class Type(ABC): pass

class IntType(Type): pass

class FloatType(Type): pass

class BoolType(Type): pass

class StaticCheck(Visitor):
    
    def visitProgram(self,ctx:Program,o):
        o=[[]]
        for x in ctx.decl:
            o[0]+=[self.visit(x,o)]
        for x in ctx.stmts:
            self.visit(x,o)

    def visitVarDecl(self,ctx:VarDecl,o):
        count=0
        for x in o[0]: 
            if x[0]==ctx.name: count+=1
        if count>0: raise Redeclared(ctx)
        return [ctx.name,None]   

    def visitFuncDecl(self,ctx:FuncDecl,o):
        if list(filter(lambda x: x[0]==ctx.name,o[0])):
            raise Redeclared(ctx)
        list_para=[[]]
        for x in ctx.param:
            list_para[0]+=[self.visit(x,list_para)]
        o[0]+=[[ctx.name,list_para[0]]]
        o=[list_para[0]]+o
        for x in ctx.local:
            o[0]+=[self.visit(x,o)]
        for x in ctx.stmts:
            self.visit(x,o)
        return [ctx.name,list_para[0]]
        
    def visitCallStmt(self,ctx:CallStmt,o):
        flag=False
        param=[]
        for x in o:
            for y in x: 
                if type(y[1]) is list and y[0]==ctx.name: 
                    flag=True
                    param=y[1]
                    break
            if flag==True: break
        if flag==False: raise UndeclaredIdentifier(ctx.name)
        if len(param)!=len(ctx.args): raise TypeMismatchInStatement(ctx)
        else: 
            for i in range(0,len(param)): 
                para=param[i]
                arg=self.visit(ctx.args[i],o)
                type_para=para[1]
                type_arg=arg
                if type(type_arg) is list:
                    type_arg=arg[1]
                if type_arg is None and type_para is None:
                    raise TypeCannotBeInferred(ctx)
                elif type_para is None and type_arg is not None:
                    para[1] = type_arg
                elif type_para is not None and type_arg is None:
                    arg[1] = type_para
                elif type_para is not type_arg:
                    raise TypeMismatchInStatement(ctx)     

    def visitAssign(self,ctx:Assign,o):
        left_exp=self.visit(ctx.lhs,o)
        right_exp=self.visit(ctx.rhs,o)
        left_type=left_exp[1]
        right_type=right_exp
        if type(right_exp) is list:
            right_type=right_exp[1]
        if left_type is None and right_type is None:
            raise TypeCannotBeInferred(ctx)
        elif left_type is not None and right_type is None: 
            right_exp[1] = left_type
        elif left_type is None and right_type is not None: 
            left_exp[1] = right_type
        elif left_type is not right_type: 
            raise TypeMismatchInStatement(ctx)

    def visitIntLit(self,ctx:IntLit,o):
        return IntType()

    def visitFloatLit(self,ctx,o):
        return FloatType()

    def visitBoolLit(self,ctx,o):
        return BoolType()

    def visitId(self,ctx,o):
        for x in o: 
            for i in x:
                if i[0]==ctx.name:
                    return i
        raise UndeclaredIdentifier(ctx.name)