class Parser:
    """Parses an array of tokens into a syntax tree."""

    def __init__(self, lexer):
        self.lexer = iter(lexer)

    def parse(self):
        yield

    def parse_expr_terminal(self):
        """parses a terminal expression"""
        yield

    def next(self):
        try:
            return next(self.lexer)
        except StopIteration:
            self.error("unexpected end of file")

    def error(self, msg):
        raise Exception(msg)
