from .types import Symbol
from .eval import eval
from .core_funcs import CORE_FUNCS
from .operators import OPERATOR_FUNCS


def _not(args, env):
    return not eval(args[0])

def _or(args, env):
    return eval(args[0]) or eval(args[1])

def _and(args, env):
    return eval(args[0]) and eval(args[1])

BUILTIN_FUNCS = {
    
    Symbol('not'): _not,
    Symbol('or'): _or,
    Symbol('and'): _and,
    **CORE_FUNCS,
    **OPERATOR_FUNCS
}