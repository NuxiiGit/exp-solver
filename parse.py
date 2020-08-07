import lex

def is_terminal(x):
    """Returns whether a token is a terminal value."""
    return type(x) == str and x.isalpha() or type(x) == float

class Node:
    """Represents the abstract syntax of a function (`op`) being applied to an argument (`arg`)."""

    def __init__(self, op, arg):
        self.op = op
        self.arg = arg

    def __str__(self):
        def show_value(value):
            if type(value) == list:
                inner = ", ".join([str(x) for x in value])
                return "[" + inner + "]"
            else:
                return str(value)
        return "(" + show_value(self.op) + " " + show_value(self.arg) + ")"

class Parser:
    """Parses an array of tokens into a syntax tree."""

    def __init__(self, s):
        self.set_lexer(lex.Lexer(s))

    def set_lexer(self, lexer):
        """Assigns a lexer to this parser."""
        self.lexer = iter(lexer)
        self.peeked = None
        self.next()

    def parse(self):
        """Parses the current lexer."""
        return self.parse_equality()

    def parse_equality(self):
        """Parses `=` operator."""
        expr = self.parse_modulo()
        while self.advance(lambda x: x == "=") != None:
            l = expr
            r = Node("neg", self.parse_modulo())
            expr = Node("plus", [l, r])
        return expr

    def parse_modulo(self):
        """Parses `%` operator."""
        expr = self.parse_addition()
        while self.advance(lambda x: x == "%") != None:
            expr = Node("mod", [expr, self.parse_addition()])
        return expr

    def parse_addition(self):
        """Parses `+` and `-` binary operators."""
        expr = self.parse_multiplication()
        while (token := self.advance(lambda x: x in { "+", "-" })) != None:
            l = expr
            r = self.parse_multiplication()
            if token == "-":
                r = Node("neg", r)
            expr = Node("plus", [l, r])
        return expr

    def parse_multiplication(self):
        """Parses `*` and `/` binary operators."""
        expr = self.parse_unary()
        while (token := self.advance(lambda x: x in { "*", "/" })) != None:
            l = expr
            r = self.parse_unary()
            if token == "/":
                r = Node("inv", r)
            expr = Node("prod", [l, r])
        return expr

    def parse_unary(self):
        """Parses `-` and `+` unary operators."""
        if (token := self.advance(lambda x: x in { "+", "-" })) != None:
            if token == "-":
                return Node("neg", self.parse_unary())
            return self.parse_unary()
        return self.parse_implicit_call()

    def parse_implicit_call(self):
        """Parses implicit application."""
        expr = self.parse_exponential()
        while self.sat(lambda x: is_terminal(x)):
            expr = Node(expr, self.parse_exponential())
        return expr

    def parse_exponential(self):
        """Parses `^` binary operator."""
        expr = self.parse_unary_postfix()
        while self.advance(lambda x: x == "^") != None:
            expr = Node("exp", [expr, self.parse_unary_postfix()])
        return expr

    def parse_unary_postfix(self):
        """Parses `!` unary operator."""
        expr = self.parse_call()
        while self.advance(lambda x: x == "!") != None:
            expr = Node("fact", expr)
        return expr

    def parse_call(self):
        """Parses explicit application."""
        expr = self.parse_grouping()
        while self.sat(lambda x: x in { "(", "[", "{" }):
            expr = Node(expr, self.parse_grouping())
        return expr

    def parse_grouping(self):
        """Parses a grouping of expressions."""
        if (token := self.advance(lambda x: x in { "(", "[", "{", "|" })) != None:
            paren_close = { "(" : ")", "[" : "]", "{" : "}", "|" : "|" }[token]
            if self.advance(lambda x: x == paren_close) != None:
                return []
            expr = self.parse_vector()
            self.expects(lambda x: x == paren_close, "expected closing parenthesis in grouping")
            if token == "|":
                expr = Node("abs", expr)
            return expr
        else:
            return self.expects(is_terminal, "expected terminal value")

    def parse_vector(self):
        """Parses a list of expressions."""
        expr = self.parse()
        if not self.sat(lambda x: x == ","):
            return expr
        exprs = [expr]
        while self.advance(lambda x: x == ",") != None:
            expr = self.parse()
            exprs.append(expr)
        return exprs

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
        raise SyntaxError(msg)
