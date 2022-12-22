from sgl.eval import eval_string
from sgl.stdlib import STD_ENV
from sgl.types import Symbol
import os

def setup():
    env = STD_ENV
    if os.path.isfile('test/file1.txt'):
        os.remove('test/file1.txt')
    eval_string('(let file (file:open "test/file1.txt" "w+"))', env)
    return env

def test_open():
    env = setup()
    assert(os.path.isfile('test/file1.txt'))

def test_write():
    env = setup()
    eval_string('(file:write file "Hello World!")', env)
    eval_string('(file:close file)', env)
    assert(open('test/file1.txt', 'r').read() == 'Hello World!')

def test_read():
    env = setup()
    eval_string('(file:write file "Hello World!")', env)
    eval_string('(file:close file)', env)

    eval_string('(let file (file:open "test/file1.txt" "r"))', env)
    assert(eval_string('(file:read file)', env) == 'Hello World!')