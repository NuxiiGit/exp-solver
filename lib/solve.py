import lib.parse as parse
import lib.ops as ops
import sys
import math
import random

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

def weight(expr, binding):
    """Computes the weight of an expression using this binding."""
    try:
        value = evaluate(expr, binding)
        return abs(value)
    except:
        return sys.float_info.max

def neighbourhood(current, amount):
    """Returns the neighbourhood of this mathematical object."""
    angle = math.pi / 8
    neighbours = [current + complex(amount * math.cos(x * angle), amount * math.sin(x * angle)) for x in [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16]]
    neighbours.append(current + amount)
    neighbours.append(current - amount)
    return neighbours

def hillclimbing(expr, unknown, variables, resolution=10):
    """Performs a naive hillclimbing optimisation algorithm to solve for `unknown`."""
    step = resolution
    binding = variables.copy()
    value = 0
    if unknown in binding:
        value = binding[unknown]
    else:
        binding[unknown] = 0
    if isinstance(value, list):
        raise ValueError("hillclimbing is not supported for vector unknowns")
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
            if step <= sys.float_info.epsilon:
                # threshold reached, return index
                return value if minimum <= 10e-09 else None
            else:
                # increase resolution
                step /= 2

def simulated_annealing(expr, unknown, variables, resolution=10):
    """Performs a simulated annealing optimisation algorithm to solve for `unknown`."""
    binding = variables.copy()
    value = 0
    if unknown in binding:
        value = binding[unknown]
    else:
        binding[unknown] = 0
    minimum = weight(expr, binding)
    while True:
        neighbour = random.choice(neighbourhood(value, step))
        binding[unknown] = neighbour
        new_minimum = weight(expr, binding)
