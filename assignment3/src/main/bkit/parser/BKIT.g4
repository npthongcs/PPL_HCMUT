grammar BKIT;

// ID: 1814205

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

program  : list_var_decl list_func_decl  EOF;
list_var_decl: var_decl list_var_decl
                | var_decl
                |;
list_func_decl: func_decl list_func_decl
                | func_decl
                |;
// grammar comment
COMMENT: '**' .*? '**' -> skip;

// grammar declare variable
var_decl: VAR COLON listID SM ;
listID: typeID CM listID
        | typeID;
typeID: ID | typearray | init_var;
typearray: ID dimension ;
dimension: LS intlit RS dimension
            | LS intlit RS ;
init_var: ID ASS literal
            | ID dimension ASS literal;
unit_array: literal CM unit_array
            | literal ;
array: LB unit_array RB
            | LB RB;

// grammar declare function
func_decl: FUNCTION COLON ID parameter BODY COLON list_var_decl list_stm ENDBODY DOT
           | FUNCTION COLON ID BODY COLON list_var_decl list_stm ENDBODY DOT;
parameter: PARAMETER COLON list_para;
list_para: typePara CM list_para
            | typePara;
typePara: ID | typearray;

// grammar statement
list_stm: stm list_stm
        | stm
        | ;
stm: assign_stm | if_stm | for_stm | while_stm | dowhile_stm | break_stm | continue_stm
        | call_stm | return_stm ;

// grammar assignment statement
assign_stm: lhs ASS exp SM;
lhs: exp6|ID;
// grammar IF statement
if_stm: IF exp THEN list_var_decl list_stm list_elseif else_ ENDIF DOT;
list_elseif: ELSEIF exp THEN list_var_decl list_stm list_elseif
            | ;
else_ : ELSE list_var_decl list_stm
        | ;
// grammar FOR statement
for_stm: FOR LP ID ASS exp CM exp CM exp RP DO list_var_decl list_stm ENDFOR DOT;
// grammar WHILE statement
while_stm: WHILE exp DO list_var_decl list_stm ENDWHILE DOT;
// grammar DO WHILE statement
dowhile_stm: DO list_var_decl list_stm WHILE exp ENDDO DOT;
// grammar BREAK statement
break_stm: BREAK SM;
// grammar CONTINUE statement
continue_stm: CONTINUE SM;
// grammar CALL statement
call_stm: ID LP para_call_stm RP SM
            |  ID LP RP SM;
para_call_stm: exp CM para_call_stm
                | exp;
// grammar call function
call_func: ID LP para_call_func RP
            | ID LP RP;
para_call_func: exp CM para_call_func
                | exp;
// grammar RETURN statement
return_stm: RETURN exp SM
            | RETURN SM;
// grammar index operator
//element_expression: exp index_operators;
index_operators: (LS exp RS)+;
                //|LS exp RS index_operators ;
// grammar expression
exp: exp1 relational exp1 | exp1;
exp1: exp1 (AND | OR) exp2 | exp2;
exp2: exp2 (SUB | SUBF | ADD | ADDF) exp3 | exp3;
exp3: exp3 (MUL | MULF | DIV | DIVF | MODUL) exp4 | exp4;
exp4: NOT exp4 | exp5;
exp5: (SUB | SUBF) exp5 | exp6;
exp6: exp6 index_operators | exp7;
exp7: call_func exp8 | exp8;
exp8: operand;
// grammar operands
operand: ID | literal| LP exp RP | call_func;
literal: FLOAT|bool_literal|DEC|OCTAL|HEXA|STRING|array;
relational: EQ | NEQ | LESS | GREATER | LEQ | GEQ | NEQF | LESSF | GREATERF | LEQF | GEQF;
//define fragment
fragment DIGIT: [0-9] ;

// define TOKEN
ID:     [a-z][_A-Za-z0-9]* ;
intlit: DEC|HEXA|OCTAL;
DEC: '0' | [1-9][0-9]*;
HEXA: '0'[xX][1-9A-F][0-9A-F]*;
OCTAL:'0'[oO][1-7][0-7]* ; // $$$$$$$$$
FLOAT: (DIGIT+) '.' DIGIT* ([Ee][+-]? DIGIT+)?
        | (DIGIT+) ([Ee][+-]? DIGIT+)
        | (DIGIT+) '.';
STRING: ["] ('\\'[btfrn'\\] | '\'"' | ~('\\' | '"' | '\n' | '\''))* ["] {
     self.text = self.text[1:-1]
};
bool_literal:   TRUE | FALSE;

// define KEYWORDS
BODY:       'Body' ;
BREAK:      'Break' ;
CONTINUE:   'Continue' ;
DO:         'Do' ;
ELSE:       'Else' ;
ELSEIF:     'ElseIf' ;
ENDBODY:    'EndBody' ;
ENDIF:      'EndIf' ;
ENDFOR:     'EndFor' ;
ENDWHILE:   'EndWhile' ;
FOR:        'For' ;
FUNCTION:   'Function';
IF:         'If' ;
PARAMETER:  'Parameter' ;
RETURN:     'Return' ;
THEN:       'Then' ;
VAR:        'Var' ;
WHILE:      'While' ;
TRUE:       'True' ;
FALSE:      'False' ;
ENDDO:      'EndDo' ;

//define OPERATORS
ADD:    '+' ;
ADDF:   '+.' ;
SUB:    '-' ;
SUBF:   '-.' ;
MUL:    '*' ;
MULF:   '*.' ;
DIV:    '\\' ;
DIVF:   '\\.' ;
MODUL:  '%' ;
NOT:    '!' ;
AND:    '&&' ;
OR:     '||' ;
EQ:     '==' ;
ASS:    '=' ;
NEQ:   '!=' ;
GREATER:'>' ;
LESS:   '<' ;
GEQ:    '>=' ;
LEQ:    '<=' ;
NEQF:   '=/=' ;
LESSF:  '<.' ;
GREATERF:   '>.' ;
GEQF:   '>=.' ;
LEQF:   '<=.' ;

// define SEPARATORS
LP: '(' ;
RP: ')' ;
LS: '[' ;
RS: ']' ;
LB: '{' ;
RB: '}' ;
COLON: ':' ;
SM: ';' ;
CM: ',' ;
DOT: '.';

WS : [ \t\r\n\f]+ -> skip ; // skip spaces, tabs, newlines

ILLEGAL_ESCAPE: '"' ('\\'[btfrn'\\] | '\'"' | ~('\\' | '"' | '\''))* '\\'~[btfrn'\\] {
    self.text = self.text[1:]
};

UNCLOSE_STRING: '"' ('\\'[btfrn'\\] | '\'"' | ~('\\' | '"' | '\''))* {
    self.text = self.text[1:]
};

UNTERMINATED_COMMENT: '**' .*?{
    self.text = self.text[1:0]
};

ERROR_CHAR: .{
    self.text=self.text;
};