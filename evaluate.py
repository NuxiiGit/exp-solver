import math
import functools

class Node:
    """Represents the abstract syntax of a function (`op`) being applied to an argument (`arg`)."""

    def __init__(self, op, arg):
        self.op = op
        self.arg = arg

    def __str__(self):
        def show_value(value):
            if type(value) == list:
                inner = ", ".join([str(x) for x in value])
                return "[" + inner + "]"
            else:
                return str(value)
        return "(" + show_value(self.op) + " " + show_value(self.arg) + ")"

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
        if type(expr) == Node:
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
