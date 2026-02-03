# The turing machine:

- A turing machine can be viewed as a computer with a single
  fixed program, expressed using:
    - A finite set of states in a state transition diagram
    - A finite alphabet of symbols
    - An infinite tape with marked off squares
    - A sensing read-write head that can travel along the
      tape, one square at a time

- A turing machine consists of 2 parts, the tape that the 
  machine can read and write, and the controller (the program)
  determines what happens at each cell.
    - It has a read-write head that can read symbols
      from the tape,
    - The tape is infinitely long, with marked-off squares.

- The machine must have a start state and at least 1 state,
  the halting state, that causes it to half for some inputs.
- Any alphabet of symbols may be used but we will generally
  use only a binary alphabet (and blanks).

## Transition function
- A transition function is a way to represent the transition 
  arc between two states on a stable transition diagram.
- The symbol δ is the lower case Greek letter delta.
  - It means a small change.
- Each transition arc ona state transition diagram can be
  represented by the δ function using a pattern:
  - δ (Current state, Input symbol) = (Next state, Output
    symbol, Head move)

## δ Function - interpretation
- δ (S0, 1) = (S1, 0, L)
  - "If the machine is currently in state S0 and the symbol
    is 1 is read from the tape, then transition to state S1,
    write 0 on the tape, and move head left".

## The importance of the TM
- It provides a defenition for what is computable
- It can be proven mathematically that a Turing Machine is
  capable of computing anything that is computable.

## Universal turing machine
- The universal turing machine reads from a tape:
  - The definition of a turing machine T (i.e the program)
  - The input data D
- In this way, the universal turing machine simulates the
  behaviour of any turing machine.

## Importance
- The theory of the universal turing machine is very important
  to the subject of computation
- It provides a definition of what is computable
- It ccan be proven mathematically that a Universal TM is
  capable of computing anything that is computable,

δ (S0, 0) = (S1,  , R)
δ (S0, 1) = (S1,  , R)
δ (S0,  ) = (S6,  , L)
δ (S1, 0) = (S1, 0, R)
δ (S1, 1) = (S1, 1, R)
δ (S1,  ) = (S2,  , L)
δ (S2, 0) = (S3,  , L)
δ (S2, 1) = (S4,  , L)
δ (S2,  ) = (S6,  , L)
δ (S3, 0) = (S3, 0, L)
δ (S3, 1) = (S4, 0, L)
δ (S3,  ) = (S5, 0, R)
δ (S4, 0) = (S3, 1, L)
δ (S4, 1) = (S4, 1, L)
δ (S4,  ) = (S5, 1, R)

a. 
b. It loops if it finds a 1, until it finds a blank, then it 
    goes back to the 1s. If it doesn't find a 1 it won't 
    continue.
b. A universal turing machine reads from the tape the 
   definition of the machine T and input data D.




