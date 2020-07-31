import lex
#from parser import Parser
#from evaluator import *

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
    lexer = lex.Lexer(src)
    for token in lexer:
        print(token)
    #parser = Parser(Lexer(src))
    #parser.set_precedence({ "_+_" : 2, "_-_" : 2 })
    #expr = parser.parse()
    #evaluator = Evaluator()
    #print(evaluator.evaluate(expr))
    #print("expr:   " + show_expr(expr))
    #print("result: " + str(val))
