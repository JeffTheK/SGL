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

def _alias(args, env):
    alias_symbol = args[0]
    original_symbol = args[1]
    func = env.funcs[original_symbol]
    env.funcs[alias_symbol] = func

SPECIAL_VARS = {
    Symbol('sgl:version'): __version__,
    Symbol('sgl:authors'): "Dmytro Kolibabchuk"
}

SPECIAL_FUNCS = {
    Symbol('sgl:vars'): _vars,
    Symbol('sgl:funcs'): _funcs,
    Symbol('sgl:classes'): _classes,
    Symbol('sgl:alias'): _alias
}