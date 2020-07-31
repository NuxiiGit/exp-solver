from lexer import is_number, is_symbol, is_identifier

class ParseError(Exception):
    """Represents a parser error case."""
    pass

class Node:
    """Represents the abstract syntax of a function (`op`) being applied to an argument (`arg`)."""

    def __init__(self, op, *args):
        self.op = op
        self.args = args

    def __str__(self):
        return "{ op : " + str(self.op) + " , args : " + str(self.args) + " }"

def infix(s):
    return "_" + s + "_"

class Parser:
    """Parses an array of tokens into a syntax tree."""

    def __init__(self, lexer):
        self.set_lexer(lexer)
        self.set_precedence({ })

    def set_lexer(self, lexer):
        """Assigns a lexer to this parser."""
        self.lexer = iter(lexer)
        self.peeked = None
        self.next()

    def set_precedence(self, ops):
        """Sets the precedence of operators."""
        self.ops = ops
        prec_set = set()
        precs = []
        for prec in ops.values():
            if prec in prec_set:
                continue
            precs.append(prec)
            prec_set.add(prec)
        self.precs = precs

    def parse(self):
        """Parses the current lexer."""
        return self.parse_binary(0)

    def parse_binary(self, ind):
        """Parses a binary operation."""
        precs = self.precs
        ops = self.ops
        if ind >= len(precs):
            return self.parse_grouping()
        else:
            prec = precs[ind]
            expr = self.parse_binary(ind + 1)
            while (token := self.advance(lambda x: is_identifier(x) and infix(x) in ops and ops[infix(x)] == prec)) != None:
                expr = Node(token, expr, self.parse_binary(ind + 1))
            return expr

    def parse_grouping(self):
        """Parses a grouping of expressions."""
        if (token := self.advance(lambda x: x in { "(", "[", "{" })) != None:
            paren_close = { "(" : ")", "[" : "]", "{" : "}" }[token]
            expr = self.parse()
            self.expects(lambda x: x == paren_close, "expected closing parenthesis in grouping")
            return expr
        else:
            return self.expects(lambda x: is_identifier(x) or is_number(x), "expected terminal value")

    def expects(self, p, on_err):
        """Throws an error if the predicate does not hold for the next token."""
        if self.sat(p):
            return self.next()
        else:
            self.error(on_err)

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
