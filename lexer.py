class Token:
    """Represents a token and its infix value."""

    def __init__(self, node, infix):
        self.node = node
        self.infix = infix

    def __str__(self):
        return "[node=" + str(self.node) + ", infix=" + str(self.infix) + "]"

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
        if x.isalpha() or x == "_":
            # consume identifier
            self.advance_while(lambda x : x.isalpha() or x.isdigit() or x == "'" or x == "_")
            return Token(self.substr(), False)
        elif x.isdigit():
            # consume number
            self.advance_while(str.isdigit)
            if not self.empty() and self.chr() == ".":
                self.advance()
                self.advance_while(str.isdigit)
            return Token(float(self.substr()), False)
        else:
            # consume operators
            self.advance()
            return Token(x, True)

    def advance_while(self, p):
        """Advances whilst some predicate `p` is true."""
        while not self.empty():
            if p(self.chr()):
                self.advance()
            else:
                break

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
