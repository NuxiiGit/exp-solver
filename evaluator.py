import parse

import math

class EvaluationError(Exception):
    """Represents the case where an expression cannot be evaluated."""
    pass

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

    def evaluate(self, expr):
        """Evaluates the expression."""
        if type(expr) == parse.Node:
            op = expr.op
            arg = expr.arg
            raise EvaluationError("unimplemented")
        elif type(expr) == str:
            if expr in self.binding:
                return self.evaluate(self.binding[expr])
            else:
                raise EvaluationError("unbound identifier '" + str(expr) + "'")
        else:
            return expr
