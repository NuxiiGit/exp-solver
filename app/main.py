from lexer import Lexer

import sys

argument = sys.argv
del argument[0]
src = " ".join(argument)
lexer = iter(Lexer(src))
for token in lexer:
    print(token)