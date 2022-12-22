from .types import Symbol, ClassDefinition
from .version import __version__

def _vars(args, env):
    return env.vars

def _funcs(args, env):
    return env.funcs

def _classes(args, env):
    output = {}
    for (key, value) in env.vars.items():
        if type(value) is ClassDefinition:
            output[key] = value
    return output

SPECIAL_VARS = {
    Symbol('sgl:version'): __version__,
    Symbol('sgl:authors'): "Dmytro Kolibabchuk"
}

SPECIAL_FUNCS = {
    Symbol('sgl:vars'): _vars,
    Symbol('sgl:funcs'): _funcs,
    Symbol('sgl:classes'): _classes
}