from parser import Op
from functools import reduce
import math

def evaluate_expr(expr):
    if type(expr) == Op:
        op = expr.op
        l = expr.l
        r = expr.r
        if op == "+":
            return evaluate_expr(l) + evaluate_expr(r)
        elif op == "-":
            return evaluate_expr(l) - evaluate_expr(r)
        elif op == "*":
            # unary function application and scalar multiplication
            if l == "-":
                return -evaluate_expr(r)
            if l == "+":
                return r
            if r == "!":
                return math.gamma(evaluate_expr(l) + 1)
            else:
                # if all else fails, it must be multiplication
                return evaluate_expr(l) * evaluate_expr(r)
        else:
            raise Exception("unknown operator '" + str(op) + "'")
    elif type(expr) == str:
        # implement lookup table for free variables
        raise Exception("unknown variable '" + str(expr) + "'")
    else:
        return expr
