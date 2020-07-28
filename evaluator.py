from parser import Op

import math

def evaluate_expr(expr, binding):
    if type(expr) == Op:
        op = expr.op
        l = expr.l
        r = expr.r
        if op == "+":
            return evaluate_expr(l, binding) + evaluate_expr(r, binding)
        elif op == "-":
            return evaluate_expr(l, binding) - evaluate_expr(r, binding)
        elif op == "*":
            # unary function application and scalar multiplication
            if l == "-":
                return -evaluate_expr(r, binding)
            if l == "+":
                return evaluate_expr(r, binding)
            if l == "ceil":
                return math.ceil(evaluate_expr(r, binding))
            if l == "floor":
                return math.floor(evaluate_expr(r, binding))
            if l == "round":
                return round(evaluate_expr(r, binding), 0)
            if r == "!":
                return math.gamma(evaluate_expr(l, binding) + 1)
            else:
                # if all else fails, it must be multiplication
                return evaluate_expr(l, binding) * evaluate_expr(r, binding)
        else:
            raise Exception("unknown operator '" + str(op) + "'")
    elif type(expr) == str:
        # implement lookup table for free variables
        if expr and expr[0] == "_" or expr[0].isalpha():
            if expr in binding:
                return evaluate_expr(binding[expr], binding)
            else:
                raise Exception("unknown variable '" + expr + "'")
        raise Exception("invalid variable identifier '" + expr + "'")
    else:
        return expr

def show_expr(expr):
    if type(expr) == Op:
        op = expr.op
        l = expr.l
        r = expr.r
        return "(" + show_expr(l) + " " + op + " " + show_expr(r) + ")"
    elif type(expr) == str:
        return expr
    else:
        return str(expr)
