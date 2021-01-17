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

program  :  var_decl* func_decl* EOF;

// grammar comment
COMMENT: '**' .*? '**' -> skip;

// grammar declare variable
var_decl: VAR COLON listID SM ;     
listID: typeID (CM typeID)* ;     
typeID: ID | array | init_var;
array: ID dimension ;            
dimension: (LS (INT|HEXA|OCTAL) RS)+ ; // [?][?][?] | [?]
init_var: ID ASS (INT|HEXA|OCTAL|BOOL|STRING|FLOAT|init_array) | array ASS (init_array| INT|HEXA|OCTAL|BOOL|STRING|FLOAT);
unit_array: ((INT|HEXA|OCTAL)|BOOL|STRING|FLOAT) (CM ((INT|HEXA|OCTAL)|BOOL|STRING|FLOAT|))* ;
init_array_: LB unit_array? RB CM init_array_  
            | LB unit_array? RB;
init_array: LB unit_array? RB 
            | LB init_array_ RB;


// grammar declare function
func_decl: FUNCTION COLON ID parameter? BODY COLON var_decl* stm* ENDBODY DOT ;
parameter: PARAMETER COLON (array|ID) (CM (ID|array))* ;

// grammar statement
stm: assign_stm | if_stm | for_smt | while_stm | dowhile_stm | break_stm | continue_stm
        | call_stm | return_stm ;

// grammar assignment statement
assign_stm: ID ASS exp SM 
            | ID (LS exp RS)+ ASS exp SM;
// grammar IF statement
if_stm: IF exp THEN var_decl* stm* (ELSEIF exp THEN var_decl* stm*)* (ELSE var_decl* stm*)? ENDIF DOT;
// grammar FOR statement
for_smt: FOR LP ID ASS exp CM exp CM exp RP DO var_decl* stm* ENDFOR DOT;
// grammar WHILE statement
while_stm: WHILE exp DO var_decl* stm* ENDWHILE DOT;
// grammar DO WHILE statement
dowhile_stm: DO var_decl* stm* WHILE exp ENDDO DOT;
// grammar BREAK statement
break_stm: BREAK SM;
// grammar CONTINUE statement
continue_stm: CONTINUE SM;
// grammar CALL statement
call_stm: ID LP ((exp|STRING) (CM (exp|STRING))*)? RP SM;
// grammar call function
call_func: ID LP ((exp|STRING) (CM (exp|STRING))*)? RP;
// grammar RETURN statement
return_stm: RETURN exp? SM;

// grammar index operator
index_operators: LS exp RS
                | LS exp RS index_operators ;

// grammar expression
exp: exp1 (EQ | NEQ | LESS | GREATER | LEQ | GEQ | NEQF | LESSF | GREATERF | LEQF | GEQF) exp1 | exp1;
exp1: exp1 (AND | OR) exp2 | exp2;
exp2: exp2 (SUB | SUBF | ADD | ADDF) exp3 | exp3;
exp3: exp3 (MUL | MULF | DIV | DIVF | MODUL) exp4 | exp4;
exp4: NOT exp4 | exp5;
exp5: (SUB | SUBF) exp5 | exp6;
exp6: exp6 index_operators | exp7;
exp7: call_func operand | operand;     

// grammar operands
operand: ID | array | call_func | literal| LP exp RP; 
literal: INT|FLOAT|BOOL|HEXA|OCTAL|STRING;

//define fragment
fragment DIGIT: [0-9] ;

// define TOKENS
ID:     [a-z][_A-Za-z0-9]* ;
INT:    '0' | [1-9][0-9]* ;
HEXA:   '0'[xX][1-9A-F][0-9A-F]* ;
OCTAL:  '0'[oO][1-7][0-7]* ;

FLOAT: (DIGIT+) DOT DIGIT* ([Ee][+-]? DIGIT+)?
        | (DIGIT+) ([Ee][+-]? DIGIT+)
        | (DIGIT+) DOT;
STRING: ["] ('\\'[btfrn'\\] | '\'"' | ~('\\' | '"' | '\n' | '\''))* ["] {
     self.text = self.text[1:-1]
};
BOOL:   TRUE | FALSE;

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