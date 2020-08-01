import parse

import math
import functools

class Value:
    """Represents all possible evaluation values."""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return self.__str__()

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
