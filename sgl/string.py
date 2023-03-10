from .eval import eval
from .types import String, Symbol, Number

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

def _quote(args, env):
    output = ""
    for arg in args:
        if (type(arg) is list):
            output += '(' + _quote(arg, env) + ')'
        elif (type(arg) is Symbol):
            output += arg.name + " "
        elif (type(arg) is Number or type(arg) is String):
            output += str(arg.value) + " "
    return output.replace(' )', ')')

def _format(args, env):
    string = eval(args[0], env)
    arguments = []
    for arg in args[1:]:
        arguments.append(str(eval(arg, env)))
    for i in range(len(arguments)):
        arg = arguments[i]
        string = string.replace(f"ARG{i + 1}", arg)
    return string

STRING_FUNCS = {
    Symbol('new-str'): _new_str,
    Symbol('replace'): _replace,
    Symbol('quote'): _quote,
    Symbol('format'): _format
}