from sgl.interpreter import exec_file

def test_hello_world(capsys):
    exec_file('examples/hello-world.sgl')
    captured = capsys.readouterr()
    assert(captured.out == "Hello, World!\n")