grammar Pypefitter;


/*
** PIPELINE
*/
pypefitter
    : PYPEFITTER stage_body
    ;

event_decl
    : event_name event_condition_decl? event_action
    ;

event_action
    : FSLASH action=Identifier
    ;

event_condition_decl
    : LBRACK  event_condition RBRACK
    ;

event_condition
    : name=FAILURE
    | name=SUCCESS
    ;

event_name
    : name=ON_ENTER
    | name=ON_EXIT
    ;

stage
    : STAGE stage_body
    ;

stage_body
    : name=Identifier LBRACE event_decl* stage* RBRACE
    ;



/*
** KEYWORDS
*/
FAILURE : 'failure';
ON_ENTER : 'on_enter';
ON_EXIT : 'on_exit';
PYPEFITTER : 'pypefitter';
STAGE : 'stage';
SUCCESS : 'success';


/*
** SEPARATORS
*/
LPAREN : '(';
RPAREN : ')';
LBRACE : '{';
RBRACE : '}';
LBRACK : '[';
RBRACK : ']';
SEMI   : ';';
COMMA  : ',';
DOT    : '.';
FSLASH : '/';


/*
** IDENTIFIERS
*/
Identifier
	:	Letter LetterOrDigit*
	;

fragment
Letter
	:	[a-zA-Z_]
	;

fragment
LetterOrDigit
	:	[a-zA-Z0-9_]
	;


/*
** STRINGS
*/

StringLiteral
	:	'"' StringCharacters? '"'
	;

fragment
StringCharacters
	:	StringCharacter+
	;

fragment
StringCharacter
	:	~["\\\r\n]
	|	EscapeSequence
	;

fragment
EscapeSequence
	:	'\\' [btnfr"'\\]
	;


/*
** WHITESPACE AND COMMENTS
*/
WS  :  [ \t\r\n\u000C]+ -> skip
    ;

COMMENT
    : '#' ~[\r\n\f]* -> channel(HIDDEN)
    ;
