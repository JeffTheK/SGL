from .eval import eval
from .types import Symbol
import os.path

def _open(args, env):
    path = eval(args[0], env)
    mode = eval(args[1], env)
    return open(path, mode)

def _read(args, env):
    file = eval(args[0], env)
    return file.read()

def _write(args, env):
    file = eval(args[0], env)
    text = eval(args[1], env)
    file.write(text)

def _close(args, env):
    file = eval(args[0], env)
    file.close()

def _mkdir(args, env):
    path = eval(args[0], env)
    os.mkdir(path)

FILE_FUNCS = {
    Symbol('file:open'): _open,
    Symbol('file:read'): _read,
    Symbol('file:write'): _write,
    Symbol('file:close'): _close,
    Symbol('file:mkdir'): _mkdir
}