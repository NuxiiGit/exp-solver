from lexer import Lexer
from parser import Parser
from evaluator import *

import sys

argument = sys.argv
del argument[0] # don't need to know about the working directory
argument_count = len(argument)
if argument_count == 0:
    print("invalid argument count")
    print("please pass the expression as a string, e.g.")
    print("  \"2 + 5\"")
else:
    src = argument[0]
    parser = Parser(Lexer(src))
    expr = parser.parse()
    print(show_expr(expr))
    val = evaluate_expr(expr, { "a" : 12, "b" : -19.3 })
    print(val)
