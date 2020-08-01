import lex
import parse
import evaluator

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
    parser = parse.Parser(lexer)
    expr = parser.parse()
    evaluator = evaluator.Evaluator()
    evaluator.set_variable("x", 12)
    print(evaluator.evaluate(expr))
    #print("expr:   " + show_expr(expr))
    #print("result: " + str(val))
