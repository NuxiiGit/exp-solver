from parser import Node

import math

class Evaluator:

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
            raise Exception("unimplemented")
        elif type(expr) == str:
            raise Exception("unimplemented 2")
        else:
            return expr
