from parser import Op
from functools import reduce

def evaluate_expr(expr):
    if type(expr) == Op:
        op = expr.op
        l = expr.l
        r = expr.r
        if op == "+":
            return evaluate_expr(l) + evaluate_expr(r)
        elif op == "$":
            # application/implicit multiplication
            return evaluate_expr(l) * evaluate_expr(r)
        else:
            raise Exception("unknown operator '" + str(op) + "'")
    else:
        # to do: pass free variables as dictionary
        return expr
