class ASTGeneration(MPVisitor):
    
    def visitProgram(self,ctx:MPParser.ProgramContext): 
        return self.visit(ctx.vardecls())
# vardecls: vardecl vardecltail;
    def visitVardecls(self,ctx:MPParser.VardeclsContext):
        return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())
# vardecltail: vardecl vardecltail | ;
    def visitVardecltail(self,ctx:MPParser.VardecltailContext): 
        if ctx.getChildCount()==2:
            return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())
        else: return []
# vardecl: mptype ids ';' ;       
    def visitVardecl(self,ctx:MPParser.VardeclContext): 
        ids = self.visit(ctx.ids())
        return [VarDecl(x,self.visit(ctx.mptype())) for x in ids]
# mptype: INTTYPE | FLOATTYPE;
    def visitMptype(self,ctx:MPParser.MptypeContext):
        return IntType() if ctx.INTTYPE() else FloatType()
# ids: ID ',' ids | ID; 
    def visitIds(self,ctx:MPParser.IdsContext):
        return [Id(str(ctx.ID()))] if ctx.getChildCount()==1 else [Id(str(ctx.ID()))] + self.visitIds(ctx.ids())