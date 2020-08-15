import lib.parse as parse
import lib.solve as solve
import sys

def print_help():
    print("usage:")
    print("  python exp-solver.py <expression> [<options>]")
    print("\navailable options:")
    print("  eval")
    print("  hillclimb")

def run(args):
    if len(args) == 0:
        print_help()
        return
    src = args[0]
    options = args[1 :]
    if src in { "help", "?" } or src.isspace():
        print_help()
        return
    # parse expression
    expr = 0
    try:
        expr = parse.Parser(src).parse()
        print("--> %s" % expr)
    except Exception as e:
        print("failed to parse expression! %s" % e)
        return
    # perform options
    for option in options:
        params = option.split(":")
        param_count = len(params)
        if params[0] == "eval":
            print("bweh")
        else:
            print("skipping unknown option '%s'" % option)

args = sys.argv
del args[0] # don't want working directory
run(args)
