class ASTGeneration(MPVisitor):
    # program: vardecls EOF;
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return self.visit(ctx.vardecls())
    # vardecls: vardecl vardecltail;
    def visitVardecls(self,ctx:MPParser.VardeclsContext):
        return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())
    # vardecltail: vardecl vardecltail | ;
    def visitVardecltail(self,ctx:MPParser.VardecltailContext):
        if ctx.vardecl():
            return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())
        return []
    # vardecl: mptype ids ';' ;
    def visitVardecl(self,ctx:MPParser.VardeclContext):
        mptype = self.visit(ctx.mptype())
        ids = self.visit(ctx.ids())
        listVar = []
        for i in ids:
            listVar.append(VarDecl(i,mptype))
        return listVar


    # mptype: INTTYPE | FLOATTYPE;
    def visitMptype(self,ctx:MPParser.MptypeContext):
        if ctx.INTTYPE():
            return IntType()
        return FloatType()
    # ids: ID ',' ids | ID;
    def visitIds(self,ctx:MPParser.IdsContext):
        if ctx.ids():
            return [Id(str(ctx.ID()))] + self.visitIds(ctx.ids())
        return [Id(str(ctx.ID()))]