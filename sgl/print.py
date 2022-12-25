from .types import Symbol
from .eval import eval

def _print(args, env):
    for arg in args:
        print(str(eval(arg, env)))

PRINT_FUNCS = {
    Symbol('print'): _print
}