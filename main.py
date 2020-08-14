import parse
import solve
import sys

def print_help():
    print("usage:")
    print("  python main.py <command> [<options>]")
    print("\navailable commands:")
    print("  eval <expression>")
    print("  hillclimb <expression>")
    print("\nexample:")
    print("  ~$ python main.py eval '1 + 3i'")
    print("  --> (plus [1.0, (3.0 i)])")
    print("  attempting to evaluate expression...")
    print("    value: 1.0+3.0i")

args = sys.argv
del args[0] # don't want working directory
count = len(args)
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
