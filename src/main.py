from lexer import Lexer
from parser import Parser
import parse

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
    result = parse.char(src, "a")
    print(result)

#    lexer = Lexer(src)
#    parser = Parser(lexer)
#    print("a: ", parser.parse())
#    for token in lexer:
#        print(token)
#    print("b: ", parser.parse())
