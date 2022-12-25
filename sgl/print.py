from .types import Symbol
from .eval import eval

def _print(args, env):
    message = ""
    for arg in args:
        message += str(eval(arg, env)) + " "
    message = message[:-1]
    print(str(eval(arg, env)), end="")

def _print_line(args, env):
    message = ""
    for arg in args:
        message += str(eval(arg, env)) + " "
    message = message[:-1]
    print(message)

PRINT_FUNCS = {
    Symbol('print'): _print,
    Symbol('print-line'): _print_line
}