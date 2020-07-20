class Parser:
    """Parses an array of tokens into a syntax tree."""

    def __init__(self, lexer):
        self.set_lexer(lexer)

    def set_lexer(self, lexer):
        """Assigns a lexer to this parser."""
        self.lexer = iter(lexer)
        self.peeked = None
        self.next()

    def parse(self):
        """Parses the current lexer."""
        return self.parse_expr_terminal()

    def parse_expr_terminal(self):
        """parses a terminal expression."""
        return self.next()

    def peek(self):
        """Returns the peeked token"""
        return self.peeked

    def next(self):
        """Advances the parser and returns the next token."""
        peeked = self.peeked
        try:
            self.peeked = next(self.lexer)
        except StopIteration:
            self.peeked = None
        return peeked

    def error(self, msg):
        """Raises a parser error with this message."""
        raise Exception(msg)
