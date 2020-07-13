class Parser:
    """Parses an array of tokens into a syntax tree."""

    def __init__(self, lexer):
        self.set_lexer(lexer)

    def set_lexer(self, lexer):
        """Assigns a lexer to this parser."""
        self.lexer = iter(lexer)

    def parse(self):
        """Parses the current lexer."""
        return self.parse_expr_terminal()

    def parse_expr_terminal(self):
        """parses a terminal expression."""
        return self.next()

    def next(self):
        """Advances the parser and returns the next token."""
        try:
            return next(self.lexer)
        except StopIteration:
            self.error("unexpected end of file")

    def error(self, msg):
        """Raises a parser error with this message."""
        raise Exception(msg)
