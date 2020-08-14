import parse
import solve
import sys

args = sys.argv
del args[0] # don't want working directory
count = len(args)
if count == 0:
    print("usage:")
    print("  python main.py [command] [expression] [options]")
    print("\navailable commands:")
    print("  eval")
    print("  hillclimb")
    print("\nexample:")
    print("  ~$ python main.py eval '1 + 3i'")
    print("  --> (plus [1.0, (3.0 i)])")
    print("  attempting to evaluate expression...")
    print("    value: 1.0+3.0i")
elif count < 2:
    print("invalid argument count")
else:
    command = args[0]
    src = args[1]
    options = args[1 :]
    expr = parse.Parser(src).parse()
    print("--> %s" % expr)
    if command == "eval":
        # evaluate expression
        print("attempting to evaluate expression...")
        value = solve.evaluate(expr)
        print("  value: %s" % parse.show_value(value))
    elif command == "hillclimb":
        # hillclimbing solver
        print("attempting hillclimb...")
        solution = solve.hillclimb(expr, "x", start=0)
        print("  solution: %s" % solution)
    else:
        print("unknown solver command '%s'" % command)
