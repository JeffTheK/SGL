from .eval import eval
from .types import Symbol
import os

def _package_string(args, env):
    string = eval(args[0], env)
    package_name = eval(args[1], env)
    python_file = open(package_name + ".py", 'w+')
    code = f"""
from sgl.eval import eval_string
from sgl.stdlib import STD_ENV
CODE = "{string}"
eval_string(CODE, STD_ENV)
"""
    python_file.write(code)
    command = f"pyinstaller {package_name + '.py'} --onefile"
    os.system(command)

def _package_file(args, env):
    file_path = eval(args[0], env)
    file = open(file_path, 'r')
    code = file.read()
    _package_string([code, file_path], env)

PACKAGER_FUNCS = {
    Symbol('packager:package-string'): _package_string,
    Symbol('packager:package-file'): _package_file
}