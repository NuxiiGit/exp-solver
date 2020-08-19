import lib.parse as parse
import lib.solve as solve
import sys

def print_help():
    print("usage:")
    print("  python exp-solver.py <expression> [<options>]")
    print("\navailable options:")
    print("  eval")
    print("  hillclimb")

def read_expr(s):
    try:
        expr = parse.Parser(s).parse()
        return expr
    except:
        return None

def read_value(s, default=0):
    try:
        if (expr := read_expr(s)) == None:
            value = solve.evaluate(expr)
            return value
    except:
        pass
    return default

def run(args):
    if len(args) == 0:
        print_help()
        return
    command = args[0]
    options = args[1 :]
    if src in { "help", "?" } or src.isspace():
        print_help()
        return
    # parse expression
    expr = read_expr(src)
    if expr == None:
        print("failed to parse expression! %s" % e)
        return
    # perform options
    for option in options:
        params = option.split(":")
        option = params[0]
        params = params[1 :]
        msg = "performing %s with %s:" % (option, params)
        if option == "eval":
            binding = { }
            for param in params:
                assignment = param.split("=")
                if len(assignment) == 2:
                    variable = assignment[0].strip()
                    value = assignment[1].strip()
                    binding[variable] = read_value(value)
                msg += "\n  skipping malformed variable binding '%s'" % param
            try:
                value = solve.evaluate(expr, binding)
                msg += "\n  result = %s" % parse.show_value(value)
            except Exception as e:
                msg += "\n  unable to evaluate expression! %s" % e
        elif option == "hillclimb":
            solution = solve.hillclimb(expr, "x")
            msg += "\n  solution = %s" % parse.show_value(solution)
        else:
            msg = "skipping unknown option '%s'" % option
        print(msg)

args = sys.argv
run(args[1 :] if len(args) > 0 else [])
