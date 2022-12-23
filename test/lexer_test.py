from sgl import lexer

def strings_to_tokens(l: list):
    out = []
    for x in l:
        out.append(lexer.Token(x, 1))
    return out

def test_tokenize():
    code1 = "(program (let i 5))"
    result1 = strings_to_tokens(['(','program','(','let','i','5',')',')'])
    assert(lexer.tokenize(code1) == result1)

    code2 = '(let i "Hello, World!")'
    result2 = strings_to_tokens(['(','let','i','"Hello, World!"', ')'])
    assert(lexer.tokenize(code2) == result2)

    code3 = '(program)'
    result3 = strings_to_tokens(['(','program',')'])
    assert(lexer.tokenize(code3) == result3)

    code3 = '("0.5")'
    result3 = strings_to_tokens(['(','"0.5"',')'])
    assert(lexer.tokenize(code3) == result3)