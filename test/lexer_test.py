from sgl import lexer

def test_tokenize():
    code = "(program (let i 5))"
    assert(lexer.tokenize(code) == ['(','program','(','let','i','5',')',')'])