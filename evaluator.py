from parser import Node
from lexer import is_identifier, is_number

import math

class EvaluationError(Exception):
    """Represents the case where an expression cannot be evaluated."""
    pass

class Evaluator:
    """Contains a variable binding which is used when evaluating expressions."""

    def __init__(self):
        self.set_binding({ })

    def set_binding(self, binding):
        """Assigns the variable binding for this evaluator."""
        self.binding = binding

    def evaluate(self, expr):
        """Evaluates the expression."""
        if type(expr) == Node:
            op = expr.op
            args = expr.args
            raise EvaluationError("unimplemented")
        elif is_identifier(expr):
            raise EvaluationError("unimplemented 2")
        elif is_number(expr):
            return expr
        else:
            raise EvaluationError("unknown value")
