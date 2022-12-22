from sgl.eval import eval_string
from sgl.stdlib import STD_ENV
from sgl.types import Symbol

def test_if():
    assert(eval_string("(if (== 1 1) 1 2)", STD_ENV) == 1)
    assert(eval_string("(if (== 1 2) 1 2)", STD_ENV) == 2)

def test_let():
    env = STD_ENV
    eval_string("(let i 1)", env)
    assert(env.vars[Symbol('i')] == 1)

def test_type():
    assert(eval_string("(type 1)", STD_ENV) == "Number")

def test_func():
    env = STD_ENV

    eval_string('(func my-func1 (+ 1 1))', env)
    assert(Symbol('my-func1') in env.funcs.keys())
    assert(eval_string('(my-func1)', env) == 2)

    eval_string('(func my-add (+ ARG1 ARG2))', env)
    assert(eval_string('(my-add 2 3)', env) == 5)