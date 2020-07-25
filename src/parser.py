class SExpr:
    """Abstract syntax for mathematical expressions."""

    def __init__(self, op, arg):
        self.op = op
        self.arg = arg

    def __str__(self):
        return "[op=" + str(self.op) + ", arg=" + str(self.arg) + "]"

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
        return self.parse_expr()

    def parse_expr(self):
        """Parses an expression."""
        return self.parse_expr_apply()

    def parse_expr_apply(self):
        """Parses the application of two values."""
        expr = self.parse_expr_terminal()
        while self.sat(lambda x: x.node == "(" or x.node == "[" or x.node == "{" or x.infix == False):
            arg = self.parse_expr_terminal()
            expr = SExpr(expr, arg)
        return expr

    def parse_expr_terminal(self):
        """Parses a terminal expression."""
        if self.sat(lambda x: x.infix == False):
            return self.next().node
        else:
            return self.parse_expr_grouping()

    def parse_expr_grouping(self):
        """Parses a grouping of expressions."""
        paren = self.expects(lambda x: x.node == "(" or x.node == "[" or x.node == "{", "malformed expression")
        paren_close = { "(" : ")", "[" : "]", "{" : "}" }[paren.node]
        if self.sat(lambda x: x.node == paren_close):
            self.next()
            return []
        expr = self.parse_expr_list()
        self.expects(lambda x: x.node == paren_close, "expected closing parenthesis in grouping")
        return expr

    def parse_expr_list(self):
        """Parses a list of expressions."""
        expr = self.parse_expr()
        if not self.sat(lambda x: x.node == ","):
            return expr
        exprs = [expr]
        while self.sat(lambda x: x.node == ","):
           self.next()
           expr = self.parse_expr()
           exprs.append(expr)
        return exprs

    def expects(self, p, on_err):
        """Throws an error if the predicate does not hold for the next token."""
        if self.sat(p):
            return self.next()
        else:
            self.error(on_err)

    def sat(self, p):
        """Returns whether the next token satisfies this predicate."""
        peek = self.peek()
        return False if peek == None else p(peek)

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
