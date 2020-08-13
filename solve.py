import parse
import ops
import sys

def evaluate(expr, binding):
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

def weight(candidate):
    """Computes the weight of a candidate."""
    return abs(candidate)

def neighbourhood(current, amount):
    """Returns the neighbourhood of this mathematical object."""
    return [current - amount, current + amount]

def hillclimb(expr, unknown, start=0, resolution=0.1):
    """Performs a naive hillclimbing optimisation algorithm to solve for `unknown`."""
    step = resolution
    value = start
    minimum = None
    try:
        minimum = weight(evaluate(expr, { unknown : value }))
    except:
        pass
    if minimum == None:
        raise ValueError("invalid starting value")
    while True:
        no_new_neighbour = True
        for neighbour in neighbourhood(value, step):
            # loop through neighbourhood to find a new minimum
            try:
                value = evaluate(expr, { unknown : neighbour })
                new_minimum = weight(value)
                if new_minimum < minimum:
                    minimum = new_minimum
                    value = neighbour
                    no_new_neighbour = False
            except:
                pass
        if no_new_neighbour:
            if step < sys.float_info.epsilon:
                # threshold reached, return index
                return value
            else:
                # increase resolution
                step /= 2
