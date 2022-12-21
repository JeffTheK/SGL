from .eval import eval
from .types import String, Symbol

def _new_str(args, env):
    output = ""
    for arg in args:
        output += arg.name + " "
    return output[:-1]

def _replace(args, env):
    old = eval(args[0], env)
    new = eval(args[1], env)
    string = eval(args[2], env)
    new_string = string.replace(old, new)
    env.vars[args[2]] = new_string

STRING_FUNCS = {
    Symbol('new-str'): _new_str,
    Symbol('replace'): _replace
}