
"""
 * @author nhphung
"""
from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List, Tuple
from AST import * 
from Visitor import *
from StaticError import *
from functools import *

class Type(ABC):
    __metaclass__ = ABCMeta
    pass
class Prim(Type):
    __metaclass__ = ABCMeta
    pass
class IntType(Prim):
    pass
class FloatType(Prim):
    pass
class StringType(Prim):
    pass
class BoolType(Prim):
    pass
class VoidType(Type):
    pass
class Unknown(Type):
    pass

@dataclass
class ArrayType(Type):
    dimen:List[int]
    eletype: Type

@dataclass
class MType:
    intype:List[Type]
    restype:Type

@dataclass
class Symbol:
    name: str
    mtype:MType

class StaticChecker(BaseVisitor):
    def __init__(self,ast):
        self.ast = ast
        self.global_envi = [
Symbol("int_of_float",MType([FloatType()],IntType())),
Symbol("float_to_int",MType([IntType()],FloatType())),
Symbol("int_of_string",MType([StringType()],IntType())),
Symbol("string_of_int",MType([IntType()],StringType())),
Symbol("float_of_string",MType([StringType()],FloatType())),
Symbol("string_of_float",MType([FloatType()],StringType())),
Symbol("bool_of_string",MType([StringType()],BoolType())),
Symbol("string_of_bool",MType([BoolType()],StringType())),
Symbol("read",MType([],StringType())),
Symbol("printLn",MType([],VoidType())),
Symbol("print",MType([StringType()],VoidType())),
Symbol("printStrLn",MType([StringType()],VoidType()))]                           


    def check(self):
        return self.visit(self.ast,self.global_envi)

    def visitProgram(self,ast, c):
        c=[c] # c[0] --> function
        flagmain = False
        for x in ast.decl:
            if isinstance(x,VarDecl):
                # check same name Function build-in
                for y in c[0]:
                    if y.name == x.variable.name:
                        raise Redeclared(Variable(), x.variable.name)
                c.append(self.visit(x,c[1:]))
            else: # --> this is declare function
                # check Function redeclared
                if x.name.name=='main':
                    flagmain = True
                for i in c[1:]:
                    if i[0]==x.name.name:
                        raise Redeclared(Function(),x.name.name)
                for i in c[0]:
                    if i.name==x.name.name:
                        raise Redeclared(Function(),x.name.name)
                # get type parameter
                listparam=[]
                for i in x.param:
                    if len(i.varDimen)!=0:
                        listparam+=[ArrayType(i.varDimen,Unknown())]
                    else:
                        listparam+=[Unknown()]
                c[0]+=[Symbol(x.name.name,MType(listparam,Unknown()))]
        if flagmain == False:
            raise NoEntryPoint()

        # modify c
        lst = c[1:]
        for i in c[0]:
            lst.append(i)
        c = lst
        for x in ast.decl:
            if isinstance(x,FuncDecl):
                self.visit(x,c)

    def visitVarDecl(self,ast,c):
        # check in variable declared
        for x in c:
            if x[0]==ast.variable.name:
                raise Redeclared(Variable(),ast.variable.name)

        if len(ast.varDimen)==0: # scalar variable
            if ast.varInit==None: # not initial
                return [ast.variable.name,Unknown()]
            else: # initial
                return [ast.variable.name,self.visit(ast.varInit,c)]
        else:   # composite variable
            if ast.varInit!=None:   # init
                return [ast.variable.name,self.visit(ast.varInit,c)]
            else:
                return [ast.variable.name,ArrayType(ast.varDimen,Unknown())]

    def visitFuncDecl(self,ast,c):
        lst=[]
        # get type parameter
        typeparam=None
        for x in c:
            if isinstance(x,Symbol) and x.name==ast.name.name:
                typeparam=x.mtype.intype
                break
        # declared parameter
        count = 0
        for x in ast.param:
            for i in lst:
                if x.variable.name==i[0]:
                    raise Redeclared(Parameter(),x.variable.name)
            if len(x.varDimen)==0:
                lst+=[[x.variable.name,typeparam[count]]]
            else:
                lst+=[[x.variable.name,ArrayType(x.varDimen,Unknown())]]
            count+=1

        # declared variable in function
        for x in ast.body[0]:
            lst+=[self.visit(x,lst)]    # <------ NOTE
        # update environment
        lst = lst + c
        # get index
        for i in range(len(lst)):
            if isinstance(lst[i],Symbol) and lst[i].name==ast.name.name:
                index = i
                break
        lst = lst + [ast.name.name]
        # statement in function
        for x in ast.body[1]:
            if type(x) is Return:
                treturn,exp = self.visit(x,lst)
                if type(lst[index].mtype.restype) is Unknown and type(treturn) is Unknown:
                    raise TypeCannotBeInferred(x)
                elif type(lst[index].mtype.restype) is Unknown and type(treturn) is not Unknown:
                    lst[index].mtype.restype = treturn
                elif type(lst[index].mtype.restype) is not Unknown and type(treturn) is not Unknown and type(lst[index].mtype.restype) is not type(treturn):
                    raise TypeMismatchInStatement(x)
                elif type(lst[index].mtype.restype) is not Unknown and type(treturn) is Unknown and type(exp) is list:
                    # exp is ID
                    if type(exp[0]) is list and exp[0][1]!='arraytype' and exp[0][1] != 'funccell':
                        exp[0][1]=lst[index].mtype.restype
                    # exp is func call
                    elif type(exp) is int:
                        lst[exp].mtype.restype = lst[index].mtype.restype
                    # exp is func cell
                    elif type(exp[0]) is list and exp[0][1]=='funccell':
                        lst[exp[0][0]].mtype.restype = lst[index].mtype.restype
                    # exp is array type
                    elif type(exp[0]) is list and exp[0][1] =='arraytype':
                        exp[0][0][1].eletype = lst[index].mtype.restype
            else: self.visit(x,lst)
        #  function no return and type is Unknown --> VoidType
        for i in range(len(lst)):
            if isinstance(lst[i],Symbol) and lst[i].name==ast.name.name:
                if type(lst[i].mtype.restype) is Unknown:
                    lst[i].mtype.restype = VoidType()
                break

    def visitId(self,ast,c):
        for x in c:
            if type(x) is list and x is not isinstance(x,Symbol) and x[0] == ast.name:
                return x
        raise Undeclared(Identifier(),ast.name)

    def inferFunc(self,exp,typeInfer,c):
        for x in c:
            if isinstance(x,Symbol) and x.name == exp.method.name:
                if type(x.mtype.restype) is Unknown:
                    x.mtype.restype = typeInfer
                    return 'YES'
                elif type(x.mtype.restype) is not type(typeInfer):
                    return 'NO'

    def visitBinaryOp(self,ast,c):
        op=ast.op
        # ==================
        if type(ast.left) is CallExpr:
            if op in['+','-','*','\\','%','==','!=','<','<=','>','>=']:
                str = self.inferFunc(ast.left,IntType(),c)
                if str == 'NO':
                    raise TypeMismatchInExpression(ast)
            elif op in['+.','-.','*.','\\.','=/=','<.','<=.','>.','>=.']:
                str = self.inferFunc(ast.left,FloatType(),c)
                if str == 'NO':
                    raise TypeMismatchInExpression(ast)
            elif op in['&&','||']:
                str = self.inferFunc(ast.left,BoolType(),c)
                if str == 'NO':
                    raise TypeMismatchInExpression(ast)
        lexp = self.visit(ast.left, c)
        if type(ast.right) is CallExpr:
            if op in['+','-','*','\\','%','==','!=','<','<=','>','>=']:
                str = self.inferFunc(ast.right,IntType(),c)
                if str == 'NO':
                    raise TypeMismatchInExpression(ast)
            elif op in['+.','-.','*.','\\.','=/=','<.','<=.','>.','>=.']:
                str = self.inferFunc(ast.right,FloatType(),c)
                if str == 'NO':
                    raise TypeMismatchInExpression(ast)
            elif op in['&&','||']:
                str = self.inferFunc(ast.right,BoolType(),c)
                if str == 'NO':
                    raise TypeMismatchInExpression(ast)
        # =================
        rexp=self.visit(ast.right,c)
        # if type(lexp) is VoidType or type(rexp) is VoidType:
        #     raise TypeMismatchInExpression(ast)

        if lexp=='error' or rexp=='error':
            return 'error'
        # operand is arraytype
        if type(lexp) is list and lexp[1]=='arraytype':
            ltype=type(lexp[0][1].eletype)
            lkind='arraytype'
        if type(rexp) is list and rexp[1] == 'arraytype':
            rtype = type(rexp[0][1].eletype)
            rkind = 'arraytype'
        # operand is ID
        if type(lexp) is list and lexp[1]!='arraytype' and lexp[1] != 'funccell':
            ltype = type(lexp[1])
            lkind='ID'
        if type(rexp) is list and rexp[1]!='arraytype' and rexp[1] != 'funccell':
            rtype = type(rexp[1])
            rkind='ID'
        # operand is literal
        if type(lexp) is IntType or type(lexp) is FloatType or type(lexp) is StringType or type(lexp) is BoolType or type(lexp) is ArrayType:
            ltype=type(lexp)
        if type(rexp) is IntType or type(rexp) is FloatType or type(rexp) is StringType or type(rexp) is BoolType or type(rexp) is ArrayType:
            rtype=type(rexp)
        # operand is call function
        if type(lexp) is int:
            lindex=lexp
            ltype=type(c[lindex].mtype.restype)
            lkind='symbol'
        if type(rexp) is int:
            rindex = rexp
            rtype = type(c[rindex].mtype.restype)
            rkind = 'symbol'
        # operand is func cell
        if type(lexp) is list and type(lexp[0]) is int:
            lindex = lexp[0]
            ltype = type(c[lindex].mtype.restype.eletype)
            lkind = 'funccell'
        if type(rexp) is list and type(rexp[0]) is int:
            rindex = rexp[0]
            rtype = type(c[rindex].mtype.restype.eletype)
            rkind = 'funccell'

        # processing
        if op in ['+','-','*','\\','%']:
            if StringType in [ltype,rtype] or FloatType in [ltype,rtype] or BoolType in [ltype,rtype] or ArrayType in [ltype,rtype] or VoidType in [ltype,rtype]:
                raise TypeMismatchInExpression(ast)
            if ltype is Unknown:
                if lkind=='ID': lexp[1]=IntType()
                elif lkind=='symbol': c[lindex].mtype.restype=IntType()
                elif lkind=='arraytype': lexp[0][1].eletype=IntType()
                elif lkind=='funccell': c[lindex].mtype.restype.eletype=IntType()
            if rtype is Unknown:
                if rkind == 'ID': rexp[1] = IntType()
                elif rkind == 'symbol': c[rindex].mtype.restype = IntType()
                elif rkind == 'arraytype': rexp[0][1].eletype = IntType()
                elif rkind == 'funccell': c[rindex].mtype.restype.eletype = IntType()
            return IntType()

        if op in ['+.','-.','*.','\\.']:
            if StringType in [ltype,rtype] or IntType in [ltype,rtype] or BoolType in [ltype,rtype] or ArrayType in [ltype,rtype] or VoidType in [ltype,rtype]:
                raise TypeMismatchInExpression(ast)
            if ltype is Unknown:
                if lkind=='ID': lexp[1]=FloatType()
                elif lkind=='symbol': c[lindex].mtype.restype=FloatType()
                elif lkind == 'arraytype': lexp[0][1].eletype = FloatType()
                elif lkind == 'funccell': c[lindex].mtype.restype.eletype = FloatType()
            if rtype is Unknown:
                if rkind == 'ID': rexp[1] = FloatType()
                elif rkind == 'symbol': c[rindex].mtype.restype = FloatType()
                elif rkind == 'arraytype': rexp[0][1].eletype = FloatType()
                elif rkind == 'funccell': c[rindex].mtype.restype.eletype = FloatType()
            return FloatType()

        if op in ['&&','||']:
            if StringType in [ltype,rtype] or FloatType in [ltype,rtype] or IntType in [ltype,rtype] or ArrayType in [ltype,rtype] or VoidType in [ltype,rtype]:
                raise TypeMismatchInExpression(ast)
            if ltype is Unknown:
                if lkind=='ID': lexp[1]=BoolType()
                elif lkind=='symbol': c[lindex].mtype.restype=BoolType()
                elif lkind == 'arraytype': lexp[0][1].eletype = BoolType()
                elif lkind == 'funccell': c[lindex].mtype.restype.eletype = BoolType()
            if rtype is Unknown:
                if rkind == 'ID': rexp[1] = BoolType()
                elif rkind == 'symbol': c[rindex].mtype.restype = BoolType()
                elif rkind == 'arraytype': rexp[0][1].eletype = BoolType()
                elif rkind == 'funccell': c[rindex].mtype.restype.eletype = BoolType()
            return BoolType()

        if op in ['==','!=','<','<=','>','>=']:
            if StringType in [ltype,rtype] or FloatType in [ltype,rtype] or BoolType in [ltype,rtype] or ArrayType in [ltype,rtype] or VoidType in [ltype,rtype]:
                raise TypeMismatchInExpression(ast)
            if ltype is Unknown:
                if lkind=='ID': lexp[1]=IntType()
                elif lkind=='symbol': c[lindex].mtype.restype=IntType()
                elif lkind == 'arraytype': lexp[0][1].eletype = IntType()
                elif lkind == 'funccell': c[lindex].mtype.restype.eletype = IntType()
            if rtype is Unknown:
                if rkind == 'ID': rexp[1] = IntType()
                elif rkind == 'symbol': c[rindex].mtype.restype = IntType()
                elif rkind == 'arraytype': rexp[0][1].eletype = IntType()
                elif rkind == 'funccell': c[rindex].mtype.restype.eletype = IntType()
            return BoolType()

        if op in ['=/=','<.','<=.','>.','>=.']:
            if StringType in [ltype,rtype] or IntType in [ltype,rtype] or BoolType in [ltype,rtype] or ArrayType in [ltype,rtype] or VoidType in [ltype,rtype]:
                raise TypeMismatchInExpression(ast)
            if ltype is Unknown:
                if lkind=='ID': lexp[1]=FloatType()
                elif lkind=='symbol': c[lindex].mtype.restype=FloatType()
                elif lkind == 'arraytype': lexp[0][1].eletype = FloatType()
                elif lkind == 'funccell': c[lindex].mtype.restype.eletype = FloatType()
            if rtype is Unknown:
                if rkind == 'ID': rexp[1] = FloatType()
                elif rkind == 'symbol': c[rindex].mtype.restype= FloatType()
                elif rkind == 'arraytype': lexp[0][1].eletype = FloatType()
                elif rkind == 'funccell': c[rindex].mtype.restype.eletype = FloatType()
            return BoolType()

    def visitUnaryOp(self,ast,c):
        op=ast.op
        # ==========
        if type(ast.body) is CallExpr:
            if op == '-':
                str = self.inferFunc(ast.body,IntType(),c)
                if str == 'NO':
                    raise TypeMismatchInExpression(ast)
            elif op == '-.':
                str = self.inferFunc(ast.body,FloatType(),c)
                if str == 'NO':
                    raise TypeMismatchInExpression(ast)
            elif op == '!':
                str = self.inferFunc(ast.body,BoolType(),c)
                if str == 'NO':
                    raise TypeMismatchInExpression(ast)
        # ==========
        exp=self.visit(ast.body,c)
        # if type(exp) is VoidType:
        #     raise TypeMismatchInExpression(ast)
        # arg error
        if exp=='error':
            return 'error'
        # exp is func cell
        if type(exp) is list and type(exp[0]) is int:
            index=exp[0]
            texp = c[index].mtype.restype.eletype
            kind = 'funccell'
        # operand is arraytype
        if type(exp) is list and exp[1] == 'arraytype':
            texp = type(exp[0][1].eletype)
            kind = 'arraytype'
        # operand is ID
        if type(exp) is list and exp[1] != 'arraytype' and exp[1] != 'funccell':
            texp=type(exp[1])
            kind='ID'
        # operand is Literal
        if type(exp) is IntType or type(exp) is FloatType or type(exp) is StringType or type(exp) is BoolType or type(exp) is ArrayType:
            texp=type(exp)
        # operand is Function
        if type(exp) is int:
            index=exp
            texp = type(c[index].mtype.restype)
            kind = 'symbol'
        # processing
        if op=='-':
            if texp is Unknown:
                if kind=='ID':
                    exp[1]=IntType()
                elif kind=='symbol':
                    c[index].mtype.restype=IntType()
                elif kind == 'arraytype':
                    exp[0][1].eletype = IntType()
                elif kind == 'funccell':
                    c[index].mtype.restype.eletype=IntType()
            elif texp is not IntType:
                raise TypeMismatchInExpression(ast)
            return IntType()
        elif op=='-.':
            if texp is Unknown:
                if kind=='ID':
                    exp[1]=FloatType()
                elif kind=='symbol':
                    c[index].mtype.restype=FloatType()
                elif kind == 'arraytype':
                    exp[0][1].eletype = FloatType()
                elif kind == 'funccell':
                    c[index].mtype.restype.eletype=FloatType()
            elif texp is not FloatType:
                raise TypeMismatchInExpression(ast)
            return FloatType()
        elif op=='!':
            if texp is Unknown:
                if kind=='ID':
                    exp[1]=BoolType()
                elif kind=='symbol':
                    c[index].mtype.restype=BoolType()
                elif kind == 'arraytype':
                    exp[0][1].eletype = BoolType()
                elif kind == 'funccell':
                    c[index].mtype.restype.eletype=BoolType()
            elif texp is not BoolType:
                raise TypeMismatchInExpression(ast)
            return BoolType()

    def visitCallExpr(self,ast,c): # return index of function
        flag=False # function is declared???
        idx=-1
        for i in range(len(c)):
            if isinstance(c[i],Symbol) and c[i].name==ast.method.name:
                idx=i
                flag=True
                break
            elif not isinstance(c[i],Symbol) and c[i][0]==ast.method.name:
                idx=-10
                break
        # name method is name variable
        if idx==-10:
            raise Undeclared(Function(),ast.method.name)
        # function isn't declared
        if flag==False:
            raise Undeclared(Function(),ast.method.name)
        # check param
        if len(ast.param)!=len(c[idx].mtype.intype):
            raise TypeMismatchInExpression(ast)
        # check type param
        arg=ast.param
        typeparam=c[idx].mtype.intype     # typeparam is list[type] and use typeparam to update c
        for i in range(len(arg)):
            # get type argument
            # ===============
            if type(arg[i]) is CallExpr:
                for x in c:
                    if isinstance(x, Symbol) and x.name == arg[i].method.name:
                        texp = x.mtype.restype
                        if type(texp) is Unknown and type(typeparam[i]) is Unknown:
                            return 'error'
                        elif type(texp) is not Unknown and type(typeparam[i]) is Unknown:
                            typeparam[i] = texp
                        elif type(texp) is Unknown and type(typeparam[i]) is not Unknown:
                            x.mtype.restype = typeparam[i]
                        elif type(texp) is not type(typeparam[i]):
                            raise TypeMismatchInExpression(arg[i])
                        break
                    elif not isinstance(x, Symbol) and x[0] == arg[i].method.name:
                        raise Undeclared(Function(), arg[i].method.name)
            # ===============
            exp=self.visit(arg[i],c)
            # if type(exp) is VoidType:
            #     raise TypeMismatchInExpression(ast)
            if exp=='error':
                return 'error'
            # exp is func cell
            if type(exp) is list and type(exp[0]) is int:
                index = exp[0]
                texp = c[index].mtype.restype.eletype
                kind = 'funccell'
            # exp is arraytype
            elif type(exp) is list and exp[1]=='arraytype':
                texp = exp[0][1].eletype
                kind='arraytype'
            elif type(exp) is list and exp[1]!='arraytype' and exp[1] != 'funccell': # exp is ID
                texp=exp[1]
                kind='ID'
            elif type(exp) is IntType or type(exp) is FloatType or type(exp) is StringType or type(exp) is BoolType or type(exp) is ArrayType:
                texp=exp
            elif type(exp) is int: # exp is call function
                index = exp
                texp = c[index].mtype.restype
                if type(texp) is VoidType:
                    raise TypeMismatchInExpression(ast)
                kind = 'symbol'
            if type(texp) is Unknown and type(typeparam[i]) is Unknown:
                return 'error'
            elif type(texp) is Unknown and type(typeparam[i]) is not Unknown:
                if kind=='ID':
                    exp[1]=typeparam[i]
                elif kind=='symbol':
                    c[index].mtype.restype=typeparam[i]
                elif kind=='arraytype':
                    exp[0][1].eletype=typeparam[i]
                elif kind == 'funccell':
                    c[index].mtype.restype.eletype=typeparam[i]
            elif type(texp) is not Unknown and type(typeparam[i]) is Unknown:
                typeparam[i]=texp
            elif type(texp) is not type(typeparam[i]):
                raise TypeMismatchInExpression(ast)
        # update c
        c[idx].mtype.intype=typeparam
        # <---- NOTE
        # i = 0
        # for x in c:
        #     if type(x) is list and len(x)==3:
        #         x[1]=typeparami]
        #         i+=1
        return idx

    def visitArrayCell(self,ast,c):
        arr=self.visit(ast.arr,c)
        if arr=='error':
            return 'error'
        # invalid type arr ( not is ID or call exp)
        if type(arr) is not list and type(arr) is not int:
            raise TypeMismatchInExpression(ast)

        # check type dimension of array cell
        for x in ast.idx:
            exp = self.visit(x, c)
            # if type(exp) is VoidType:
            #     raise TypeMismatchInExpression(ast)
            # exp is ID
            if type(exp) is list and exp[1] != 'arraytype' and exp[1] != 'funccell':
                if type(exp[1]) is Unknown:
                    exp[1] = IntType()
                elif type(exp[1]) is not IntType:
                    raise TypeMismatchInExpression(ast)
            # exp is literal different Int
            elif type(exp) is FloatType or type(exp) is StringType or type(exp) is BoolType or type(exp) is ArrayType or type(exp) is VoidType:
                raise TypeMismatchInExpression(ast)
            # exp is func call
            elif type(exp) is int:
                index = exp
                texp = c[index].mtype.restype
                if type(texp) is FloatType or type(texp) is StringType or type(texp) is BoolType or type(texp) is ArrayType or type(exp) is VoidType:
                    raise TypeMismatchInExpression(ast)
                elif type(texp) is Unknown:
                    c[index].mtype.restype = IntType()
            # exp is array cell
            elif type(exp) is list and exp[1] == 'arraytype':
                texp = exp[0][1].eletype
                if type(texp) is Unknown:
                    exp[0][1].eletype = IntType()
                elif type(texp) is not IntType:
                    raise TypeMismatchInExpression(ast)
            # exp is func cell
            elif type(exp) is list and type(exp[0]) is int:
                index = exp[0]
                texp = c[index].mtype.restype.eletype
                if type(texp) is Unknown:
                    c[index].mtype.restype.eletype = IntType()
                elif type(texp) is not IntType:
                    raise TypeMismatchInExpression(ast)

        # arr is ID
        if type(arr) is list and arr[1] != 'arraytype' and arr[1] != 'funccell':
            if type(arr[1]) is not ArrayType:
                raise TypeMismatchInExpression(ast)
            # check dimension
            if type(arr[1]) is ArrayType and len(arr[1].dimen) != len(ast.idx):
                raise TypeMismatchInExpression(ast)
            return [arr,'arraytype']      # [[name,ArrayType],'arraytype']

        elif type(arr) is int:
            index=arr
            texp=c[index].mtype.restype
            if type(texp) is Unknown:
                return 'error'
            elif type(texp) is not ArrayType:
                raise TypeMismatchInExpression(ast)
            elif len(ast.idx) != len(texp.dimen):
                raise TypeMismatchInExpression(ast)
            return [index,'funccell']

    def visitAssign(self,ast,c):
        lhs=self.visit(ast.lhs,c)
        ltype = Unknown()
        # test =================
        if type(ast.rhs) is BinaryOp:
            if ast.rhs.op in ['+','-','*','\\','%']:
                ltype = IntType()
            elif ast.rhs.op in ['+.','-.','*.','\\.']:
                ltype = FloatType()
            elif ast.rhs.op in ['==','!=','<','<=','>','>=','&&','||','=/=','<.','<=.','>.','>=.']:
                ltype = BoolType()
        elif type(ast.rhs) is UnaryOp:
            if ast.rhs.op == '-':
                ltype = IntType()
            elif ast.rhs.op == '-.':
                ltype = FloatType()
            elif ast.rhs.op == '!':
                ltype = BoolType()

        # =======================
        # lhs is array cell
        if type(lhs) is list and lhs[1] == 'arraytype':
            if type(lhs[0][1].eletype) is Unknown:
                lhs[0][1].eletype = ltype
            else : ltype = lhs[0][1].eletype
            # elif type(ltype) is Unknown:
            #     ltype = lhs[0][1].eletype
            # elif type(ltype) is not type(lhs[0][1].eletype):
            #     raise TypeMismatchInExpression(ast.rhs)
            lkind = 'arraytype'
        # lhs is ID
        elif type(lhs) is list and lhs[1] != 'arraytype' and lhs[1] != 'funccell':
            if type(lhs[1]) is Unknown:
                lhs[1] = ltype
            # elif type(ltype) is Unknown:
            #     ltype = lhs[1]
            elif type(ltype) is ArrayType:
                raise TypeMismatchInStatement(ast)
            else: ltype = lhs[1]
            # elif type(ltype) is not type(lhs[1]):
            #     raise TypeMismatchInExpression(ast.rhs)
            lkind = 'ID'
        # lhs is func cell
        elif type(lhs) is list and type(lhs[0]) is int:
            lindex = lhs[0]
            if type(c[lindex].mtype.restype.eletype) is Unknown:
                c[lindex].mtype.restype.eletype = ltype
            else: ltype = c[lindex].mtype.restype.eletype
            # elif type(ltype) is not type(c[lindex].mtype.restype.eletype):
            #     raise TypeMismatchInExpression(ast.rhs)
            lkind = 'funccell'

        # =======================
        # ======
        if type(ast.rhs) is CallExpr:
            for x in c:
                if isinstance(x,Symbol) and x.name==ast.rhs.method.name:
                    rtype = x.mtype.restype
                    if type(rtype) is VoidType:
                        raise TypeMismatchInStatement(ast)
                    elif type(ltype) is Unknown and type(rtype) is Unknown:
                        raise TypeCannotBeInferred(ast)
                    elif type(ltype) is not Unknown and type(rtype) is Unknown:
                        x.mtype.restype = ltype
                elif not isinstance(x,Symbol) and x[0]==ast.rhs.method.name:
                    raise Undeclared(Function(),ast.rhs.method.name)

        # ======
        rhs = self.visit(ast.rhs,c)
        if lhs=='error' or rhs=='error':
            raise TypeCannotBeInferred(ast)

        # lhs and rhs is Array  a[1], b[1] --> a=b
        if type(lhs) is list and len(lhs)==2 and type(rhs) is list and len(rhs)==2 and type(lhs[1]) is ArrayType and type(rhs[1]) is ArrayType:
            if lhs[1].dimen != rhs[1].dimen:
                raise TypeMismatchInStatement(ast)
            if type(lhs[1].eletype) is Unknown and type(rhs[1].eletype) is Unknown:
                raise TypeCannotBeInferred(ast)
            if type(lhs[1].eletype) is not Unknown and type(rhs[1].eletype) is Unknown:
                rhs[1].eletype = lhs[1].eletype
            if type(lhs[1].eletype) is Unknown and type(rhs[1].eletype) is not Unknown:
                lhs[1].eletype = rhs[1].eletype
            return

        # rhs is func cell
        if type(rhs) is list and type(rhs[0]) is int:
            rindex = rhs[0]
            rtype = c[rindex].mtype.restype.eletype
            rkind = 'funccell'
        # rhs is array cell
        elif type(rhs) is list and rhs[1]=='arraytype':
            rtype=rhs[0][1].eletype
            rkind='arraytype'
        # rhs is ID
        elif type(rhs) is list and rhs[1]!='arraytype' and rhs[1] != 'funccell':
            rtype=rhs[1]
            if type(rtype) is ArrayType:
                raise TypeMismatchInStatement(ast)
            rkind='ID'
        # rhs is call function
        elif type(rhs) is int:
            rindex=rhs
            rtype=c[rindex].mtype.restype
            rkind='symbol'
        else: # rhs is literal
            rtype=rhs

        if type(lhs) is VoidType or type(rhs) is VoidType:
            raise TypeMismatchInStatement(ast)

        if type(ltype) is Unknown and type(rtype) is Unknown:
            raise TypeCannotBeInferred(ast)
        elif type(ltype) is Unknown and type(rtype) is not Unknown:
            if lkind=='ID':
                lhs[1]=rtype
            elif lkind=='arraytype':
                lhs[0][1].eletype=rtype
            elif lkind=='funccell':
                c[lindex].mtype.restype.eletype = rtype
        elif type(ltype) is not Unknown and type(rtype) is Unknown:
            if rkind == 'ID':
                rhs[1] = ltype
            elif rkind == 'symbol':
                c[rindex].mtype.restype = ltype
            elif rkind == 'arraytype':
                rhs[0][1].eletype=ltype
            elif rkind=='funccell':
                c[rindex].mtype.restype.eletype = ltype
        elif type(ltype) is not type(rtype):
            raise TypeMismatchInStatement(ast)

    def visitReturn(self,ast,c):
        if type(ast.expr) is type(None):
            return VoidType(),None

        exp=self.visit(ast.expr,c)

        if exp == 'error':
            raise TypeCannotBeInferred(ast)
        # exp is ID
        if type(exp) is list and exp[1]!='arraytype' and exp[1] != 'funccell':
            return exp[1],[exp]
        # exp is call function
        elif type(exp) is int:
            return c[exp].mtype.restype,[exp]
        # exp is array type
        elif type(exp) is list and exp[1]=='arraytype':
            return exp[0][1].eletype,[exp]
        # exp is func cell
        elif type(exp) is list and type(exp[0]) is int:
            index=exp[0]
            return c[index].mtype.restype.eletype,[exp]
        # literal
        else: return exp,None

    def checkType(self,exp,typeCheck,c):
        #========
        if type(exp) is CallExpr:
            for x in c:
                if isinstance(x,Symbol) and x.name==exp.method.name:
                    texp = x.mtype.restype
                    if type(texp) is Unknown:
                        x.mtype.restype = typeCheck
                elif not isinstance(x,Symbol) and x[0]==exp.method.name:
                    raise Undeclared(Function(),exp.method.name)
        #========
        exp = self.visit(exp,c)
        if exp == 'error':
            return 'error'
        # exp is func cell
        if type(exp) is list and type(exp[0]) is int:
            index = exp[0]
            texp = c[index].mtype.restype.eletype
            kind = 'funccell'
        # exp is arraytype
        elif type(exp) is list and exp[1] == 'arraytype':
            texp = exp[0][1].eletype
            kind = 'arraytype'
        elif type(exp) is list and exp[1] != 'arraytype' and exp[1] != 'funccell':  # exp is ID
            texp = exp[1]
            kind = 'ID'
        elif type(exp) is IntType or type(exp) is FloatType or type(exp) is StringType or type(exp) is ArrayType or type(exp) is BoolType:
            if type(exp) is not type(typeCheck):
                return 'NO'
            elif type(exp) is type(typeCheck):
                return 'YES'
        elif type(exp) is int:  # exp is call function
            index = exp
            texp = c[index].mtype.restype
            if type(texp) is VoidType:
                return 'NO'
            kind = 'symbol'

        if type(texp) is not type(typeCheck):
            if type(texp) is Unknown:
                if kind=='ID':
                    exp[1]=typeCheck
                elif kind=='symbol':
                    c[index].mtype.restype=typeCheck
                elif kind == 'arraytype':
                    exp[0][1].eletype = typeCheck
                elif kind == 'funccell':
                    c[index].mtype.restype.eletype= typeCheck
                return 'YES'
            else: return 'NO'
        else: return 'YES'

    def returnInStmt(self,treturn,x,exp,lst,name):
        index = -1
        for i in range(len(lst)):
            if isinstance(lst[i],Symbol) and lst[i].name == name:
                index = i

        if type(lst[index].mtype.restype) is Unknown and type(treturn) is Unknown:
            raise TypeCannotBeInferred(x)
        elif type(lst[index].mtype.restype) is Unknown and type(treturn) is not Unknown:
                lst[index].mtype.restype = treturn
        elif type(lst[index].mtype.restype) is not Unknown and type(treturn) is not Unknown and type(lst[index].mtype.restype) is not type(treturn):
            raise TypeMismatchInStatement(x)
        elif type(lst[index].mtype.restype) is not Unknown and type(treturn) is Unknown and type(exp) is list:
            # exp is ID
            if type(exp[0]) is list and exp[0][1] != 'arraytype' and exp[0][1] != 'funccell':
                exp[0][1] = lst[index].mtype.restype
            # exp is func call
            elif type(exp[0]) is int:
                lst[exp[0]].mtype.restype = lst[index].mtype.restype
            # exp is func cell
            elif type(exp[0]) is list and exp[0][1] == 'funccell':
                lst[exp[0][0]].mtype.restype = lst[index].mtype.restype
            # exp is array type
            elif type(exp[0]) is list and exp[0][1] == 'arraytype':
                exp[0][0][1].eletype = lst[index].mtype.restype

    def visitIf(self,ast,c):
        # ifthenStmt: List[Tuple[Expr, List[VarDecl], List[Stmt]]]
        # elseStmt: Tuple[List[VarDecl], List[Stmt]]
        namefunc = c[len(c) - 1]
        for x in ast.ifthenStmt:
            lst = []
            # exp=self.visit(x[0],c)
            str=self.checkType(x[0],BoolType(),c)
            if str == 'NO':
                raise TypeMismatchInStatement(ast)
            elif str == 'error':
                raise TypeCannotBeInferred(ast)
            else:
                # var decl in if_then
                for y in x[1]:
                    lst += [self.visit(y, lst)]
                lst += c
                # stmt in if_then
                for z in x[2]:
                    if type(z) is Return:
                        treturn, exp = self.visit(z, lst)
                        self.returnInStmt(treturn,z,exp,lst,namefunc)
                    else: self.visit(z, lst)
        # else stmt
        lst_else=[]
        if len(ast.elseStmt)>0:
            # var decl in else stmt
            for x in ast.elseStmt[0]:
                lst_else += [self.visit(x,lst_else)]
            lst_else += lst
            # stmt in else stmt
            for x in ast.elseStmt[1]:
                if type(x) is Return:
                    treturn, exp = self.visit(x, lst_else)
                    self.returnInStmt(treturn, x, exp, lst_else, namefunc)
                else:
                    self.visit(x, lst_else)

    def visitCallStmt(self,ast,c):
        flag = False  # function is declared???
        idx = -1
        for i in range(len(c)):
            if isinstance(c[i], Symbol) and c[i].name == ast.method.name:
                idx = i
                flag = True
                break
            elif not isinstance(c[i], Symbol) and c[i][0] == ast.method.name:
                idx = -10
                break
        # name method is name variable
        if idx == -10:
            raise Undeclared(Function(), ast.method.name)
        # function isn't declared
        if flag == False:
            raise Undeclared(Function(), ast.method.name)
        # check restype function
        if type(c[idx].mtype.restype) is Unknown:
            c[idx].mtype.restype = VoidType()
        if type(c[idx].mtype.restype) is not VoidType:
            raise TypeMismatchInStatement(ast)
        # check param
        if len(ast.param) != len(c[idx].mtype.intype):
            raise TypeMismatchInStatement(ast)
        # check type param
        arg = ast.param
        typeparam = c[idx].mtype.intype  # typeparam is list[type] and use typeparam to update c

        for i in range(len(arg)):
            # get type argument
            # ===============
            if type(arg[i]) is CallExpr:
                for x in c:
                    if isinstance(x, Symbol) and x.name == arg[i].method.name:
                        texp = x.mtype.restype
                        if type(texp) is Unknown and type(typeparam[i]) is Unknown:
                            return 'error'
                        elif type(texp) is not Unknown and type(typeparam[i]) is Unknown:
                            typeparam[i] = texp
                        elif type(texp) is Unknown and type(typeparam[i]) is not Unknown:
                            x.mtype.restype = typeparam[i]
                        elif type(texp) is not type(typeparam[i]):
                            raise TypeMismatchInExpression(arg[i])
                        break
                    elif not isinstance(x, Symbol) and x[0] == arg[i].method.name:
                        raise Undeclared(Function(), arg[i].method.name)
            # ===============
            exp = self.visit(arg[i], c)
            # if type(exp) is VoidType:
            #     raise TypeMismatchInExpression(ast)
            if exp == 'error':
                return 'error'
            # exp is func cell
            if type(exp) is list and type(exp[0]) is int:
                index = exp[0]
                texp = c[index].mtype.restype.eletype
                kind = 'funccell'
            # exp is arraytype
            elif type(exp) is list and exp[1] == 'arraytype':
                texp = exp[0][1].eletype
                kind = 'arraytype'
            elif type(exp) is list and exp[1] != 'arraytype' and exp[1] != 'funccell':  # exp is ID
                texp = exp[1]
                kind = 'ID'
            elif type(exp) is IntType or type(exp) is FloatType or type(exp) is StringType or type(
                    exp) is BoolType or type(exp) is ArrayType:
                texp = exp
            elif type(exp) is int:  # exp is call function
                index = exp
                texp = c[index].mtype.restype
                # if type(texp) is VoidType:
                #     raise TypeMismatchInStatement(ast)
                kind = 'symbol'

            if type(texp) is Unknown and type(typeparam[i]) is Unknown:
                return 'error'
            elif type(texp) is Unknown and type(typeparam[i]) is not Unknown:
                if kind == 'ID':
                    exp[1] = typeparam[i]
                elif kind == 'symbol':
                    c[index].mtype.restype = typeparam[i]
                elif kind == 'arraytype':
                    exp[0][1].eletype = typeparam[i]
                elif kind == 'funccell':
                    c[index].mtype.restype.eletype = typeparam[i]
            elif type(texp) is not Unknown and type(typeparam[i]) is Unknown:
                typeparam[i] = texp
            elif type(texp) is not type(typeparam[i]):
                raise TypeMismatchInStatement(ast)
        # update c
        c[idx].mtype.intype = typeparam

    def visitFor(self,ast,c):
        # index_var = self.visit(ast.idx1,c)
        # check index variable
        str = self.checkType(ast.idx1, IntType(), c)
        if str == 'NO':
            raise TypeMismatchInStatement(ast)
        elif str == 'error':
            raise TypeCannotBeInferred(ast)
        # check exp1
        # exp1 = self.visit(ast.expr1,c)
        str = self.checkType(ast.expr1, IntType(), c)
        if str == 'NO':
            raise TypeMismatchInStatement(ast)
        elif str == 'error':
            raise TypeCannotBeInferred(ast)
        # check exp3
        # exp3 = self.visit(ast.expr3,c)
        str = self.checkType(ast.expr3, IntType(), c)
        if str == 'NO':
            raise TypeMismatchInStatement(ast)
        elif str == 'error':
            raise TypeCannotBeInferred(ast)
        # check exp2
        # exp2 = self.visit(ast.expr2,c)
        str = self.checkType(ast.expr2, BoolType(), c)
        if str == 'NO':
            raise TypeMismatchInStatement(ast)
        elif str == 'error':
            raise TypeCannotBeInferred(ast)
        # loop
        lst = []
        namefunc = c[len(c) - 1]
        for x in ast.loop[0]:       # declared variable
            lst+=[self.visit(x,lst)]
        lst += c
        for x in ast.loop[1]:
            if type(x) is Return:
                treturn,exp = self.visit(x,lst)
                self.returnInStmt(treturn,x,exp,lst,namefunc)
            else:
                self.visit(x,lst)

    def visitDowhile(self,ast,c):
        # sl: Tuple[List[VarDecl], List[Stmt]]
        # exp: Expr
        lst = []
        namefunc = c[len(c) - 1]
        for x in ast.sl[0]:   # declared variable
            lst += [self.visit(x,lst)]
        lst += c
        for x in ast.sl[1]:
            if type(x) is Return:
                treturn,exp = self.visit(x,lst)
                self.returnInStmt(treturn,x,exp,lst,namefunc)
            else:
                self.visit(x,lst)
        # check expr
        # exp = self.visit(ast.exp, lst)
        str = self.checkType(ast.exp, BoolType(), lst)
        if str == 'NO':
            raise TypeMismatchInStatement(ast)
        elif str == 'error':
            raise TypeCannotBeInferred(ast)

    def visitWhile(self,ast,c):
        # exp: Expr
        # sl: Tuple[List[VarDecl], List[Stmt]]
        # check expr
        # exp = self.visit(ast.exp, c)
        str = self.checkType(ast.exp, BoolType(), c)
        if str == 'NO':
            raise TypeMismatchInStatement(ast)
        elif str == 'error':
            raise TypeCannotBeInferred(ast)
        lst = []
        namefunc = c[len(c) - 1]
        for x in ast.sl[0]:  # declared variable
            lst += [self.visit(x, lst)]
        lst += c
        for x in ast.sl[1]:
            if type(x) is Return:
                treturn, exp = self.visit(x, lst)
                self.returnInStmt(treturn, x, exp, lst, namefunc)
            else:
                self.visit(x, lst)

    def visitContinue(self,ast,c): pass
    def visitBreak(self,ast,c): pass

    # Literal

    def visitIntLiteral(self,ast,c):
        return IntType()

    def visitFloatLiteral(self,ast,c):
        return FloatType()

    def visitStringLiteral(self,ast,c):
        return StringType()

    def visitBooleanLiteral(self,ast,c):
        return BoolType()

    def visitArrayLiteral(self,ast,c):
        if type(ast.value[0]) is not ArrayLiteral:
            return ArrayType([len(ast.value)], self.visit(ast.value[0], c))
        else:
            return ArrayType([len(ast.value)] + self.visit(ast.value[0], c).dimen, self.visit(ast.value[0], c).eletype)
