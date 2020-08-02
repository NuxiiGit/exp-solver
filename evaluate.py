import parse
import math
import functools

class EvaluationError(Exception):
    """Represents the case where an expression cannot be evaluated."""
    pass

def builtin_plus(arg):
    """Adds two mathematical objects together."""
    if type(arg) == list:
        if len(arg) == 0:
            return 0
        acc = arg[0]
        for item in arg[1:]:
            acc = acc + item
        return acc
    else:
        return arg

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
