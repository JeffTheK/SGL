from .types import *
from .lexer import tokenize
from .parser import parse
from .std_env import STD_ENV
import sys

def _program(args, env):
    for exp in args:
        eval(exp, env)

def _if(args, env):
    (test, conseq, alt) = args
    exp = (conseq if eval(test, env) else alt)
    return eval(exp, env)

def _print(args, env):
    for arg in args:
        print(eval(arg, env))

def _let(args, env):
    (symbol, exp) = args
    env[symbol] = eval(exp, env)

def _type(args, env):
    return type(args[0]).__name__

def _equality(args, env):
    return eval(args[0], env) == eval(args[1], env)

def _add(args, env):
    return eval(args[0], env) + eval(args[1], env)

def _subtract(args, env):
    return eval(args[0], env) + eval(args[1], env)

def _multiply(args, env):
    return eval(args[0], env) * eval(args[1], env)

def _divide(args, env):
    return eval(args[0], env) / eval(args[1], env)

def _less_than(args, env):
    return eval(args[0], env) < eval(args[1], env)

def _greater_than(args, env):
    return eval(args[0], env) > eval(args[1], env)

def _not(args, env):
    return not eval(args[0])

def _or(args, env):
    return eval(args[0]) or eval(args[1])

def _and(args, env):
    return eval(args[0]) and eval(args[1])

def _error(args, env):
    print("Error")
    exit()

BUILTIN_FUNCS = {
    Symbol('program'): _program,
    Symbol('if'): _if,
    Symbol('print'): _print,
    Symbol('let'): _let,
    Symbol('type'): _type,
    Symbol('error'): _error,
    Symbol('=='): _equality,
    Symbol('!='): lambda args, env: not _equality(args, env),
    Symbol('not'): _not,
    Symbol('or'): _or,
    Symbol('and'): _and,
    Symbol('<'): _less_than,
    Symbol('>'): _greater_than,
    Symbol('+'): _add,
    Symbol('-'): _subtract,
    Symbol('*'): _multiply,
    Symbol('/'): _divide
}

def eval(x: Exp, env=STD_ENV) -> Exp:
    "Evaluate an expression in an environment."
    if type(x) is Symbol:        # variable reference
        return env[x]
    elif type(x) is Number:      # constant number
        return x.value
    elif type(x) is String:
        return x.value
    elif x[0] in BUILTIN_FUNCS.keys():
        return BUILTIN_FUNCS[x[0]](x[1:], env)
    else:                            # procedure call
        proc = eval(x[0], env)
        args = [eval(arg, env) for arg in x[1:]]
        return proc(*args)

def exec_string(string: str):
    tokens = tokenize(string)
    eval(parse(tokens))

def exec_file(file_path: str):
    file = open(file_path, 'r')
    exec_string(file.read())
    file.close()

def run():
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
        exec_file(file_path)

if __name__ == "__main__":
    run()