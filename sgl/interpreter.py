from .types import *
from .lexer import tokenize
from .parser import parse
from .eval import eval, eval_string
from .std_env import STD_ENV
import sys
import traceback

def exec_string(string: str):
    tokens = tokenize(string)
    eval(parse(tokens), STD_ENV)

def exec_file(file_path: str):
    file = open(file_path, 'r')
    exec_string(file.read())
    file.close()

def repl():
    while True:
        try: 
            result = eval_string(input("sgl > "), STD_ENV)
            print(result)
        except Exception as e:
            print("Exception: " + str(e))

def run():
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
        exec_file(file_path)
    else:
        repl()

if __name__ == "__main__":
    run()