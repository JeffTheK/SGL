from .eval import eval
from .types import String, Symbol

def _new_str(args, env):
    output = ""
    for arg in args:
        output += arg.name + " "
    return output[:-1]

STRING_FUNCS = {
    Symbol('new-str'): _new_str
}