from sgl.interpreter import eval_string
from sgl.stdlib import STD_ENV

def test_print(capsys):
    eval_string('(print "Hello")', STD_ENV)
    captured = capsys.readouterr()
    assert(captured.out == "Hello\n")

def test_print_var(capsys):
    env = STD_ENV
    eval_string('(let i 1)', env)
    eval_string('(print i)', env)
    captured = capsys.readouterr()
    assert(captured.out == "1\n")