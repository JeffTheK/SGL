from sgl import parser
from sgl import lexer
from sgl.types import *

def test_parse():
    code = "(program (let i 5))"
    tokens = lexer.tokenize(code)
    result = parser.parse(tokens)
    print(result)
    assert(result == [Symbol('program'), [Symbol('let'), Symbol('i'), Number(5)]])

def test_parse_string():
    code = '(let i "hello")'
    tokens = lexer.tokenize(code)
    result = parser.parse(tokens)
    assert(result == [Symbol('let'), Symbol('i'), String('hello')])