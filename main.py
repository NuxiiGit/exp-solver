import parse
import evaluate

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
    expr = parse.Parser(src).parse()
    print(expr)
    evaluator = evaluate.Evaluator()
    evaluator.set_variable("plus", lambda arg: arg[0] + arg[1])
    evaluator.set_variable("neg", lambda arg: -arg)
    print(evaluator.evaluate(expr))
    #print("expr:   " + show_expr(expr))
    #print("result: " + str(val))
