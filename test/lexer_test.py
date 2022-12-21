from sgl import lexer

def test_tokenize():
    code1 = "(program (let i 5))"
    result1 = ['(','program','(','let','i','5',')',')']
    assert(lexer.tokenize(code1) == result1)

    code2 = '(let i "Hello, World!")'
    result2 = ['(','let','i','"Hello, World!"', ')']
    assert(lexer.tokenize(code2) == result2)