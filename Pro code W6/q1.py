class ASTGeneration(MPVisitor):
    
    def visitProgram(self,ctx:MPParser.ProgramContext):

        return 1 + self.visit(ctx.vardecls())

    def visitVardecls(self,ctx:MPParser.VardeclsContext):

        return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())

    def visitVardecltail(self,ctx:MPParser.VardecltailContext): 

        if (ctx.getChildCount()==2): return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())
        else: return 0

    def visitVardecl(self,ctx:MPParser.VardeclContext): 
        return 1 + self.visit(ctx.mptype()) + self.visit(ctx.ids())

    def visitMptype(self,ctx:MPParser.MptypeContext):

        return 1;

    def visitIds(self,ctx:MPParser.IdsContext):
        if (ctx.getChildCount()==1): return 1
        else: return 2 + self.visit(ctx.ids())
        