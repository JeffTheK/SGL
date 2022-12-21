from sgl.eval import eval_string
from sgl.std_env import STD_ENV

def test_new_str():
    assert(eval_string("(new-str Hello World)", STD_ENV) == "Hello World")