from sgl.eval import eval_string
from sgl.std_env import STD_ENV
from sgl.types import List, Symbol

def setup_env():
    env = STD_ENV
    eval_string('(let i (new-list 1 "hello" true))', env)
    return env

def test_new_list():
    env = STD_ENV
    eval_string('(let i (new-list 1 "hello" true))', env)
    assert(env.vars[Symbol('i')] == List([1, "hello", True]))

def test_len():
    assert(eval_string('(len i)', setup_env()) == 3)

def test_elem_at():
    assert(eval_string('(elem-at 2 i)', setup_env()) == True)

def test_for_each():
    env = setup_env()
    eval_string('(let num1 0)', env)
    eval_string('(for-each x i (let num1 (+ num1 5)))', env)
    assert(env.vars[Symbol('num1')] == 15)

def test_pop_at():
    env = setup_env()
    assert(eval_string('(pop-at 2 i)', env) == True)
    assert(eval_string('(len i)', env) == 2)

def test_clear():
    env = setup_env()
    eval_string('(clear i)', env)
    assert(eval_string('(len i)', env) == 0)