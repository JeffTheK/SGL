from sgl.eval import eval_string
from sgl.stdlib import STD_ENV
from sgl.types import Symbol
import pytest

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

def test_include():
    env = STD_ENV
    eval_string('(include "test/libfile1.sgl")', env)
    assert(eval_string('(my-add-from-other-file 2 3)', env) == 5)

def test_use_namespace():
    env = STD_ENV
    eval_string('(func somelib:some-func (+ ARG1 ARG2))', env)
    eval_string('(use-namespace "somelib")', env)
    assert(eval_string('(some-func 2 3)', env) == 5)

def test_ensure():
    env = STD_ENV
    eval_string('(ensure (== 1 1))', env)
    with pytest.raises(AssertionError):
        eval_string('(ensure (== 1 2))', env)

def test_while(capsys):
    env = STD_ENV
    eval_string('(let i 1)', env)
    eval_string('(while (!= i 5) (print i) (let i (+ i 1)))', env)
    captured = capsys.readouterr()
    assert(captured.out == "1234")

def test_return():
    env = STD_ENV
    code = """
(func my-func1 
    (if (> ARG1 10)
        (return ">10")
        (pass)
    )

    (if (< ARG1 -10)
        (return "<10")
        (pass)
    )

    "other"
)
"""
    eval_string(code, env)
    assert(eval_string('(my-func1 11)', env) == ">10")
    assert(eval_string('(my-func1 -11)', env) == "<10")
    assert(eval_string('(my-func1 5)', env) == "other")