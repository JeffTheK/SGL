from sgl.eval import eval_string
from sgl.std_env import STD_ENV
from sgl.types import List, Symbol

def test_new_list():
    env = STD_ENV
    eval_string('(let i (new-list 1 "hello" true))', env)
    assert(env.vars[Symbol('i')] == List([1, "hello", True]))