import parse
import ops

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

def hillclimb(expr, unknown):
    """Performs a naive hillclimbing optimisation algorithm to solve for `unknown`."""
    value = 0
    amount = 1
    minimum = weight(evaluate(expr, { unknown : value }))
    while True:
        no_new_neighbour = True
        for neighbour in neighbourhood(value, amount):
            # loop through neighbourhood to find a new minimum
            new_minimum = weight(evaluate(expr, { unknown : neighbour }))
            if new_minimum < minimum:
                minimum = new_minimum
                value = neighbour
                no_new_neighbour = False
        if no_new_neighbour:
            # no new neighbour, return minimum
            return value
