def sat(p):
    """Parses a character of a string if it satisfies some predicate."""
    return (lambda x: None if x == "" or (not p(x[0])) else (x[0], x[1:]))

def char(c):
    """Parses a specific character."""
    return sat(lambda x: x == c)

