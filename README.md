# CODE CHALLENGE
TR CLONE: https://codingchallenges.substack.com/p/coding-challenge-43-tr

# APPROACH
As we can see some usage examples that we can use with the `tr` command are `tr A-Z a-z`, `tr A-Z"[:digit:]" a-z`

So in order to create this characters range to parse one to another we instead of falling to the if hell loop or trying to make some complex logic we take the approach of creating a new language and for that we need a grammar

## GRAMMAR

```bash
S -> S TOKEN |  TOKEN | ε

TOKEN -> " [ : CLASSNAME : ] " | CHAR CONT 

CONT -> - CHAR | ε

CHAR -> a | b | c | d | e | f | g | h | i | j | k | l |
 m | n | o | p | q | r | s | t | u | v | w | x | y | z |
  A | B | C | D | E | F | G | H | I | J | K | L | M | 
  N | O | P | Q | R | S | T | U | V | W | X | Y | Z | 
  0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9

CLASSNAME -> alnum | alpha | blank | cntrl | digit | 
lower |print | punct | rune | space | special | upper
```
NOTE: `ε` represents no entry/input

As we are using Python we are going to use the SLY module which let us to create a Lexer and a Parser.
