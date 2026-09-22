# xy-language
tree-walking interpreted language

xy is a mini, dynamically-typed, expression-orientated scripting language that uses python, it shouldnt be taken seriously whatsoever lolol, but i feel like its somewhat helpful to help people new to programming to comprehend certain ideas alot easier (maybe? people learn differently) i decided to publish it after working on it since late september of this year (2026)

**how the language is structured**

every xy program is a singular expression, the parser ``Parser.parse`` parses just one expression and then requires end of input there is no statement list no semi-colons and newline handling in the lexer, there is no luxury of that kind.

what this means for u:

a program is written on a only one line, ``if`` ``for`` ``while`` and ``func`` are all expressions they evaluate to a value not some control-flow construct

to achieve being able to do multiple things u chain them via variables (``set x = "string"``) no such thing as sequencing operator

remember, its a small scripting language not a full multi-statement file format

int: 5,-3 (python int under the hood)
float: 6.9 (any number with a dot "." within it)
string: "x and y, where is z?" (double qoutes, doesnt support singular qoutes however does support `\t` `\n` `\"` `//`)

okay yeah im tired of writing it heres a cheat sheet (ill probably write more)

``set x = 5                          -- variables
set s = "hi " + "there"            -- string concat
set b = "ha" * 3                   -- "hahaha"

x + y x - y x * y x / y x ** y
x == y x != y x < y x > y x <= y x >= y
x and y x or y not x

if x > 3 then printxy("z") elif x == 3 then printxy("eq") else printxy("small")

for i = 0 to 10 then printxy(i)          -- 0..9
for i = 10 to 0 step -1 then printxy(i)  -- countdown

while x > 0 then set x = x - 1

func square(n) -- n * n     -- note: -- not ->
square(5)

set double = func(n) -- n * 2
double(21)

set L = [1, 2, 3]
L / 1      -- index    > 2
L + 4      -- append   > [1,2,3,4]
L - 0      -- remove   > [2,3]
L * [9]    -- concat   > [1,2,3,9]

append(L, 4) pop(L, 0) extend(L1, L2) -- mutate in place
is_num(v)  is_str(v)  is_list(v)  is_func(v)
printxy(v)  input()  input_int()  clear()
null / false = 0     true = 1     math_pi``

(also tysm to @codepulse on yt his videos helped me understand things alot more easier)
