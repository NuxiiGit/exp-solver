import sys

argument = sys.argv
argument_count = len(argument)

if argument_count < 1:
    print("invalid number of arguments")
else:
    for arg in argument:
        print("arg: ", arg)