from sgl.eval import eval_string
from sgl.stdlib import STD_ENV

def test_pow():
    assert(eval_string('(math:pow 2 2)', STD_ENV) == 4)