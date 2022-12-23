from .types import Symbol, String
from .eval import eval, eval_string
import os

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
    for i in range(len(args)):
        arg = args[i]
        env.vars[Symbol(f'ARG{i + 1}')] = eval(arg, env)

    for x in body[:-1]:
        eval(x, env)
    return eval(body[-1], env)

def _func(args, env):
    name = args[0]
    body = args[1:]
    env.funcs[name] = lambda args, env, body=body: _func_call(args, env, body)

def _include(args, env):
    file_path: String = eval(args[0], env)
    file = open(file_path, 'r')
    code = file.read()
    file.close()
    eval_string(code, env)

def _use_namespace(args, env):
    namespace = eval(args[0], env) + ":"
    # funcs
    for i in range(len(env.funcs.keys())):
        old_key = list(env.funcs.keys())[i]
        if namespace in old_key.name:
            new_key = Symbol(old_key.name.replace(namespace, ''))
            env.funcs[new_key] = env.funcs.pop(old_key)
    
    # vars
    for i in range(len(env.vars.keys())):
        old_key = list(env.vars.keys())[i]
        if namespace in old_key.name:
            new_key = Symbol(old_key.name.replace(namespace, ''))
            env.vars[new_key] = env.funcs.pop(old_key)

CORE_FUNCS = {
    Symbol('program'): _program,
    Symbol('if'): _if,
    Symbol('print'): _print,
    Symbol('let'): _let,
    Symbol('type'): _type,
    Symbol('error'): _error,
    Symbol('func'): _func,
    Symbol('include'): _include,
    Symbol('use-namespace'): _use_namespace
}