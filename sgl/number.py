from .eval import eval
from .types import Symbol, Number, List

def _to_number(args, env):
    value = eval(args[0], env)
    try: return Number(int(value))
    except ValueError:
        return Number(float(value))

def _to_int(args, env):
    number = _to_number(args, env)
    return int(number.value)

def _to_float(args, env):
    number = _to_number(args, env)
    return float(number.value)

def _range(args, env):
    start = eval(args[0], env)
    stop = eval(args[1], env)
    step = eval(args[2], env)
    return List(range(start, stop, step))

NUMBER_FUNCS = {
    Symbol('to-number'): _to_number,
    Symbol('to-int'): _to_int,
    Symbol('to-float'): _to_float,
    Symbol('range'): _range
}