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

def op_gamma(x):
    """Computes the gamma function of a mathematical object."""
    if isinstance(x, list):
        return [op_gamma(a) for a in x]
    elif isinstance(x, complex):
        raise ArithmeticError("complex factorials are not supported")
    else:
        return math.gamma(x)

def op_fact(x):
    """Computes the factorial of a mathematical object."""
    return op_gamma(op_plus([x, 1]))

def op_exp(x):
    """Returns the power of this object mathematical object."""
    base = math.e
    val = x
    if isinstance(x, list):
        if len(x) != 2:
            raise ArithmeticError("undefined exponent argument count")
        base = x[0]
        val = x[1]
    return base ** val

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

def op_abs(x):
    """Returns the absolute value of a mathematical object."""
    if isinstance(x, list):
        return [op_abs(a) for a in x]
    else:
        return abs(x)

def op_signum(x):
    """Returns the sign of this mathematical object."""
    if isinstance(x, list):
        return [op_signum(a) for a in x]
    else:
        m = abs(x)
        if m:
            x /= m
        return x

def op_ceil(x):
    """Returns the ceiling of this mathematical object."""
    if isinstance(x, list):
        return [op_ceil(a) for a in x]
    elif isinstance(x, complex):
        return complex(math.ceil(x.real), math.ceil(x.imag))
    else:
        return math.ceil(x)

def op_round(x):
    """Returns the rounded version of this mathematical object."""
    if isinstance(x, list):
        return [op_round(a) for a in x]
    elif isinstance(x, complex):
        return complex(round(x.real), round(x.imag))
    else:
        return round(x)

def op_floor(x):
    """Returns the floor of this mathematical object."""
    if isinstance(x, list):
        return [op_floor(a) for a in x]
    elif isinstance(x, complex):
        return complex(math.floor(x.real), math.floor(x.imag))
    else:
        return math.floor(x)

def op_phase(x):
    """Returns the phase of a complex number."""
    if isinstance(x, list):
        return [op_phase(a) for a in x]
    else:
        return cmath.phase(x)

def op_mod(x):
    """Returns the modulo of this mathematical object."""
    if isinstance(x, list) and len(x) == 2:
        a = x[0]
        b = x[1]
        c = op_floor(op_prod([a, op_inv(b)]))
        return op_plus([a, op_neg(op_prod([c, b]))])
    else:
        raise ValueError("unsupported argument count for modulo")

def op_sin(x):
    """Returns the sine of this mathematical object."""
    if isinstance(x, list):
        return [op_sin(a) for a in x]
    elif isinstance(x, complex):
        return cmath.sin(x)
    else:
        return math.sin(x)

def op_cos(x):
    """Returns the cosine of this mathematical object."""
    if isinstance(x, list):
        return [op_cos(a) for a in x]
    elif isinstance(x, complex):
        return cmath.cos(x)
    else:
        return math.cos(x)

def op_tan(x):
    """Returns the tangent of this mathematical object."""
    if isinstance(x, list):
        return [op_tan(a) for a in x]
    elif isinstance(x, complex):
        return cmath.tan(x)
    else:
        return math.tan(x)

def op_asin(x):
    """Returns the inverse sine of this mathematical object."""
    if isinstance(x, list):
        return [op_asin(a) for a in x]
    elif isinstance(x, complex):
        return cmath.asin(x)
    else:
        return math.asin(x)

def op_acos(x):
    """Returns the inverse cosine of this mathematical object."""
    if isinstance(x, list):
        return [op_acos(a) for a in x]
    elif isinstance(x, complex):
        return cmath.acos(x)
    else:
        return math.acos(x)

def op_atan(x):
    """Returns the inverse tangent of this mathematical object."""
    if isinstance(x, list):
        return [op_atan(a) for a in x]
    elif isinstance(x, complex):
        return cmath.atan(x)
    else:
        return math.atan(x)

def op_csc(x):
    """Returns the cosecant of this mathematical object."""
    return op_inv(op_sin(x))

def op_sec(x):
    """Returns the secant of this mathematical object."""
    return op_inv(op_cos(x))

def op_cot(x):
    """Returns the cotangent of this mathematical object."""
    return op_inv(op_tan(x))

def op_acsc(x):
    """Returns the inverse cosecant of this mathematical object."""
    return op_inv(op_asin(x))

def op_asec(x):
    """Returns the inverse secant of this mathematical object."""
    return op_inv(op_acos(x))

def op_acot(x):
    """Returns the inverse cotangent of this mathematical object."""
    return op_inv(op_atan(x))

def op_sinh(x):
    """Returns the hyperbolic sine of this mathematical object."""
    if isinstance(x, list):
        return [op_sinh(a) for a in x]
    elif isinstance(x, complex):
        return cmath.sinh(x)
    else:
        return math.sinh(x)

def op_cosh(x):
    """Returns the hyperbolic cosine of this mathematical object."""
    if isinstance(x, list):
        return [op_cosh(a) for a in x]
    elif isinstance(x, complex):
        return cmath.cosh(x)
    else:
        return math.cosh(x)

def op_tanh(x):
    """Returns the hyperbolic tangent of this mathematical object."""
    if isinstance(x, list):
        return [op_tanh(a) for a in x]
    elif isinstance(x, complex):
        return cmath.tanh(x)
    else:
        return math.tanh(x)

def op_asinh(x):
    """Returns the inverse hyperbolic sine of this mathematical object."""
    if isinstance(x, list):
        return [op_asinh(a) for a in x]
    elif isinstance(x, complex):
        return cmath.asinh(x)
    else:
        return math.asinh(x)

def op_acosh(x):
    """Returns the inverse hyperbolic cosine of this mathematical object."""
    if isinstance(x, list):
        return [op_acosh(a) for a in x]
    elif isinstance(x, complex):
        return cmath.acosh(x)
    else:
        return math.acosh(x)

def op_atanh(x):
    """Returns the inverse hyperbolic tangent of this mathematical object."""
    if isinstance(x, list):
        return [op_atanh(a) for a in x]
    elif isinstance(x, complex):
        return cmath.atanh(x)
    else:
        return math.atanh(x)

def op_csch(x):
    """Returns the hyperbolic cosecant of this mathematical object."""
    return op_inv(op_sinh(x))

def op_sech(x):
    """Returns the hyperbolic secant of this mathematical object."""
    return op_inv(op_cosh(x))

def op_coth(x):
    """Returns the hyperbolic cotangent of this mathematical object."""
    return op_inv(op_tanh(x))

def op_acsch(x):
    """Returns the inverse hyperbolic cosecant of this mathematical object."""
    return op_inv(op_asinh(x))

def op_asech(x):
    """Returns the inverse hyperbolic secant of this mathematical object."""
    return op_inv(op_acosh(x))

def op_acoth(x):
    """Returns the inverse hyperbolic cotangent of this mathematical object."""
    return op_inv(op_atanh(x))

class Evaluator:
    """Contains a variable binding which is used when evaluating expressions."""

    def __init__(self):
        self.binding = { }
        self.builtins = {
            "plus" : op_plus,
            "prod" : op_prod,
            "neg" : op_neg,
            "inv" : op_inv,
            "gamma" : op_gamma,
            "fact" : op_fact,
            "exp" : op_exp,
            "log" : op_log,
            "ln" : op_ln,
            "sin" : op_sin,
            "cos" : op_cos,
            "tan" : op_tan,
            "csc" : op_csc,
            "sec" : op_sec,
            "cot" : op_cot,
            "sinh" : op_sinh,
            "cosh" : op_cosh,
            "tanh" : op_tanh,
            "csch" : op_csch,
            "sech" : op_sech,
            "coth" : op_coth,
            "asin" : op_asin,
            "acos" : op_acos,
            "atan" : op_atan,
            "acsc" : op_acsc,
            "asec" : op_asec,
            "acot" : op_acot,
            "asinh" : op_asinh,
            "acosh" : op_acosh,
            "atanh" : op_atanh,
            "acsch" : op_acsch,
            "asech" : op_asech,
            "acoth" : op_acoth,
            "abs" : op_abs,
            "signum" : op_signum,
            "sgn" : "signum",
            "ceil" : op_ceil,
            "round" : op_round,
            "floor" : op_floor,
            "phase" : op_phase,
            "arg" : "phase",
            "mod" : op_mod,
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
