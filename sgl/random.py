from .eval import eval
from .types import Symbol
import random as rnd

def _random_int(args, env):
    min = eval(args[0], env)
    max = eval(args[1], env)
    return rnd.randint(min, max)

RANDOM_FUNCS = {
    Symbol('random:random-int'): _random_int
}