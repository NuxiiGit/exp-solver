def sat(s, p):
    """Parses a character of a string if it satisfies some predicate."""
    if s == "" or (not p(s[0])):
        return None
    return s[0], s[1:]

def char(s, c):
    """Parses a specific character."""
    return sat(s, lambda x: x == c)
