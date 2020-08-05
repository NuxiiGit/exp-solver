import parse
import math
import cmath
import functools
import numbers

def assert_lists_equal_length(a, b):
    len_a = len(a)
    len_b = len(b)
    if len_a != len_b:
        raise ArithmeticError("incompatible vector lengths (" + str(len_a) + " and " + str(len_b) + ")")
    else:
        return len_a

def op_plus(x):
    """Adds a list of mathematical objects."""
    def binary_plus(a, b):
        if isinstance(a, list) and isinstance(b, list):
            n = assert_lists_equal_length(a, b)
            xs = []
            for i in range(0, n):
                xs.append(binary_plus(a[i], b[i]))
            return xs
        else:
            return a + b
    if isinstance(x, list):
        if len(x) == 0:
            return 0
        acc = x[0]
        for item in x[1 :]:
            acc = binary_plus(acc, item)
        return acc
    else:
        return x

def op_prod(x):
    """Multiplies a list of mathematical objects."""
    def binary_prod(a, b):
        if isinstance(a, list) and isinstance(b, list):
            n = assert_lists_equal_length(a, b)
            dot = 0
            for i in range(0, n):
                dot = dot + binary_prod(a[i], b[i])
            return dot
        elif isinstance(b, list):
            return [a * x for x in b]
        else:
            return a * b
    if isinstance(x, list):
        if len(x) == 0:
            return 1
        acc = x[0]
        for item in x[1 :]:
            acc = binary_prod(acc, item)
        return acc
    else:
        return x

def op_neg(x):
    """Negates a mathematical object."""
    return op_prod([-1, x])

def op_inv(x):
    """Finds the inverse of a mathematical object."""
    if isinstance(x, list):
        return [op_inv(a) for a in x]
    else:
        return 1 / x

def op_fact(x):
    """Computes the factorial of a mathematical object."""
    if isinstance(x, list):
        return [op_fact(a) for a in x]
    elif isinstance(x, complex):
        raise ArithmeticError("complex factorials are not supported")
    else:
        return math.gamma(x + 1)

def op_log(x):
    """Returns the logarithm of a mathematical object."""
    base = 10
    val = x
    if isinstance(x, list):
        if len(x) != 2:
            raise ArithmeticError("undefined logarithm argument count")
        base = x[0]
        val = x[1]
    if isinstance(base, complex) or isinstance(val, complex):
        return cmath.log(val, base)
    else:
        return math.log(val, base)

def op_ln(x):
    """Returns the natural logarithm of a mathematical structure."""
    return op_log([math.e, x])

def op_sin(x):
    """Computes the sine of this mathematical object."""
    if isinstance(x, list):
        return [op_sin(a) for a in x]
    elif isinstance(x, complex):
        return cmath.sin(x)
    else:
        return math.sin(x)

def op_abs(x):
    """Computes the absolute value of a mathematical object."""
    if isinstance(x, list):
        return [op_abs(a) for a in x]
    else:
        return abs(x)

class Evaluator:
    """Contains a variable binding which is used when evaluating expressions."""

    def __init__(self):
        self.binding = { }
        self.builtins = {
            "plus" : op_plus,
            "prod" : op_prod,
            "neg" : op_neg,
            "inv" : op_inv,
            "fact" : op_fact,
            "log" : op_log,
            "ln" : op_ln,
            "sin" : op_sin,
            "abs" : op_abs,
            "i" : 1j,
            "e" : math.e,
            "pi" : math.pi,
            "tau" : 2 * math.pi,
            "phi" : (1 + 5 ** 0.5) / 2
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
                return op_prod([op, arg])
        elif type(expr) == str:
            if expr in self.binding:
                return self.evaluate(self.binding[expr])
            elif expr in self.builtins:
                return self.evaluate(self.builtins[expr])
            else:
                raise LookupError("unbound identifier '" + str(expr) + "'")
        elif type(expr) == list:
            return [self.evaluate(x) for x in expr]
        else:
            return expr
