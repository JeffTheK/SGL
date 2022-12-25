from sgl.eval import eval_string
from sgl.stdlib import STD_ENV

def test_equality():
    assert(eval_string("(== 1 1)", STD_ENV) == True)
    assert(eval_string("(== 1 2)", STD_ENV) == False)

def test_not_equality():
    assert(eval_string("(!= 1 1)", STD_ENV) == False)
    assert(eval_string("(!= 1 2)", STD_ENV) == True)

def test_not():
    assert(eval_string("(not (== 1 2))", STD_ENV) == True)
    assert(eval_string("(not (== 1 1))", STD_ENV) == False)

def test_or():
    assert(eval_string("(or (== 1 1) (== 1 2))", STD_ENV) == True)
    assert(eval_string("(or (== 1 2) (== 1 3))", STD_ENV) == False)

def test_and():
    assert(eval_string("(and (== 1 1) (== 1 1))", STD_ENV) == True)
    assert(eval_string("(and (== 1 1) (== 1 2))", STD_ENV) == False)

def test_greater_then():
    assert(eval_string("(> 2 1)", STD_ENV) == True)
    assert(eval_string("(> 1 1)", STD_ENV) == False)

def test_less_then():
    assert(eval_string("(< 1 2)", STD_ENV) == True)
    assert(eval_string("(< 2 1)", STD_ENV) == False)

def test_add():
    assert(eval_string("(+ 1 1)", STD_ENV) == 2)

def test_subtract():
    assert(eval_string("(- 1 1)", STD_ENV) == 0)

def test_multiply():
    assert(eval_string("(* 2 1)", STD_ENV) == 2)

def test_divide():
    assert(eval_string("(/ 4 2)", STD_ENV) == 2)

def test_modulus():
    assert(eval_string("(% 4 2)", STD_ENV) == 0)