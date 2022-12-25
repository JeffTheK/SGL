from sgl.interpreter import eval_string
from sgl.stdlib import STD_ENV

def test_print(capsys):
    eval_string('(print "Hello")', STD_ENV)
    captured = capsys.readouterr()
    