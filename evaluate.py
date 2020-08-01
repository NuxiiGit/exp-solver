import math
import functools

class Value:
    """Represents all possible evaluation values."""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        if type(self.value) == list:
            inner = ", ".join([str(x) for x in self.value])
            return "[" + inner + "]"
        else:
            return str(self.value)

class Node:
    """Represents the abstract syntax of a function (`op`) being applied to an argument (`arg`)."""

    def __init__(self, op, arg):
        self.op = Value(op)
        self.arg = Value(arg)

    def __str__(self):
        return "(" + str(self.op) + " " + str(self.arg) + ")"

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
