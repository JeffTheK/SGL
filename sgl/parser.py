from .types import *

class Node:
    def __init__(self, name, args) -> None:
        self.name = name
        self.args = args

def parse(tokens: list) -> Exp:
    "Read an expression from a sequence of tokens."
    if len(tokens) == 0:
        raise SyntaxError('unexpected EOF')
    token = tokens.pop(0)
    if token == '(':
        L = []
        while tokens[0] != ')':
            L.append(parse(tokens))
        tokens.pop(0) # pop off ')'
        return L
    elif token == ')':
        raise SyntaxError('unexpected )')
    else:
        return atom(token)

def atom(token: str):
    "Numbers become numbers; every other token is a symbol."
    if token[0] in list('-0123456789') and token != "-":
        if token.count('.') > 0:
            return Number(float(token))
        else:
            return Number(int(token))
    elif token[0] == '"':
        return String(token[1:-1])
    else:
        return Symbol(token)