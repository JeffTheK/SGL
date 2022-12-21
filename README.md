# SGL

Lisp lije programming language

## Commands

### Main

|Syntax|Description|
|---|---|
|`(program EXPR...)`|Evaluates all EXPR|
|`(if CONDITION ON_TRUE ON_FALSE)`|Tests CONDITION when true evaluates ON_TRUE else evaluates ON_FALSE|
|`(let NAME VALUE)`|Creates variable named NAME with value VALUE or assigns a value to already created NAME|
|`(print ARGS...)`| Outputs ARGS |
|`(type ARG)`| Returns type as string of ARG |

### Operators

|Syntax|Description|
|------|-----------|
|`(== A B)`| Returns bool whether A is equal B |
|`(!= A B)`| Returns bool whether A is NOT equal to B |
|`(not EXPR)`| Negates EXPR expression |
|`(or EXPR1 EXPR2)`| Returns bool whether EXPR1 or EXPR2 evalutes to true |
|`(and EXPR1 EXPR2)`| Returns bool whether EXPR1 AND EXPR2 evaluate to true |
|`(> A B)`| Returns whether A is greater then B |
|`(< A B)`| Returns whether A is less then B |
|`(+ A B)`| Returns A plus B |
|`(- A B)`| Returns A minus B |
|`(* A B)`| Returns A multiplied by B |
|`(/ A B)`| Returns A divided by B |

### List

|Syntax|Description|
|------|-----------|
|`(new-list ELEMENTS...)`| Creates new List with ELEMENTS as elements|
|`(elem-at INDEX LIST)`| Returns element at INDEX of LIST|
|`(pop-at INDEX LIST)`| Removes and returns element at INDEX of LIST|
|`(clear LIST`)| Removes all elements of LIST|
|`(len LIST)`| Returns length of LIST|
|`(for-each ITERATOR LIST EXPR`)| Evaluates EXPR for each element stored in ITERATOR in LIST |