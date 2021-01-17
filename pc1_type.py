from abc import ABC

class Type(ABC): pass

class IntType(Type): pass

class FloatType(Type) : pass

class BoolType(Type): pass

class StaticCheck(Visitor):

    def visitBinOp(self,ctx:BinOp,o): 
        ltype = type(self.visit(ctx.e1,o))
        rtype = type(self.visit(ctx.e2,o))
        if ctx.op in ['+','-','*']:
            if BoolType in [(ltype),rtype]:
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