grammar Pypefitter;

/*
** PIPELINE
*/
pypefitter
    : PYPEFITTER name=Identifier LBRACE stage* RBRACE
    ;

/*
** STAGES
*/
stage
    : STAGE stage_body
    ;

stage_body
    : name=Identifier LBRACE stage* RBRACE
    ;


/*
** KEYWORDS
*/
PYPEFITTER : 'pypefitter';
STAGE : 'stage';


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
