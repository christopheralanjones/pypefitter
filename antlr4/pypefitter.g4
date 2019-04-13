grammar pypefitter;

/*
** PIPELINE
*/
pypefitter
    : PYPEFITTER LBRACE RBRACE
    ;

/*
** KEYWORDS
*/
PYPEFITTER : 'pypefitter';


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
** WHITESPACE AND COMMENTS
*/
WS  :  [ \t\r\n\u000C]+ -> skip
    ;

COMMENT
    : '#' ~[\r\n\f]* -> channel(HIDDEN)
    ;
