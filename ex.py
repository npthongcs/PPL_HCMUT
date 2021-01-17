class StaticCheck(Visitor):
    def visitProgram(self, ctx: Program, o: object):
        declared = ([], 0)
        for decl in ctx.decl:
            if type(decl) == VarDecl:
                self.visitVarDecl(decl, declared)
            elif type(decl) == ConstDecl:
                self.visitConstDecl(decl, declared)
            elif type(decl) == FuncDecl:
                self.visitFuncDecl(decl, declared)

    def visitVarDecl(self, ctx: VarDecl, o: object):
        current_scope = o[1]
        if [ctx.name, current_scope] in o[0]:
            raise RedeclaredVariable(ctx.name)
        else:
            o[0].append([ctx.name, current_scope])

    def visitConstDecl(self, ctx: ConstDecl, o: object):
        current_scope = o[1]
        if [ctx.name, current_scope] in o[0]:
            raise RedeclaredConstant(ctx.name)
        else:
            o[0].append([ctx.name, current_scope])

    def visitFuncDecl(self, ctx: FuncDecl, o: object):
        current_scope = o[1]
        if [ctx.name, current_scope] in o[0]:
            raise RedeclaredFunction(ctx.name)
        else:
            o[0].append([ctx.name, current_scope])
            body_declared = (list(map(lambda x: x.copy(), o[0])), (current_scope + 1))
            for i in ctx.param:
                self.visitVarDecl(i, body_declared)

            for decl in ctx.body[0]:
                if type(decl) == VarDecl:
                    self.visitVarDecl(decl, body_declared)
                elif type(decl) == ConstDecl:
                    self.visitConstDecl(decl, body_declared)
                elif type(decl) == FuncDecl:
                    self.visitFuncDecl(decl, body_declared)

            for decl in ctx.body[1]:
                if type(decl) == Id:
                    self.visitId(decl, body_declared)

    def visitIntType(self, ctx: IntType, o: object):
        return

    def visitFloatType(self, ctx: FloatType, o: object):
        return

    def visitIntLit(self, ctx: IntLit, o: object):
        return

    def visitId(self, ctx: Id, o: object):
        if len(list(filter(lambda x: x[0] == ctx.name, o[0]))) == 0:
            raise UndeclaredIdentifier(ctx.name)