# CODE CHALLENGE
TR CLONE: https://codingchallenges.substack.com/p/coding-challenge-43-tr

# SETUP
- `python3 -m venv .venv`
- `source .venv/bin/activate`
- `pip3 install -r requirements.txt`
- DONE :)

## Runing tests
We are using unittest module
`python3 -m unittest discover -s tests`

# APPROACH
As we can see some usage examples that we can use with the `tr` command are `tr A-Z a-z`, `tr A-Z"[:digit:]" a-z`

So in order to create this characters range to parse one to another we instead of falling to the if hell loop or trying to make some complex logic we take the approach of creating a new language and for that we need a grammar

## GRAMMAR

```bash
S -> S TOKEN |  TOKEN | ε

TOKEN -> [ : CLASSNAME : ] | CHAR CONT 

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

## STEPS

### STEP 1
In this step your goal is to support translating from one character to another, when reading from the standard input. For this your program should start up and wait for a line of input from the user. It will then output the line having made the substitution specified, for example:

```bash
% cctr c C
coding challenges
Coding Challenges
```
Type CTRL-D to send the EOF and terminate cctr.

```bash
echo coding challenges | python3 main.py c C
```

### STEP 2:
In this step your goal is to support translation of a range of characters. As is common ranges are specified by the start and end separated by a hyphen. For example the upper case letters are A-Z and the lower case letters a-z. When you’ve implemented this it should look something like this:

```bash
% head -n3 test.txt
The Project Gutenberg eBook of The Art of War
    
This ebook is for the use of anyone anywhere in the United States and
```
```bash
% head -n3 test.txt | cctr A-Z a-z
the project gutenberg ebook of the art of war
    
this ebook is for the use of anyone anywhere in the united states and
```
Where we can see the first three lines as published by Project Gutenberg, then the same translated to lowercase in the second example.

```bash
head -n3 test.txt | python3 main.py A-Z a-z
```

### STEP 3:
There is another way to specify the translation we just did:

```bash
% head -n3 test.txt | cctr "[:upper:]" "[:lower:]" 
the project gutenberg ebook of the art of war
    
this ebook is for the use of anyone anywhere in the united states and
```

In this step your goal is to support the [:class:] specifier as shown above. You can find the full list of classes in the man entry, I’d suggest at least supporting the following:

```bash
[:class:]  Represents all characters belonging to the defined character
                class.  Class names are:

                alnum        <alphanumeric characters>
                alpha        <alphabetic characters>
                blank        <whitespace characters>
                cntrl        <control characters>
                digit        <numeric characters>
                lower        <lower-case alphabetic characters>
                print        <printable characters>
                punct        <punctuation characters>
                rune         <valid characters>
                space        <space characters>
                special      <special characters>
                upper        <upper-case characters>
```

```bash
head -n3 test.txt | python3 main.py "[:upper:]" "[:lower:]" 
```

### Step 4
In this step your goal is to support deleting characters with the -d option. From the man page we get:

```bash
tr [-Ccu] -d string1

-d      Delete characters in string1 from the input.
```
So once implemented you should be able to do:

```bash
% head -n3 test.txt | cctr -d War
The Poject Gutenbeg eBook of The At of 
    
This ebook is fo the use of nyone nywhee in the United Sttes nd
```
Notice all instances of the characters W, a and r have been removed. Don’t forget to support the classes too, for example:

```bash
% head -n3 test.txt | cctr -d "[:upper:]"
he roject utenberg eook of he rt of ar
    
his ebook is for the use of anyone anywhere in the nited tates and
```

```bash
head -n3 test.txt | python3 main.py -d "[:upper:]
```

### STEP 5
In this step your goal is to support squashing characters with the -s option. From the man page we get:

```bash
tr [-Ccu] -s string1

-s      Squeeze multiple occurrences of the characters listed in the last
        operand (either string1 or string2) in the input into a single
        instance of the character.  This occurs after all deletion and
        translation is completed.
```

When used that looks like this:

```bash
% cctr -s AB                             
AAABBBCCC
ABCCC
```

Or using the classes and out test file:
```bash
% head -n10 test.txt | cctr -ds "[:alnum:]" "[:space:]" 
 
 
 
 
. , - 
 
 ... ,
 
 .
```

```bash
echo AAABBBCCC | python3 main.py -s AB 
```


```bash
head -n10 test.txt | python3 main.py -ds "[:alnum:]" "[:space:]
```