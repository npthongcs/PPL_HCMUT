from functools import reduce

class Type(ABC): pass

class IntType(Type): pass

class FloatType(Type): pass

class BoolType(Type): pass

class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o):
        o = list(reduce(lambda acc,ele: acc+[self.visit(ele,acc)],ctx.decl,[]))
        for x in ctx.stmts: 
            self.visit(x,o)

    def visitVarDecl(self,ctx:VarDecl,o):
        return [ctx.name,None]

    def visitAssign(self,ctx:Assign,o):
        r,l = self.visit(ctx.rhs,o),self.visit(ctx.lhs,o)
        type_r = r
        type_l = l[1]
        if type(type_r) is list: 
            type_r = r[1]

        if (type_l is None) and (type_r is None): 
            raise TypeCannotBeInferred(ctx)
        elif type_l is None and type_r is not None : 
            l[1] = type_r
        elif type_r is None and type_l is not None: 
            r[1] = type_l
        elif type(type_l) is not type(type_r): 
            raise TypeMismatchInStatement(ctx)
        
    def visitBinOp(self,ctx:BinOp,o):
        left = self.visit(ctx.e1,o)
        right = self.visit(ctx.e2,o)
        typeleft = type(left)
        typeright = type(right)
        if typeleft is list:
            typeleft = type(left[1])
        if typeright is list:
            typeright = type(right[1])
        
        if ctx.op in ['+','-','*','/']:
            if (FloatType in [typeleft,typeright]) or (BoolType in [typeleft,typeright]): 
                raise TypeMismatchInExpression(ctx)
            if typeleft is type(None): 
                left[1] = IntType()
            if typeright is type(None): 
                right[1] = IntType()
            return IntType()
        
        if ctx.op in ['+.','-.','*.','/.']:
            if (IntType in [typeleft,typeright]) or (BoolType in [typeleft,typeright]):  
                raise TypeMismatchInExpression(ctx)
            if typeleft is type(None): 
                left[1] = FloatType()
            if typeright is type(None): 
                right[1] = FloatType()
            return FloatType()
        
        if ctx.op in ['>','=']:
            if (FloatType in [typeleft,typeright]) or (BoolType in [typeleft,typeright]): 
                raise TypeMismatchInExpression(ctx)
            if typeleft is type(None): 
                left[1] = IntType()
            if typeright is type(None): 
                right[1] = IntType()
            return BoolType()
        
        if ctx.op in ['>.','=.']:
            if (IntType in [typeleft,typeright]) or (BoolType in [typeleft,typeright]):  
                raise TypeMismatchInExpression(ctx)
            if typeleft is type(None): 
                left[1] = FloatType()
            if typeright is type(None): 
                right[1] = FloatType()
            return BoolType()
        
        if ctx.op in ['&&','||','>b','=b']:
            if (IntType in [typeleft,typeright]) or (FloatType in [typeleft,typeright]):  
                raise TypeMismatchInExpression(ctx)
            if typeleft is type(None): 
                left[1] = BoolType()
            if typeright is type(None): 
                right[1] = BoolType()
            return BoolType()
      
    def visitUnOp(self,ctx:UnOp,o):
        exp = self.visit(ctx.e,o)
        type_exp = type(exp)
        if type_exp is list: 
            type_exp = type(exp[1])
        
        if ctx.op == '-': 
            if type_exp is type(None):
                exp[1] = IntType()
            elif type_exp is not IntType:
                raise TypeMismatchInExpression(ctx)
            return IntType()
    
        if ctx.op == '-.': 
            if type_exp is type(None):
                exp[1] = FloatType()
            elif type_exp is not FloatType:
                raise TypeMismatchInExpression(ctx)
            return FloatType()
        
        if ctx.op == '!': 
            if type_exp is type(None):
                exp[1] = BoolType()
            elif type_exp is not BoolType:
                raise TypeMismatchInExpression(ctx)
            return BoolType()
        
        if ctx.op == 'i2f': 
            if type_exp is type(None):
                exp[1] = IntType()
            elif type_exp is not IntType:
                raise TypeMismatchInExpression(ctx)
            return FloatType()

        if ctx.op == 'floor': 
            if type_exp is type(None):
                exp[1] = FloatType()
            elif type_exp is not FloatType:
                raise TypeMismatchInExpression(ctx)
            return IntType()

    def visitIntLit(self,ctx:IntLit,o):
        return IntType()

    def visitFloatLit(self,ctx,o):
        return FloatType()

    def visitBoolLit(self,ctx,o):
        return BoolType()
        
    def visitId(self,ctx,o):
        for x in o:
            if x[0] == ctx.name:
                return x
        raise UndeclaredIdentifier(ctx.name)
        