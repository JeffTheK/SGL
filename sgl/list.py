from .eval import eval
from .types import List, Symbol

def _new_list(args, env):
    elements = []
    for arg in args:
        elements.append(eval(arg, env))
    return List(elements)

def _elem_at(args, env):
    index = eval(args[0], env)
    list: List = eval(args[1], env)
    return list.elements[index]

def _pop_at(args, env):
    index = eval(args[0], env)
    list: List = eval(args[1], env)
    return list.elements.pop(index)

def _clear(args, env):
    list: List = eval(args[0], env)
    list.elements.clear()

def _len(args, env):
    list: List = eval(args[0], env)
    return len(list.elements)

def _for_each(args, env):
    list: List = eval(args[1], env)
    iterator = args[0]
    action = args[2]
    for elem in list.elements:
        env.vars[iterator] = elem
        eval(action, env)

def _insert(args, env):
    index = eval(args[0], env)
    value = eval(args[1], env)
    list: List = eval(args[2], env)
    list.elements.insert(index, value)

def _filter(args, env):
    list: List = eval(args[0], env)
    condition = args[1]
    output = List([])
    for x in list.elements:
        env.vars[Symbol('ARG1')] = x
        if eval(condition, env) == True:
            output.elements.append(x)
    return output

LIST_FUNCS = {
    Symbol('new-list'): _new_list,
    Symbol('elem-at'): _elem_at,
    Symbol('pop-at'): _pop_at,
    Symbol('clear'): _clear,
    Symbol('len'): _len,
    Symbol('for-each'): _for_each,
    Symbol('insert'): _insert,
    Symbol('filter'): _filter
}