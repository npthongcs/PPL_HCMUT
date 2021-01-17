from functools import reduce

class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o):
        acc = list(reduce(lambda acc,ele: acc+[self.visit(ele,acc)],ctx.decl,[]))
        return self.visit(ctx.exp,acc)

    def visitVarDecl(self,ctx:VarDecl,o):
        return ctx

    def visitBinOp(self,ctx:BinOp,o): 
        ltype = type(self.visit(ctx.e1,o))
        rtype = type(self.visit(ctx.e2,o))
        if ctx.op in ['+','-','*']:
            if BoolType in [ltype,rtype]:
                raise TypeMismatchInExpression(ctx)
            elif FloatType in [ltype,rtype]:
                return FloatType()
            else: return IntType()
        elif ctx.op == '/':
            if BoolType in [ltype,rtype]:
                raise TypeMismatchInExpression(ctx)
            else: return FloatType()
        elif ctx.op in ['!','&&','||']:
            if IntType in [ltype,rtype] or FloatType in [ltype,rtype]:
                raise TypeMismatchInExpression(ctx)
            else: return BoolType()
        else:
            if ltype == rtype: return BoolType()
            else: raise TypeMismatchInExpression(ctx)

    def visitUnOp(self,ctx:UnOp,o):
        rtype=(self.visit(ctx.e,o))
        if ctx.op == '-':
            if type(rtype) == BoolType:
                raise TypeMismatchInExpression(ctx)
            else: return rtype
        else:
            if type(rtype) == BoolType: return BoolType()
            else: raise TypeMismatchInExpression(ctx)

    def visitIntLit(self,ctx:IntLit,o): 
        return IntType()
        
    def visitFloatLit(self,ctx,o): 
        return FloatType()

    def visitBoolLit(self,ctx,o): 
        return BoolType()
        
    def visitId(self,ctx,o):
        for x in o:
            if x.name==ctx.name: return x.typ
        raise UndeclaredIdentifier(ctx.name)