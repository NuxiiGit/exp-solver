import parse
import solve
import sys

args = sys.argv
del args[0] # don't want working directory
count = len(args)
if count == 0:
    print("usage")
elif count < 2:
    print("invalid argument count")
else:
    kind = args[0]
    src = args[1]
    options = args[1 :]
    expr = parse.Parser(src).parse()
    print("--> %s" % expr)
    if kind == "eval":
        # evaluate expression
        print("attempting to evaluate expression...")
        value = solve.evaluate(expr)
        print("  value: %s" % parse.show_value(value))
    elif kind == "hillclimb":
        # hillclimbing solver
        print("attempting hillclimb...")
        solution = solve.hillclimb(expr, "x", start=0)
        print("  solution: %s" % solution)
    else:
        print("unknown solver option '%s'" % kind)
