from .eval import eval
from .types import Symbol, Number

def _to_number(args, env):
    value = eval(args[0], env)
    try: return Number(int(value))
    except ValueError:
        return Number(float(value))

def _to_int(args, env):
    number = _to_number(args, env)
    return Number(int(number.value))

def _to_float(args, env):
    number = _to_number(args, env)
    return Number(float(number.value))

NUMBER_FUNCS = {
    Symbol('to-number'): _to_number,
    Symbol('to-int'): _to_int,
    Symbol('to-float'): _to_float
}