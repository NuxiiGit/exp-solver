import lib.parse as parse
import lib.solve as solve
import sys

def print_help():
    print("usage:")
    print("  python exp-solver.py <command> [<options>]")
    print("\navailable commands:")
    print("  eval")
    print("  hillclimb")

def read_expr(s):
    return parse.Parser(s).parse()

def read_value(s, default=0):
    try:
        expr = read_expr(s);
        value = solve.evaluate(expr)
        return value
    except:
        return default

def run(args):
    if len(args) == 0:
        print_help()
        return
    command = args[0]
    options = args[1 :]
    if command in { "help", "?" } or command.isspace():
        print_help()
        return
    if command == "eval":
        if len(options) == 0:
            print("eval <expression> [<variable=binding>]")
            return
        expr = read_expr(options[0])
        binding = { }
        for param in options[1 :]:
            assignment = param.split("=")
            if len(assignment) != 2:
                raise ValueError("malformed variable binding '%s'" % param)
            variable = assignment[0].strip()
            value = assignment[1].strip()
            binding[variable] = read_value(value)
        value = solve.evaluate(expr, binding)
        print(parse.show_value(value))
        return
    if command == "hillclimb":
        solution = solve.hillclimb(expr, "x")
        if solution == None:
            print("unable to find a solution")
            return
        print(parse.show_value(solution))
        return
    print("unknown command '%s'\n" % command)
    print_help()

args = sys.argv
try:
    run(args[1 :] if len(args) > 0 else [])
except Exception as e:
    print("an error occurred!\n%s" % e)
