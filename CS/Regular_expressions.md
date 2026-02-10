# Regular expressions

- Regular expressions are patterns used to specify a set of
  strings.
- Regular expressions are used for:
    - Finding particular words in a stream,
    - Finding combinations of characters in strings,
    - Defining a set of acceptable string in a language.
- They are not are no equivelemnt to wildcards, that you may
  have used before such as 'd*g' which matched 'dog', 'dig, 
  and 'dug'.

- S = set that begins with 'a' and is followed by 

# Notation
- Precedence rules (), *, +, ?, |

- Members side by side must apear in that sequence
- | = Seperates alternatives (or)
- * = Indicates that there are 0 or more of the preceding 
      element.
- + = Indicates that there is 1 or more of the preceding 
      element.
- ? = Indicates that there are 0 or 1 of the preceding 
      element.
- () = Used to identify groupings.

# Character sets
- [abc] = a or b or c
- [0-9] = any number
- [A-Z] = any capital leter

- a{3}


exactly 'aaa'
- a{2,4} = aa, aaa, aaaa

# Start and end rules
- ^cat = must start with cat
- dog$ = must end with dog
- ^cat$ = only 'cat' allowed

# Useful shortcuts
- col(o|ou)r
- a*b+

# Regular languages
- A language is regular if it can be represented by:
    - A regular expression,
    - A finite state machine (FSM).




