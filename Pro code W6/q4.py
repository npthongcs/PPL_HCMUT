class ASTGeneration(MPVisitor):
    
    def toBool(self,x): 
        return x == "True"
    
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return self.visit(ctx.exp())

    def visitExp(self,ctx:MPParser.ExpContext):
        if ctx.getChildCount()==1: return self.visit(ctx.term())
        else: return Binary(ctx.ASSIGN().getText(),self.visit(ctx.term()),self.visit(ctx.exp()))

    def visitTerm(self,ctx:MPParser.TermContext): 
        if ctx.getChildCount()==1: return self.visit(ctx.factor(0))
        else: Binary(ctx.COMPARE().getText(),self.visit(ctx.factor(0)),self.visit(ctx.factor(1)))

    def visitFactor(self,ctx:MPParser.FactorContext):
        if ctx.getChildCount()==1: return self.visit(ctx.operand())
        else: return Binary(ctx.ANDOR().getText(),self.visit(ctx.factor()),self.visit(ctx.operand()))

    def visitOperand(self,ctx:MPParser.OperandContext):
        if ctx.getChildCount()!=1: return self.visit(ctx.exp())
        elif ctx.ID(): return Id(ctx.ID().getText())
        elif ctx.INTLIT(): return IntLiteral(int(ctx.INTLIT().getText()))
        else: return BooleanLiteral(self.toBool(ctx.BOOLIT().getText()))
        
        
        
class ASTGeneration(MPVisitor):
    def toBool(self,x):
        return x == "True"

    def visitProgram(self,ctx:MPParser.ProgramContext):
        return self.visit(ctx.exp())

    def visitExp(self,ctx:MPParser.ExpContext):
        return Binary(ctx.ASSIGN().getText(), self.visit(ctx.term()), self.visit(ctx.exp())) if ctx.exp() else self.visit(ctx.term())

    def visitTerm(self,ctx:MPParser.TermContext): 
        return Binary(ctx.COMPARE().getText(), self.visit(ctx.factor(0)), self.visit(ctx.factor(1))) if ctx.COMPARE() else self.visit(ctx.factor(0))

    def visitFactor(self,ctx:MPParser.FactorContext):
        return Binary(ctx.ANDOR().getText(), self.visit(ctx.factor()), self.visit(ctx.operand())) if ctx.ANDOR() else self.visit(ctx.operand())
  
    def visitOperand(self,ctx:MPParser.OperandContext):
        return Id(ctx.ID().getText()) if ctx.ID() else IntLiteral(int(ctx.INTLIT().getText())) if ctx.INTLIT() else BooleanLiteral(self.toBool(ctx.BOOLIT().getText())) if ctx.BOOLIT() else self.visit(ctx.exp())