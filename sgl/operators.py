from .eval import eval
from .types import Symbol

def _equality(args, env):
    return eval(args[0], env) == eval(args[1], env)

def _add(args, env):
    return eval(args[0], env) + eval(args[1], env)

def _subtract(args, env):
    return eval(args[0], env) - eval(args[1], env)

def _multiply(args, env):
    return eval(args[0], env) * eval(args[1], env)

def _divide(args, env):
    return eval(args[0], env) / eval(args[1], env)

def _less_than(args, env):
    return eval(args[0], env) < eval(args[1], env)

def _greater_than(args, env):
    return eval(args[0], env) > eval(args[1], env)

OPERATOR_FUNCS = {
    Symbol('=='): _equality,
    Symbol('!='): lambda args, env: not _equality(args, env),
    Symbol('<'): _less_than,
    Symbol('>'): _greater_than,
    Symbol('+'): _add,
    Symbol('-'): _subtract,
    Symbol('*'): _multiply,
    Symbol('/'): _divide
}