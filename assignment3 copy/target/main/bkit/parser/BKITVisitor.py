# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete generic visitor for a parse tree produced by BKITParser.

class BKITVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKITParser#program.
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#list_var_decl.
    def visitList_var_decl(self, ctx:BKITParser.List_var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#list_func_decl.
    def visitList_func_decl(self, ctx:BKITParser.List_func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_decl.
    def visitVar_decl(self, ctx:BKITParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#listID.
    def visitListID(self, ctx:BKITParser.ListIDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#typeID.
    def visitTypeID(self, ctx:BKITParser.TypeIDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#typearray.
    def visitTypearray(self, ctx:BKITParser.TypearrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#dimension.
    def visitDimension(self, ctx:BKITParser.DimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#init_var.
    def visitInit_var(self, ctx:BKITParser.Init_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#unit_array.
    def visitUnit_array(self, ctx:BKITParser.Unit_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#array.
    def visitArray(self, ctx:BKITParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_decl.
    def visitFunc_decl(self, ctx:BKITParser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#parameter.
    def visitParameter(self, ctx:BKITParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#list_para.
    def visitList_para(self, ctx:BKITParser.List_paraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#typePara.
    def visitTypePara(self, ctx:BKITParser.TypeParaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#list_stm.
    def visitList_stm(self, ctx:BKITParser.List_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#stm.
    def visitStm(self, ctx:BKITParser.StmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#assign_stm.
    def visitAssign_stm(self, ctx:BKITParser.Assign_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#lhs.
    def visitLhs(self, ctx:BKITParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#if_stm.
    def visitIf_stm(self, ctx:BKITParser.If_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#list_elseif.
    def visitList_elseif(self, ctx:BKITParser.List_elseifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#else_.
    def visitElse_(self, ctx:BKITParser.Else_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#for_stm.
    def visitFor_stm(self, ctx:BKITParser.For_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#while_stm.
    def visitWhile_stm(self, ctx:BKITParser.While_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#dowhile_stm.
    def visitDowhile_stm(self, ctx:BKITParser.Dowhile_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#break_stm.
    def visitBreak_stm(self, ctx:BKITParser.Break_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#continue_stm.
    def visitContinue_stm(self, ctx:BKITParser.Continue_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#call_stm.
    def visitCall_stm(self, ctx:BKITParser.Call_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#para_call_stm.
    def visitPara_call_stm(self, ctx:BKITParser.Para_call_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#call_func.
    def visitCall_func(self, ctx:BKITParser.Call_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#para_call_func.
    def visitPara_call_func(self, ctx:BKITParser.Para_call_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#return_stm.
    def visitReturn_stm(self, ctx:BKITParser.Return_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#index_operators.
    def visitIndex_operators(self, ctx:BKITParser.Index_operatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp.
    def visitExp(self, ctx:BKITParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp1.
    def visitExp1(self, ctx:BKITParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp2.
    def visitExp2(self, ctx:BKITParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp3.
    def visitExp3(self, ctx:BKITParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp4.
    def visitExp4(self, ctx:BKITParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp5.
    def visitExp5(self, ctx:BKITParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp6.
    def visitExp6(self, ctx:BKITParser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp7.
    def visitExp7(self, ctx:BKITParser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp8.
    def visitExp8(self, ctx:BKITParser.Exp8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#operand.
    def visitOperand(self, ctx:BKITParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#literal.
    def visitLiteral(self, ctx:BKITParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#relational.
    def visitRelational(self, ctx:BKITParser.RelationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#intlit.
    def visitIntlit(self, ctx:BKITParser.IntlitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#bool_literal.
    def visitBool_literal(self, ctx:BKITParser.Bool_literalContext):
        return self.visitChildren(ctx)



del BKITParser