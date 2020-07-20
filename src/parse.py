def sat(s, p):
    """Parses a character of a string if it satisfies some predicate."""
    if s == "" or !p(s[0]):
        return None
    return s[0], s[1:]
