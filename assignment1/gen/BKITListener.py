# Generated from /Users/macintoshhd/Documents/PPL/assignment1/src/main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete listener for a parse tree produced by BKITParser.
class BKITListener(ParseTreeListener):

    # Enter a parse tree produced by BKITParser#program.
    def enterProgram(self, ctx:BKITParser.ProgramContext):
        pass

    # Exit a parse tree produced by BKITParser#program.
    def exitProgram(self, ctx:BKITParser.ProgramContext):
        pass


    # Enter a parse tree produced by BKITParser#var_decl.
    def enterVar_decl(self, ctx:BKITParser.Var_declContext):
        pass

    # Exit a parse tree produced by BKITParser#var_decl.
    def exitVar_decl(self, ctx:BKITParser.Var_declContext):
        pass


    # Enter a parse tree produced by BKITParser#listID.
    def enterListID(self, ctx:BKITParser.ListIDContext):
        pass

    # Exit a parse tree produced by BKITParser#listID.
    def exitListID(self, ctx:BKITParser.ListIDContext):
        pass


    # Enter a parse tree produced by BKITParser#typeID.
    def enterTypeID(self, ctx:BKITParser.TypeIDContext):
        pass

    # Exit a parse tree produced by BKITParser#typeID.
    def exitTypeID(self, ctx:BKITParser.TypeIDContext):
        pass


    # Enter a parse tree produced by BKITParser#array.
    def enterArray(self, ctx:BKITParser.ArrayContext):
        pass

    # Exit a parse tree produced by BKITParser#array.
    def exitArray(self, ctx:BKITParser.ArrayContext):
        pass


    # Enter a parse tree produced by BKITParser#dimension.
    def enterDimension(self, ctx:BKITParser.DimensionContext):
        pass

    # Exit a parse tree produced by BKITParser#dimension.
    def exitDimension(self, ctx:BKITParser.DimensionContext):
        pass


    # Enter a parse tree produced by BKITParser#init_var.
    def enterInit_var(self, ctx:BKITParser.Init_varContext):
        pass

    # Exit a parse tree produced by BKITParser#init_var.
    def exitInit_var(self, ctx:BKITParser.Init_varContext):
        pass


    # Enter a parse tree produced by BKITParser#unit_array.
    def enterUnit_array(self, ctx:BKITParser.Unit_arrayContext):
        pass

    # Exit a parse tree produced by BKITParser#unit_array.
    def exitUnit_array(self, ctx:BKITParser.Unit_arrayContext):
        pass


    # Enter a parse tree produced by BKITParser#init_array_.
    def enterInit_array_(self, ctx:BKITParser.Init_array_Context):
        pass

    # Exit a parse tree produced by BKITParser#init_array_.
    def exitInit_array_(self, ctx:BKITParser.Init_array_Context):
        pass


    # Enter a parse tree produced by BKITParser#init_array.
    def enterInit_array(self, ctx:BKITParser.Init_arrayContext):
        pass

    # Exit a parse tree produced by BKITParser#init_array.
    def exitInit_array(self, ctx:BKITParser.Init_arrayContext):
        pass


    # Enter a parse tree produced by BKITParser#func_decl.
    def enterFunc_decl(self, ctx:BKITParser.Func_declContext):
        pass

    # Exit a parse tree produced by BKITParser#func_decl.
    def exitFunc_decl(self, ctx:BKITParser.Func_declContext):
        pass


    # Enter a parse tree produced by BKITParser#parameter.
    def enterParameter(self, ctx:BKITParser.ParameterContext):
        pass

    # Exit a parse tree produced by BKITParser#parameter.
    def exitParameter(self, ctx:BKITParser.ParameterContext):
        pass


    # Enter a parse tree produced by BKITParser#stm.
    def enterStm(self, ctx:BKITParser.StmContext):
        pass

    # Exit a parse tree produced by BKITParser#stm.
    def exitStm(self, ctx:BKITParser.StmContext):
        pass


    # Enter a parse tree produced by BKITParser#assign_stm.
    def enterAssign_stm(self, ctx:BKITParser.Assign_stmContext):
        pass

    # Exit a parse tree produced by BKITParser#assign_stm.
    def exitAssign_stm(self, ctx:BKITParser.Assign_stmContext):
        pass


    # Enter a parse tree produced by BKITParser#if_stm.
    def enterIf_stm(self, ctx:BKITParser.If_stmContext):
        pass

    # Exit a parse tree produced by BKITParser#if_stm.
    def exitIf_stm(self, ctx:BKITParser.If_stmContext):
        pass


    # Enter a parse tree produced by BKITParser#for_smt.
    def enterFor_smt(self, ctx:BKITParser.For_smtContext):
        pass

    # Exit a parse tree produced by BKITParser#for_smt.
    def exitFor_smt(self, ctx:BKITParser.For_smtContext):
        pass


    # Enter a parse tree produced by BKITParser#while_stm.
    def enterWhile_stm(self, ctx:BKITParser.While_stmContext):
        pass

    # Exit a parse tree produced by BKITParser#while_stm.
    def exitWhile_stm(self, ctx:BKITParser.While_stmContext):
        pass


    # Enter a parse tree produced by BKITParser#dowhile_stm.
    def enterDowhile_stm(self, ctx:BKITParser.Dowhile_stmContext):
        pass

    # Exit a parse tree produced by BKITParser#dowhile_stm.
    def exitDowhile_stm(self, ctx:BKITParser.Dowhile_stmContext):
        pass


    # Enter a parse tree produced by BKITParser#break_stm.
    def enterBreak_stm(self, ctx:BKITParser.Break_stmContext):
        pass

    # Exit a parse tree produced by BKITParser#break_stm.
    def exitBreak_stm(self, ctx:BKITParser.Break_stmContext):
        pass


    # Enter a parse tree produced by BKITParser#continue_stm.
    def enterContinue_stm(self, ctx:BKITParser.Continue_stmContext):
        pass

    # Exit a parse tree produced by BKITParser#continue_stm.
    def exitContinue_stm(self, ctx:BKITParser.Continue_stmContext):
        pass


    # Enter a parse tree produced by BKITParser#call_stm.
    def enterCall_stm(self, ctx:BKITParser.Call_stmContext):
        pass

    # Exit a parse tree produced by BKITParser#call_stm.
    def exitCall_stm(self, ctx:BKITParser.Call_stmContext):
        pass


    # Enter a parse tree produced by BKITParser#call_func.
    def enterCall_func(self, ctx:BKITParser.Call_funcContext):
        pass

    # Exit a parse tree produced by BKITParser#call_func.
    def exitCall_func(self, ctx:BKITParser.Call_funcContext):
        pass


    # Enter a parse tree produced by BKITParser#return_stm.
    def enterReturn_stm(self, ctx:BKITParser.Return_stmContext):
        pass

    # Exit a parse tree produced by BKITParser#return_stm.
    def exitReturn_stm(self, ctx:BKITParser.Return_stmContext):
        pass


    # Enter a parse tree produced by BKITParser#index_operators.
    def enterIndex_operators(self, ctx:BKITParser.Index_operatorsContext):
        pass

    # Exit a parse tree produced by BKITParser#index_operators.
    def exitIndex_operators(self, ctx:BKITParser.Index_operatorsContext):
        pass


    # Enter a parse tree produced by BKITParser#exp.
    def enterExp(self, ctx:BKITParser.ExpContext):
        pass

    # Exit a parse tree produced by BKITParser#exp.
    def exitExp(self, ctx:BKITParser.ExpContext):
        pass


    # Enter a parse tree produced by BKITParser#exp1.
    def enterExp1(self, ctx:BKITParser.Exp1Context):
        pass

    # Exit a parse tree produced by BKITParser#exp1.
    def exitExp1(self, ctx:BKITParser.Exp1Context):
        pass


    # Enter a parse tree produced by BKITParser#exp2.
    def enterExp2(self, ctx:BKITParser.Exp2Context):
        pass

    # Exit a parse tree produced by BKITParser#exp2.
    def exitExp2(self, ctx:BKITParser.Exp2Context):
        pass


    # Enter a parse tree produced by BKITParser#exp3.
    def enterExp3(self, ctx:BKITParser.Exp3Context):
        pass

    # Exit a parse tree produced by BKITParser#exp3.
    def exitExp3(self, ctx:BKITParser.Exp3Context):
        pass


    # Enter a parse tree produced by BKITParser#exp4.
    def enterExp4(self, ctx:BKITParser.Exp4Context):
        pass

    # Exit a parse tree produced by BKITParser#exp4.
    def exitExp4(self, ctx:BKITParser.Exp4Context):
        pass


    # Enter a parse tree produced by BKITParser#exp5.
    def enterExp5(self, ctx:BKITParser.Exp5Context):
        pass

    # Exit a parse tree produced by BKITParser#exp5.
    def exitExp5(self, ctx:BKITParser.Exp5Context):
        pass


    # Enter a parse tree produced by BKITParser#exp6.
    def enterExp6(self, ctx:BKITParser.Exp6Context):
        pass

    # Exit a parse tree produced by BKITParser#exp6.
    def exitExp6(self, ctx:BKITParser.Exp6Context):
        pass


    # Enter a parse tree produced by BKITParser#exp7.
    def enterExp7(self, ctx:BKITParser.Exp7Context):
        pass

    # Exit a parse tree produced by BKITParser#exp7.
    def exitExp7(self, ctx:BKITParser.Exp7Context):
        pass


    # Enter a parse tree produced by BKITParser#operand.
    def enterOperand(self, ctx:BKITParser.OperandContext):
        pass

    # Exit a parse tree produced by BKITParser#operand.
    def exitOperand(self, ctx:BKITParser.OperandContext):
        pass


    # Enter a parse tree produced by BKITParser#literal.
    def enterLiteral(self, ctx:BKITParser.LiteralContext):
        pass

    # Exit a parse tree produced by BKITParser#literal.
    def exitLiteral(self, ctx:BKITParser.LiteralContext):
        pass



del BKITParser