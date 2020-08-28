import lib.parse as parse
import lib.solve as solve
import sys

def show_value(value):
    """Converts a parser value into a string."""
    if isinstance(value, list):
        inner = ", ".join([show_value(x) for x in value])
        return "[" + inner + "]"
    elif isinstance(value, complex):
        real = show_value(value.real)
        imag = show_value(value.imag)
        if imag in { "0", "-0" }:
            # negligible complex component
            return real
        if real in { "0", "-0" }:
            # negligible real component
            return imag + "i"
        separator = "+" if value.imag >= 0 else ""
        return real + separator + imag + "i"
    elif isinstance(value, float):
        return ("%.9f" % value).rstrip("0").rstrip(".")
    else:
        return str(value)

def print_help():
    print("usage:")
    print("  python exp-solver.py <command> [<options>]")
    print("\navailable commands:")
    print("  eval")
    print("  hillclimb")
    print("\nexample:")
    print("  ~$ python exp-solver.py hillclimb 'x^2 + 2' x")
    print("  1.414213562i")

def read_expr(s):
    return parse.Parser(s).parse()

def read_value(s, default=0):
    try:
        expr = read_expr(s);
        value = solve.evaluate(expr)
        return value
    except:
        return default

def generate_binding(args):
    binding = { }
    if len(args) > 1 and args[0].strip() == "where":
        for arg in args[1 :]:
            assignment = arg.split("=")
            if len(assignment) != 2:
                raise ValueError("malformed variable binding '%s'" % arg)
            variable = assignment[0].strip()
            value = assignment[1].strip()
            binding[variable] = read_value(value)
    return binding

def run(args):
    if len(args) == 0:
        print_help()
        return
    command = args[0]
    options = args[1 :]
    if command in { "help", "?" } or command.isspace():
        print_help()
    elif command in { "eval", "evaluate" }:
        if len(options) < 1:
            print("eval <expression> [where] [<variable=binding>]")
        else:
            expr = read_expr(options[0])
            binding = generate_binding(options[1 :])
            value = solve.evaluate(expr, binding)
            print(show_value(value))
    elif command in { "hillclimb", "hillclimbing" }:
        if len(options) < 2:
            print("hillclimb <expression> <unknown> [where] [<variable=binding>]")
        else:
            expr = read_expr(options[0])
            unknown = options[1]
            binding = generate_binding(options[2 :])
            solution = solve.hillclimbing(expr, unknown, binding)
            if solution == None:
                print("unable to find a solution")
            else:
                print(show_value(solution))
    else:
        print("unknown command '%s'\n" % command)
        print_help()

args = sys.argv
try:
    run(args[1 :] if len(args) > 0 else [])
except Exception as e:
    print("an error occurred!\n%s" % e)
