import lib.parse as parse
import lib.solve as solve
import sys

def print_help():
    print("usage:")
    print("  python exp-solver.py <expression> [<options>]")
    print("\navailable options:")
    print("  eval")
    print("  hillclimb")

args = sys.argv
del args[0] # don't want working directory
arg_count = len(args)
if arg_count == 0:
    print_help()
else:
    src = args[0]
    options = args[1 :]
    if src == "help" or src == "?":
        print_help()
    else:
        try:
            expr = parse.Parser(src).parse()
            print("--> %s" % expr)
        except Exception as e:
            print("failed to parse expression! %s" % e)

"""
if count == 0:
    print_help()
elif count < 2:
    print("invalid argument count!")
    print_help()
else:
    command = args[0]
    options = args[1 :]
    if command == "eval" and len(options) == 1:
        # evaluate expression
        expr = parse.Parser(options[0]).parse()
        print("attempting to evaluate the following expression...")
        print("--> %s" % expr)
        value = solve.evaluate(expr)
        print(" = %s" % parse.show_value(value))
    elif command == "hillclimb" and len(options) == 1:
        # hillclimbing solver
        src = options[0]
        expr = parse.Parser(src).parse()
        print("attempting hillclimbing algorithm...")
        print("--> %s" % expr)
        solution = solve.hillclimb(expr, "x", start=0)
        print("  solution = %s" % solution)
    else:
        print("unknown solver command '%s'" % command)
"""
