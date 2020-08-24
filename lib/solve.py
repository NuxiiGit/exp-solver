import lib.parse as parse
import lib.ops as ops
import sys
import math

def evaluate(expr, binding={ }):
    """Evaluates an expression using this binding."""
    if isinstance(expr, parse.Node):
        op = evaluate(expr.op, binding)
        arg = evaluate(expr.arg, binding)
        if callable(op):
            return op(arg)
        else:
            # implicit multiplication
            return ops.op_prod([op, arg])
    elif isinstance(expr, str):
        if expr in binding:
            return evaluate(binding[expr], binding)
        elif expr in ops.binding:
            return evaluate(ops.binding[expr], binding)
        else:
            raise LookupError("unbound identifier '%s'" % expr)
    elif isinstance(expr, list):
        return [evaluate(x, binding) for x in expr]
    else:
        return expr

def approximately_zero(value):
    """Returns whether this floating point value is approimately equal to zero."""
    if value == 0:
        return True
    e1 = math.floor(math.log10(abs(value)))
    e2 = math.floor(math.log10(sys.float_info.epsilon))
    return e1 <= e2 + 1

def weight(expr, binding):
    """Computes the weight of an expression using this binding."""
    try:
        value = evaluate(expr, binding)
        return abs(value)
    except:
        return sys.float_info.max

def neighbourhood(current, amount):
    """Returns the neighbourhood of this mathematical object."""
    if isinstance(current, list):
        raise ValueError("neighbourhood operators are not implemented for vector unknowns")
    n = 16
    angle = 2 * math.pi / n
    return [current + complex(amount * math.cos(x * angle), amount * math.sin(x * angle)) for x in range(0, n)]

def hillclimb(expr, unknown, variables, resolution=0.1):
    """Performs a naive hillclimbing optimisation algorithm to solve for `unknown`."""
    step = resolution
    binding = variables.copy()
    value = 0
    if unknown in binding:
        value = binding[unknown]
    else:
        binding[unknown] = 0
    minimum = weight(expr, binding)
    while True:
        no_new_neighbour = True
        for neighbour in neighbourhood(value, step):
            # loop through neighbourhood to find a new minimum
            binding[unknown] = neighbour
            new_minimum = weight(expr, binding)
            if new_minimum < minimum:
                minimum = new_minimum
                value = neighbour
                no_new_neighbour = False
        if no_new_neighbour:
            if approximately_zero(step):
                print(value)
                # threshold reached, return index
                return value if approximately_zero(minimum) else None
            else:
                # increase resolution
                step /= 2
