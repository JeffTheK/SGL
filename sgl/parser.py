from .types import *
from .lexer import Token
from .error import error

class Node:
    def __init__(self, name, args) -> None:
        self.name = name
        self.args = args

def parse(tokens: list, file_path=None) -> Exp:
    "Read an expression from a sequence of tokens."
    try:
        if len(tokens) == 0:
            raise SyntaxError('unexpected EOF')
        token = tokens.pop(0)
        if token.value == '(':
            L = []
            while tokens[0].value != ')':
                L.append(parse(tokens))
            tokens.pop(0) # pop off ')'
            return L
        elif token.value == ')':
            raise SyntaxError('unexpected )')
        else:
            return atom(token)
    except Exception as e:
        error("Parser error", e, token.line, file_path)

def atom(token: Token):
    "Numbers become numbers; every other token is a symbol."
    if token.value[0] in list('-0123456789') and token.value != "-":
        if token.value.count('.') > 0:
            return Number(float(token.value))
        else:
            return Number(int(token.value))
    elif token.value[0] == '"':
        return String(token.value[1:-1])
    else:
        return Symbol(token.value)