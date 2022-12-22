# SGL

Lisp like programming language

## Installation

* `git clone https://github.com/JeffTheK/SGL/.git`
* `cd SGL`
* `make install`
* Thats all, now you can execute sgl file by running `sgl FILE_NAME`

## Types

|Name|Description|
|---|---|
|`Symbol`| A word that starts with ascii characters, can include symbols like `-` `:` |
|`Number`| An integer or float |
|`List`| A collection of elements with any type |
|`String`| Collection of characters |
|`Atom`| An Atom is either Symbol, Number, List or String |
|`Expression`| A Symbol followed by zero or more Atoms enclosed in braces |

## Commands

### Main

|Syntax|Description|
|---|---|
|`(program EXPR...)`|Evaluates all EXPR|
|`(if CONDITION ON_TRUE ON_FALSE)`|Tests CONDITION when true evaluates ON_TRUE else evaluates ON_FALSE|
|`(let NAME VALUE)`|Creates variable named NAME with value VALUE or assigns a value to already created NAME|
|`(print ARGS...)`| Outputs ARGS |
|`(type ARG)`| Returns type as string of ARG |
|`(func NAME EXPR...)` | Defines new function named NAME with EXPR... as body. Returns last expression as result |

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
|`(insert INDEX VALUE LIST)` | Inserts VALUE at INDEX in LIST |

### String

|Syntax|Description|
|------|-----------|
|`(quote EXPR...)`| Returns EXPR as string without evaluating them |