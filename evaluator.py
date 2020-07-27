from parser import SExpr
from functools import reduce

def evaluate_expr(expr):
    if type(expr) == SExpr:
        op = expr.op
        args = expr.args
        if op == "+":
            return reduce(lambda x, y: evaluate_expr(x) + evaluate_expr(y), args, 0)
        elif op == "":
            return reduce(lambda x, y: evaluate_expr(x) * evaluate_expr(y), args, 1)
        else:
            raise Exception("unknown operator '" + str(op) + "'")
    else:
        # to do: pass free variables as dictionary
        return expr
