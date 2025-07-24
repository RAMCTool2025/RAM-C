grammar Logic;

formula
    : '(' formula ')'                   # parens
    | '[' term '=' term ']'             # eq
    | '[' term '≠' term ']'             # neq
    | '⟨' label '⟩' formula             # diamond
    | '<' label '>' formula             # diamond2
    | '[' label ']' formula             # box
    | '⋁' ID '.' formula                # bigOr
    | '⋀' ID '.' formula                # bigAnd
    | 'И' ID '.' formula                # fresh
    | '\\OR' ID '.' formula             # bigOr2
    | '\\AND' ID '.' formula            # bigAnd2
    | '\\NEW' ID '.' formula            # fresh2
    | var                               # recVar
    | '(' formula '∨' formula ')'       # or
    | '(' formula '∧' formula ')'       # and
    | '(' formula '\\or' formula ')'     # or2
    | '(' formula '\\and' formula ')'    # and2
    | '(' 'μ' var '.' formula ')' '(' args ')'     # mu
    | '(' 'ν' var '.' formula ')' '(' args ')'     # nu
    | '(' '\\mu' var '.' formula ')' '(' args ')'   # mu2
    | '(' '\\nu' var '.' formula ')' '(' args ')'   # nu2
    ;

label
    : term
    | term ',' term
    ;

args
    : (term (',' term)*)?
    ;

term
    : ID
    | NUMBER
    | '*'
    ;

var
    : ID '(' args ')'
    ;

ID: [a-zA-Z_][a-zA-Z_0-9]*;
NUMBER: '-'?[0-9]+;
WS: [ \t\r\n]+ -> skip;
