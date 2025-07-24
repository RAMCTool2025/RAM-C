# RAM-C


RAM-C (Register-Automaton Model Checker) is a tool that model checks a (fresh)-register automaton against a Fresh HML (μFHML) formula. 


## Requirements


The following is needed in order to run RAM-C:

- Python (3.10+)
- The Oink tool by Tom van Dijk (https://github.com/trolando/oink)

## Setup


Before running the tool, it is necessary to install Oink locally on your machine and copy the binary (named `oink`) into the `oink_bin` folder. The instructions for doing so can be found at https://github.com/trolando/oink. 

## Usage


To run the tool, please use the following command:

`python run.py <FRA_File> <formula_file>`

Where

 - <FRA_File> is the path to the input fresh-register automaton (given as an XML file)
 - <formula_file> is the path to the Fresh muHML formula, given as per the grammar below

For the (fresh)-register automaton file, the XML file should have as root a <register-automaton> element, with the following child elements:
 
 - `<states>`
 - `<initial-state>`
 - `<transitions>`
 - `<final-state>`
 
In the `<states>` element, you can declare many states, where each state is of the form:
```xml
<state>
    <id>{state_name}</id>
    <available-registers>
        <register>{i}</register>
        <register>{j}</register>
        ...
    </available-registers>
</state>
```

The initial state is simply of the form:

```xml
<initial-state>{state_name}</initial-state>
```

And similarly for each final-state:
```xml
<final-state>{state_name}</final-state>
```

As for `<transitions>`, this will contain one child element for each transition of the form:
```xml
<transition>
    <from>{source state}</from>
    <input>{transition tag}</input>
    <op>{LFresh, GFresh, or Stored}</op>
    <register>{i}</register>
    <to>{target state}</to>
</transition> 
```
where

- `Stored` represents a Known transition,
- `LFresh` represents a Locally-fresh transition,
- `GFresh` represents a Globally-fresh transition.

Note that the input element for each transition is optional. 

As for the muHML formula, this can be stored in a text file that adheres to the following grammar:

```antlrv4

formula
    : '(' formula ')'                               # parens
    | '[' term '=' term ']'                         # eq
    | '[' term '≠' term ']'                         # neq
    | '⟨' label '⟩' formula                         # diamond
    | '<' label '>' formula                         # diamond2
    | '[' label ']' formula                         # box
    | '⋁' ID '.' formula                            # bigOr
    | '⋀' ID '.' formula                            # bigAnd
    | 'И' ID '.' formula                            # fresh
    | '\\OR' ID '.' formula                         # bigOr2
    | '\\AND' ID '.' formula                        # bigAnd2
    | '\\NEW' ID '.' formula                        # fresh2
    | var                                           # recVar
    | '(' formula '∨' formula ')'                   # or
    | '(' formula '∧' formula ')'                   # and
    | '(' formula '\\or' formula ')'                # or2
    | '(' formula '\\and' formula ')'               # and2
    | '(' 'μ' var '.' formula ')' '(' args ')'      # mu
    | '(' 'ν' var '.' formula ')' '(' args ')'      # nu
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

```