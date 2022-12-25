from .types import Symbol

def _print(args, env):
    for arg in args:
        print(eval(arg, env))

PRINT_FUNCS = {
    Symbol('print'): _print
}