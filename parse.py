class ParseError(Exception):
    """Represents a parser error case."""
    pass

class Node:
    """Represents the abstract syntax of a function (`op`) being applied to an argument (`arg`)."""

    def __init__(self, op, *args):
        self.op = op
        self.arg = args

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
        return self.parse_grouping()

    def parse_grouping(self):
        """Parses a grouping of expressions."""
        if (token := self.advance(lambda x: x in { "(", "[", "{" })) != None:
            paren_close = { "(" : ")", "[" : "]", "{" : "}" }[token]
            expr = self.parse()
            self.expects(lambda x: x == paren_close, "expected closing parenthesis in grouping")
            return expr
        else:
            return self.expects(lambda x: type(x) == str and x.isalpha() or type(x) == float, "expected terminal value")

    def expects(self, p, on_err):
        """Throws an error if the predicate does not hold for the next token."""
        if self.sat(p):
            return self.next()
        else:
            self.error("got '" + str(self.peek()) + "': " + str(on_err))

    def advance(self, p):
        """Advances the parser and returns the token if it satisfies the predicate. Otherwise returns `None`."""
        if self.sat(p):
            return self.next()
        else:
            return None

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
        raise ParseError(msg)
