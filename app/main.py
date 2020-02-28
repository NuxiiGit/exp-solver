from lexer import Lexer

import sys

argument = sys.argv
del argument[0] # don't need to know about the working directory
argument_count = len(argument)
if argument_count == 0:
    print("invalid argument count")
    print("please pass the expression as a string, e.g.")
    print("  \"2a + 5b\"")
else:
    src = argument[0]
    lexer = iter(Lexer(src))
    for token in lexer:
        print(token)