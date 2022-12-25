from sgl.eval import eval_string
from sgl.stdlib import STD_ENV

def test_alias():
    env = STD_ENV
    eval_string('(sgl:alias def func)', env)
    eval_string('(def add (+ ARG1 ARG2))', env)
    assert(eval_string('(add 2 3)', env) == 5)