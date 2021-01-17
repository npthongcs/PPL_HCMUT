from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *

class ASTGeneration(BKITVisitor):

    def visitProgram(self,ctx:BKITParser.ProgramContext):
        return Program(self.visit(ctx.list_var_decl()) + self.visit(ctx.list_func_decl()))

    # declare variable

    def visitList_var_decl(self,ctx:BKITParser.List_var_declContext):
        return self.visit(ctx.var_decl()) + self.visit(ctx.list_var_decl()) if ctx.getChildCount()==2 else self.visit(ctx.var_decl()) if ctx.getChildCount()==1 else []

    def visitVar_decl(self,ctx:BKITParser.Var_declContext):
        return self.visit(ctx.listID())

    def visitListID(self,ctx:BKITParser.ListIDContext):
        return self.visit(ctx.typeID()) + self.visit(ctx.listID()) if ctx.getChildCount()==3 else self.visit(ctx.typeID())

    def visitTypeID(self,ctx:BKITParser.TypeIDContext):
        if ctx.ID(): return [VarDecl(Id(ctx.ID().getText()),[],None)]
        elif ctx.typearray(): return self.visit(ctx.typearray())
        else: return self.visit(ctx.init_var())

    def visitTypearray(self,ctx:BKITParser.TypearrayContext):
        return [VarDecl(Id(ctx.ID().getText()),self.visit(ctx.dimension()),None)]

    def visitDimension(self,ctx:BKITParser.DimensionContext):
        if ctx.getChildCount()==4: return [self.visit(ctx.intlit())]+self.visit(ctx.dimension())
        else: return [self.visit(ctx.intlit())]

    def visitIntlit(self,ctx:BKITParser.IntlitContext):
        if ctx.HEXA(): return int(ctx.HEXA().getText(),16)
        elif ctx.OCTAL(): return int(ctx.OCTAL().getText(),8)
        else: return int(ctx.DEC().getText())

    def visitInit_var(self,ctx:BKITParser.Init_varContext):
        if ctx.getChildCount()==3: return [VarDecl(Id(ctx.ID().getText()),[],self.visit(ctx.literal()))]
        else: return [VarDecl(Id(ctx.ID().getText()),self.visit(ctx.dimension()),self.visit(ctx.literal()))]

    def visitLiteral(self,ctx:BKITParser.LiteralContext):
        if ctx.FLOAT(): return FloatLiteral(float(ctx.FLOAT().getText()))
        elif ctx.bool_literal(): return self.visit(ctx.bool_literal())
        elif ctx.STRING(): return StringLiteral(ctx.STRING().getText())
        elif ctx.DEC(): return IntLiteral(int(ctx.DEC().getText()))
        elif ctx.HEXA(): return IntLiteral(int(ctx.HEXA().getText(),16))
        elif ctx.OCTAL(): return IntLiteral(int(ctx.OCTAL().getText(), 8))
        else: return self.visit(ctx.array())

    def visitBool_literal(self,ctx:BKITParser.Bool_literalContext):
        return BooleanLiteral(True) if ctx.TRUE() else BooleanLiteral(False)

    def visitArray(self,ctx:BKITParser.ArrayContext):
        if ctx.getChildCount()==2: return ArrayLiteral([])
        else: return ArrayLiteral(self.visit(ctx.unit_array()))

    def visitUnit_array(self,ctx:BKITParser.Unit_arrayContext):
        if ctx.getChildCount()==1: return [self.visit(ctx.literal())]
        else: return [self.visit(ctx.literal())] + self.visit(ctx.unit_array())

    # declare function

    def visitList_func_decl(self,ctx:BKITParser.List_func_declContext):
        return self.visit(ctx.func_decl()) + self.visit(ctx.list_func_decl()) if ctx.getChildCount()==2 else self.visit(ctx.func_decl()) if ctx.getChildCount()==1 else []

    def visitFunc_decl(self,ctx:BKITParser.Func_declContext):
        if ctx.getChildCount()==9: return [FuncDecl(Id(ctx.ID().getText()),[],(self.visit(ctx.list_var_decl()),self.visit(ctx.list_stm())))]
        else: return [FuncDecl(Id(ctx.ID().getText()),self.visit(ctx.parameter()),(self.visit(ctx.list_var_decl()),self.visit(ctx.list_stm())))]

    def visitParameter(self,ctx:BKITParser.ParameterContext):
        return self.visit(ctx.list_para())

    def visitList_para(self,ctx:BKITParser.List_paraContext):
        return self.visit(ctx.typePara()) + self.visit(ctx.list_para()) if ctx.getChildCount()==3 else self.visit(ctx.typePara())

    def visitTypePara(self,ctx:BKITParser.TypeParaContext):
        if ctx.ID(): return [VarDecl(Id(ctx.ID().getText()),[],None)]
        else: return self.visit(ctx.typearray())

    # statement

    def visitList_stm(self,ctx:BKITParser.List_stmContext):
        if ctx.getChildCount()==2: return self.visit(ctx.stm()) + self.visit(ctx.list_stm())
        elif ctx.getChildCount()==1: return self.visit(ctx.stm())
        else: return []

    def visitStm(self,ctx:BKITParser.StmContext):
        if ctx.assign_stm(): return self.visit(ctx.assign_stm())
        elif ctx.if_stm(): return self.visit(ctx.if_stm())
        elif ctx.for_stm(): return self.visit(ctx.for_stm())
        elif ctx.while_stm(): return self.visit(ctx.while_stm())
        elif ctx.dowhile_stm(): return self.visit(ctx.dowhile_stm())
        elif ctx.break_stm(): return self.visit(ctx.break_stm())
        elif ctx.continue_stm(): return self.visit(ctx.continue_stm())
        elif ctx.call_stm(): return self.visit(ctx.call_stm())
        else: return self.visit(ctx.return_stm())

    # assignment statement
    def visitAssign_stm(self,ctx:BKITParser.Assign_stmContext):
        return [Assign(self.visit(ctx.lhs()),self.visit(ctx.exp()))]

    def visitLhs(self,ctx:BKITParser.LhsContext):
        if ctx.ID(): return Id(ctx.ID().getText())
        else: return self.visit(ctx.exp6())

    def visitIndex_operators(self,ctx:BKITParser.Index_operatorsContext):
        res=[]
        for x in ctx.exp():
            res+=[self.visit(x)]
        return res
    # expression

    def visitExp(self,ctx:BKITParser.ExpContext):
        if ctx.getChildCount()==1: return self.visit(ctx.exp1(0))
        else: return BinaryOp(self.visit(ctx.relational()),self.visit(ctx.exp1(0)),self.visit(ctx.exp1(1)))

    def visitRelational(self,ctx:BKITParser.RelationalContext):
        if ctx.EQ(): return ctx.EQ().getText()
        elif ctx.NEQ(): return ctx.NEQ().getText()
        elif ctx.LESS(): return ctx.LESS().getText()
        elif ctx.GREATER(): return ctx.GREATER().getText()
        elif ctx.LEQ(): return ctx.LEQ().getText()
        elif ctx.GEQ(): return ctx.GEQ().getText()
        elif ctx.NEQF(): return ctx.NEQF().getText()
        elif ctx.LESSF(): return ctx.LESSF().getText()
        elif ctx.GREATERF(): return ctx.GREATERF().getText()
        elif ctx.LEQF(): return ctx.LEQF().getText()
        else: return ctx.GEQF().getText()

    def visitExp1(self,ctx:BKITParser.Exp1Context):
        if ctx.getChildCount() == 1: return self.visit(ctx.exp2())
        else:
            if ctx.AND(): return BinaryOp(ctx.AND().getText(),self.visit(ctx.exp1()),self.visit(ctx.exp2()))
            else: return BinaryOp(ctx.OR().getText(),self.visit(ctx.exp1()),self.visit(ctx.exp2()))

    def visitExp2(self,ctx:BKITParser.Exp2Context):
        if ctx.getChildCount() == 1: return self.visit(ctx.exp3())
        else:
            if ctx.SUB(): return BinaryOp(ctx.SUB().getText(),self.visit(ctx.exp2()),self.visit(ctx.exp3()))
            elif ctx.SUBF(): return BinaryOp(ctx.SUBF().getText(),self.visit(ctx.exp2()),self.visit(ctx.exp3()))
            elif ctx.ADD(): return BinaryOp(ctx.ADD().getText(),self.visit(ctx.exp2()),self.visit(ctx.exp3()))
            else: return BinaryOp(ctx.ADDF().getText(),self.visit(ctx.exp2()),self.visit(ctx.exp3()))

    def visitExp3(self,ctx:BKITParser.Exp3Context):
        if ctx.getChildCount() == 1: return self.visit(ctx.exp4())
        else:
            if ctx.MUL(): return BinaryOp(ctx.MUL().getText(),self.visit(ctx.exp3()),self.visit(ctx.exp4()))
            elif ctx.MULF(): return BinaryOp(ctx.MULF().getText(),self.visit(ctx.exp3()),self.visit(ctx.exp4()))
            elif ctx.DIV(): return BinaryOp(ctx.DIV().getText(),self.visit(ctx.exp3()),self.visit(ctx.exp4()))
            elif ctx.DIVF(): return BinaryOp(ctx.DIVF().getText(), self.visit(ctx.exp3()), self.visit(ctx.exp4()))
            else: return BinaryOp(ctx.MODUL().getText(),self.visit(ctx.exp3()),self.visit(ctx.exp4()))

    def visitExp4(self,ctx:BKITParser.Exp4Context):
        if ctx.getChildCount() == 1: return self.visit(ctx.exp5())
        else: return UnaryOp(ctx.NOT().getText(),self.visit(ctx.exp4()))

    def visitExp5(self,ctx:BKITParser.Exp5Context):
        if ctx.getChildCount() == 1: return self.visit(ctx.exp6())
        elif ctx.SUB(): return UnaryOp(ctx.SUB().getText(),self.visit(ctx.exp5()))
        else: return UnaryOp(ctx.SUBF().getText(),self.visit(ctx.exp5()))

    def visitExp6(self,ctx:BKITParser.Exp6Context):
        if ctx.getChildCount() == 1: return self.visit(ctx.exp7())
        else: return ArrayCell(self.visit(ctx.exp6()),self.visit(ctx.index_operators())) ####

    def visitExp7(self,ctx:BKITParser.Exp7Context):
        if ctx.getChildCount() == 1: return self.visit(ctx.exp8())
        else: return self.visit(ctx.call_func()) + self.visit(ctx.exp8())

    def visitCall_func(self,ctx:BKITParser.Call_funcContext):
        if ctx.getChildCount()==3: return CallExpr(Id(ctx.ID().getText()),[])
        else: return CallExpr(Id(ctx.ID().getText()),self.visit(ctx.para_call_func()))

    def visitPara_call_func(self,ctx:BKITParser.Para_call_funcContext):
        if ctx.getChildCount()==1: return [self.visit(ctx.exp())]
        else: return [self.visit(ctx.exp())] + self.visit(ctx.para_call_func())

    def visitExp8(self,ctx:BKITParser.Exp8Context):
        return self.visit(ctx.operand())

    def visitOperand(self,ctx:BKITParser.OperandContext):
        if ctx.ID(): return Id(ctx.ID().getText())
       # elif ctx.typearray(): return self.visit(ctx.typearray())
        elif ctx.literal(): return self.visit(ctx.literal())
        elif ctx.call_func(): return self.visit(ctx.call_func())
        else: return self.visit(ctx.exp())

    # IF statement

    def visitIf_stm(self,ctx:BKITParser.If_stmContext):
        ifstm=[(self.visit(ctx.exp()),self.visit(ctx.list_var_decl()),self.visit(ctx.list_stm()))]
        elifstm=self.visit(ctx.list_elseif())
        elsestm=self.visit(ctx.else_())
        return [If(ifstm+elifstm,elsestm)]

    def visitList_elseif(self,ctx:BKITParser.List_elseifContext):
        if ctx.getChildCount()==6: return [(self.visit(ctx.exp()),self.visit(ctx.list_var_decl()),self.visit(ctx.list_stm()))] + self.visit(ctx.list_elseif())
        else: return []

    def visitElse_(self,ctx:BKITParser.Else_Context):
        if ctx.getChildCount()==3: return (self.visit(ctx.list_var_decl()),self.visit(ctx.list_stm()))
        else: return [(),()]

    # FOR statement

    def visitFor_stm(self,ctx:BKITParser.For_stmContext):
        return [For(Id(ctx.ID().getText()),self.visit(ctx.exp(0)),self.visit(ctx.exp(1)),self.visit(ctx.exp(2)),(self.visit(ctx.list_var_decl()),self.visit(ctx.list_stm())))]

    # WHILE statement

    def visitWhile_stm(self,ctx:BKITParser.While_stmContext):
        return [While(self.visit(ctx.exp()),(self.visit(ctx.list_var_decl()),self.visit(ctx.list_stm())))]

    # Dowhile statement

    def visitDowhile_stm(self,ctx:BKITParser.Dowhile_stmContext):
        return [Dowhile((self.visit(ctx.list_var_decl()),self.visit(ctx.list_stm())),self.visit(ctx.exp()))]

    # Break statement

    def visitBreak_stm(self,ctx:BKITParser.Break_stmContext):
        return [Break()]

    # Break statement

    def visitContinue_stm(self,ctx:BKITParser.Continue_stmContext):
        return [Continue()]

    # Call statement

    def visitCall_stm(self,ctx:BKITParser.Call_stmContext):
        if ctx.getChildCount()==4: return [CallStmt(Id(ctx.ID().getText()),[])]
        else: return [CallStmt(Id(ctx.ID().getText()),self.visit(ctx.para_call_stm()))]

    def visitPara_call_stm(self,ctx:BKITParser.Para_call_funcContext):
        if ctx.getChildCount()==1: return [self.visit(ctx.exp())]
        else: return [self.visit(ctx.exp())] + self.visit(ctx.para_call_stm())

    # Return statement

    def visitReturn_stm(self,ctx:BKITParser.Return_stmContext):
        if ctx.getChildCount()==2: return [Return(None)]
        else: return [Return(self.visit(ctx.exp()))]







