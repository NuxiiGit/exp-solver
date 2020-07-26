from parser import SExpr

def evaluate_expr(expr):
    if type(expr) == SExpr:
        op = expr.op
        arg = expr.arg
        if op == "+":
            if type(arg) == list:
                return reduce(lambda x, y: x + y, arg, 0)
            else:
                return arg
        elif type(op) != list and type(arg) != list:
            return evaluate_expr(op) * evaluate_expr(arg)
        else:
            raise Exception("unknown operator '" + str(op) + "'")
    else:
        return expr
