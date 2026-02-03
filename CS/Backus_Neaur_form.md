# Backus-Naur Form

- Backus-Naur form (BNF) is a formal notation used to 
  describe the syntax rules of a language.
- It is a meta-language: a language that describes a 
  language.
  - First developed by John Backus (1959),
  - Augmented by Peter Naur (1960).

- Regular languages are expressible by regular expressions.
- Some languages cannot be expressed by a regular expression.
- The class of languages called context-free languages is
  more expressive than regular languages.
- BNF is a way to define these context-free languages.

## BFS vs regular expressions
- Regular expressions can be used to describe simple 
  "languages" and to match patterns in text.

## BNF meta-symbols
- ::=   Is defined as
- <>    Surrounds category names
- |     Or

- BNF is expressed using prodution rules of the form
  <left> ::= right
- BNF contains non-terminal/terminal symbols

## Language representations
- An instruction for a computer must not be ambiguous in any
  way:
  - A programming language requires strict and precise rules,
  - This is why we have not yet been successful at natural
    language processing.
  - BNF can be used by compiler writers to represent the
    precise syntax of a programming language.

## Context free languages
- A context-free language can be defined by BNF when a single
  non-terminal symbol on the left can always be replaced by
  the definition on the right.
- There is no ambiguity in the definiion.

- Each individual BNF statement is called a production rule.

## Recursive production rules
- A recursive rule is defined in terms of itself
- Using recursion allows a set of production rules to be
  extremely concise while allowing an infinite number of items
  to be precisely defined.
- If a production rule has recursion there neds to be a non-
  recursive case.

## Parsing
- The act of parsing is checking an input string against
  the set of BNF rules to see if it is valid
- A compiler or interpreter ecounters an input like (8-(6+4)),
  it validates the input by building a tree according to the
  BNF rules

## Terminal symbols



