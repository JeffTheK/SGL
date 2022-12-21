from .eval import eval
from .types import List, Symbol

def _new_list(args, env):
    elements = []
    for arg in args:
        elements.append(eval(arg, env))
    return List(elements)

LIST_FUNCS = {
    Symbol("new-list"): _new_list
}