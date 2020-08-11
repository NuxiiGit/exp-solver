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

def neighbourhood(current, amount):
    """Returns the neighbourhood of this mathematical object."""
    return [current - amount, current + amount]

def hillclimb(expr, unknown, variables={ }):
    """Performs a naive hillclimbing optimisation algorithm to solve for `unknown`."""
    binding = variables.copy()
    if not (unknown in binding):
        binding[unknown] = 0
    # TODO: hill climbing
    minimum = evaluate(expr, binding)
    amount = 1
    while True:
        neighbours = neighbourhood(binding[unknown], amount)
        # loop through neighbourhood to find a new minimum
    return binding[unknown]
