import parse
import ops

def evaluate(expr, binding):
    """Evaluates an expression using this binding."""
    if isinstance(expr, parse.Node):
        op = evaluate(expr.op, binding)
        arg = evaluate(expr.arg, binding)
        if callable(op):
            return op(arg)
        else:
            # implicit multiplication
            return ops.op_prod([op, arg])
    elif isinstance(expr, str):
        if expr in binding:
            return evaluate(binding[expr], binding)
        elif expr in ops.binding:
            return evaluate(ops.binding[expr], binding)
        else:
            raise LookupError("unbound identifier '%s'" % expr)
    elif isinstance(expr, list):
        return [evaluate(x, binding) for x in expr]
    else:
        return expr

class Evaluator:
    """Contains a variable binding which is used when evaluating expressions."""

    def __init__(self):
        self.binding = { }

    def set_variable(self, ident, value):
        """Assigns the variable binding for this evaluator."""
        if value == None and ident in self.binding:
            del self.binding[ident]
        else:
            self.binding[ident] = value

    def get_variable(self, ident):
        """Returns the value of this variable binding."""
        return self.binding[ident] if ident in self.binding else None

    def evaluate(self, expr):
        """Evaluates the expression."""
        if type(expr) == parse.Node:
            op = self.evaluate(expr.op)
            arg = self.evaluate(expr.arg)
            if callable(op):
                return op(arg)
            else:
                return op_prod([op, arg])
        elif type(expr) == str:
            if expr in self.binding:
                return self.evaluate(self.binding[expr])
            elif expr in ops.binding:
                return self.evaluate(ops.binding[expr])
            else:
                raise LookupError("unbound identifier '" + str(expr) + "'")
        elif type(expr) == list:
            return [self.evaluate(x) for x in expr]
        else:
            return expr
