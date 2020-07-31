def is_number(self):
    """Returns whether a token is a numerical value."""
    return type(self) == float

def is_identifier(self):
    """Returns whether a token is an identifier."""
    return type(self) == str and isalpha(self)

def is_symbol(self):
    """Returns whether a token is a kind of reserved symbol."""
    return type(self) == str and not is_identifier(self)
