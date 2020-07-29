def is_symbol(self):
    """Returns whether a token is a kind of reserved symbol."""
    return self in { "(", ")", "[", "]", "{", "}", "," }

def is_number(self):
    """Returns whether a token is a numerical value."""
    return type(self) == float

def is_identifier(self):
    """Returns whether a token is an identifier."""
    return not is_number(self) and not is_symbol(self)

class Lexer:
    """Splits a string into individual smaller tokens."""

    def __init__(self, src):
        self.set_source(src, 0, len(src))

    def __iter__(self):
        return self

    def __next__(self):
        if self.empty():
            raise StopIteration
        else:
            return self.next()

    def set_source(self, src, offset, length):
        """Sets the current source string to lex, and the offset and length to lex."""
        self.src = src
        self.cursor_begin = offset
        self.cursor_end = self.cursor_begin
        self.length = length

    def next(self):
        """Returns the next token in the source string."""
        self.advance_while(str.isspace)
        self.clear()
        x = self.chr()
        if x.isalpha() or x == "'":
            # consume identifier
            self.advance_while(lambda x: x.isalpha() or x == "'")
            return self.substr()
        elif x.isdigit():
            # consume real number
            self.advance_while(str.isdigit)
            if self.sat(lambda x: x == "."):
                self.advance()
                self.advance_while(str.isdigit)
            return float(self.substr())
        else:
            # consume operators
            self.advance()
            if x == '.' and self.sat(str.isdigit):
                # fractional numbers
                self.advance_while(str.isdigit)
                return float(self.substr())
            else:
                return x

    def advance_while(self, p):
        """Advances whilst some predicate `p` is true."""
        while not self.empty():
            if p(self.chr()):
                self.advance()
            else:
                break

    def sat(self, p):
        """Returns whether the current character satisfies a predicate `p`."""
        return not self.empty() and p(self.chr())

    def advance(self):
        """Advances the lexer."""
        self.cursor_end += 1

    def chr(self):
        """Returns the next character."""
        return self.src[self.cursor_end]

    def substr(self):
        """Returns the current substring."""
        return self.src[self.cursor_begin : self.cursor_end]

    def clear(self):
        """Clears the current substring."""
        self.cursor_begin = self.cursor_end

    def empty(self):
        """Returns whether the lexer is empty."""
        return self.cursor_end >= self.length
