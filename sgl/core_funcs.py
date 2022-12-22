from .types import Symbol
from .eval import eval

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
    env.vars[symbol] = eval(exp, env)

def _type(args, env):
    return type(args[0]).__name__

def _error(args, env):
    print("Error")
    exit()

def _func_call(args, env, body):
    for x in body[:-1]:
        eval(x, env)
    return eval(body[-1], env)

def _func(args, env):
    name = args[0]
    body = args[1:]
    env.funcs[name] = lambda args, env, body=body: _func_call(args, env, body)

CORE_FUNCS = {
    Symbol('program'): _program,
    Symbol('if'): _if,
    Symbol('print'): _print,
    Symbol('let'): _let,
    Symbol('type'): _type,
    Symbol('error'): _error,
    Symbol('func'): _func
}