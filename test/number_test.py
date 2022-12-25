from sgl.eval import eval_string
from sgl.stdlib import STD_ENV
from sgl.types import Number

def setup():
    env = STD_ENV
    eval_string('(let num1 5)', env)
    return env

def test_to_num():
    assert(eval_string('(to-number "1")', STD_ENV) == Number(1))

def test_to_int():
    env = setup()
    assert(eval_string('(to-int (/ num1 2))', env) == 2)

def test_to_float():
    assert(eval_string('(to-float "0.5")', STD_ENV) == 0.5)

def test_range(capsys):
    eval_string('(for-each x (range 0 5 1) (print x))', STD_ENV)
    captured = capsys.readouterr()
    assert(captured.out == '01234')