# Reverse polish notation

Infix: The operator comes between the operands. This is the 
notation you've encountered before.

Prefix (Polish notation) : The operator comes before the 
operands. This was invented in 1924 by Polish mathematician 
Jan Lukasiewicz.


- Postfix (RPN): The operator comes after the operands. During
  the 1950s, Reverse Polish was devised as a way to do 
  mathematics without braces. 
- The system is used extensively in computer algorithms 
  because evaluation can be done using a stack.

## Why we use it?
- Eliminates the need for brackets in sub-expressions as the
  order of evaluation is unambiguous.
- The algorithm for evaluating postfix expressions is simpler
  than infix expressions.
  - The resulting expressions can be evaluated using a stack.

## Order of precedence
- Highest precedence
> ~ (Unary minus; negative; ~4 + 1 = 3)
> ^ (Exponentiation; 3^2 = 9)
> *  /
> + -
> =
- Lowest precedence

## Conversion
- We only need concern ourselves with infix and postfix (RPN)
  conversions.
- Methods for converting infix to RPN:
  - Translating by numbering
  - Translating by bracketing
  - Translation by binary tree
- Methods for converting RPM to infix:
  _ Translating by scanning
  - Translating by bracketing

## Translating by numbering
- This algorithm works by numbering operands and operators.

## Translating by bracketing
- This method works by fully bracketing the expression and 
  rearranging the operators inside the brackets.

## Translation by binary tree
- This method works by building a binary tree from the infix
  expression and then traversing it using a post-order 
  traversal algorithm.

## RPM to infix - Scanning
- This method works by scanning left to right, picking out
  pairs of operands and single operators.
  - Scan right, writing down operands,
  - If you find an operator, insert it between the operands it
    applies to,
  - Add brackets to make clear which operands the operator
    applies to.

## RPN evaluation
- Given an RPN expression, an algorithm can be used to 
  evaluate it to produce a result.
    - This algorithm makes use of a stack.

## RPN evaluation - stack
- This method works pushing and popping operands in response
  to operators:
    - If the token is an operand, push it on the stack,
    - If the tocken is an operator, pop required number of 
      operands from stack; perform the operation; push the
      result.




