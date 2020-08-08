def neighbourhood(current, amount):
    """Returns the neighbourhood of this mathematical object."""
    return [current - amount, current + amount]

def hillclimb(evaluator, unknown):
    """Performs a naive hillclimbing optimisation algorithm to solve for `unknown`."""
    amount = 1
    index = evaluator.get_variable(unknown)
    if not isinstance(index, (int, float, complex)):
        index = 0
    # TODO: hill climbing
    return index
