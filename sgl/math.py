from .eval import eval
from .types import Symbol
import math

def _sin(args, env):
    return math.sin(eval(args[0], env))

def _cos(args, env):
    return math.cos(eval(args[0], env))

def _tan(args, env):
    return math.tan(eval(args[0], env))

def _sqrt(args, env):
    return math.sqrt(eval(args[0], env))

def _pow(args, env):
    number = eval(args[0], env)
    power = eval(args[1], env)
    return number**power

MATH_FUNCS = {
    Symbol('math:sin'): _sin,
    Symbol('math:cos'): _cos,
    Symbol('math:tan'): _tan,
    Symbol('math:sqrt'): _sqrt,
    Symbol('math:pow'): _pow
}