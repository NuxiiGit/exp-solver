import parse
import evaluate
import solve
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
    evaluator = evaluate.Evaluator()
    value = evaluator.evaluate(expr)
    print("expression: " + str(expr))
    print("value:      " + str(value))
