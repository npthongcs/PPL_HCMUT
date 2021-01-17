grammar BKIT;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:       
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}

options{
	language=Python3;
}

program: (declare_func | declare_var) * EOF;

declare_var: var_type ID (CM ID)* SM ;
declare_func: var_type ID LP (var_type ID (CM ID)* (SM var_type ID (CM ID)*)*)? RP LB body RB ;
body: (declare_var | call_func | assign | st_return)*;
operands: INTLIT | FLOATLIT | ID | call_func | LP exp RP;
call_func: ID LP (exp (CM exp)*)? RP;
st_return: RETURN exp SM;
assign: ID EQ exp SM;
exp: LP exp RP
    | exp (MUL | DIV) exp
    | operands SUB operands
    | <assoc=right> exp ADD exp
    | operands; 
var_type: INT|FLOAT;

INT : 'int';
FLOAT : 'float';
RETURN : 'return';
LB : '{';
RB : '}';
SM : ';';
CM : ',';
EQ : '=';
LP : '(';
RP : ')';
ADD : '+';
SUB : '-';
MUL : '*';
DIV : '/';
ID : [_a-zA-Z][_a-zA-Z0-9]*;
INTLIT: [1-9][0-9]* | '0';
FLOATLIT: INTLIT ([.][0-9]+)?([Ee][+|-]?[0-9]+)?;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
UNTERMINATED_COMMENT: .;