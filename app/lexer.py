def lex(s):
    """Splits an string into an array of smaller tokens."""
    a = []
    i = 0
    n = len(s)
    while i < n:
        if s[i].isspace():
            # ignore whitespace
            i += 1
            continue
        j = i + 1
        if s[i].isalpha():
            # consume identifier
            while j < n:
                if s[j].isalpha() or s[j].isdigit():
                    j += 1
                else:
                    break
        a.append(s[i : j])
        i = j
    return a