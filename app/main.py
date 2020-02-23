from lexer import Lexer

import sys

argument = sys.argv
del argument[0]
src = " ".join(argument)
lexer = Lexer(src)
while not lexer.empty():
    token = lexer.next()
    print(token)