from sgl.eval import eval_string
from sgl.stdlib import STD_ENV

def test_random_int():
    assert(eval_string("(random:random-int 1 5)", STD_ENV) in [1,2,3,4,5])