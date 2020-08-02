import parse
import math
import functools
import numbers

class EvaluationError(Exception):
    """Represents the case where an expression cannot be evaluated."""
    pass

def builtin_plus(x):
    """Adds two mathematical objects together."""
    def binary_plus(a, b):
        if type(a) == list and type(b) == list:
            return 0
        elif isinstance(a, numbers.Number) and isinstance(b, numbers.Number):
            return a + b
        else:
            raise EvaluationError("plus is not defined for types ''")
    if type(x) == list:
        if len(x) == 0:
            return 0
        acc = x[0]
        for item in x[1:]:
            acc = binary_plus(acc, item)
        return acc
    else:
        return x

def builtin_neg(arg):
    """Negates a mathematical object."""
    return -arg

class Evaluator:
    """Contains a variable binding which is used when evaluating expressions."""

    def __init__(self):
        self.binding = { }
        self.builtins = {
            "plus" : builtin_plus,
            "neg" : builtin_neg,
            "i" : 1j
        }

    def set_variable(self, ident, value):
        """Assigns the variable binding for this evaluator."""
        if value == None and ident in self.binding:
            del self.binding[ident]
        else:
            self.binding[ident] = value

    def evaluate(self, expr):
        """Evaluates the expression."""
        if type(expr) == parse.Node:
            op = self.evaluate(expr.op)
            arg = self.evaluate(expr.arg)
            if callable(op):
                return op(arg)
            else:
                return op * arg
        elif type(expr) == str:
            if expr in self.binding:
                return self.evaluate(self.binding[expr])
            elif expr in self.builtins:
                return self.evaluate(self.builtins[expr])
            else:
                raise EvaluationError("unbound identifier '" + str(expr) + "'")
        elif type(expr) == list:
            return [self.evaluate(x) for x in expr]
        else:
            return expr
