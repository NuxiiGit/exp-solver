import lexer

import sys

argument = sys.argv
del argument[0]
src = " ".join(argument)
tokens = lexer.lex(src)
print(tokens)