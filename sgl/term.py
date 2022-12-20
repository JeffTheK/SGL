from .types import Symbol
from .eval import eval
import os

def _exec(args, env):
    command = eval(args[0], env)
    os.system(command)

TERM_FUNCS = {
    Symbol('term:exec'): _exec
}