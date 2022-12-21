from sgl.eval import eval_string
from sgl.std_env import STD_ENV
from sgl.types import Symbol

def setup_env():
    env = STD_ENV
    eval_string('(let str1 (new-str Hello World))', STD_ENV)
    return env

def test_new_str():
    assert(eval_string("(new-str Hello World)", setup_env()) == "Hello World")

def tests_replace():
    env = setup_env()
    eval_string('(replace "World" "Friend" str1)', env)
    assert(env.vars[Symbol('str1')] == "Hello Friend")