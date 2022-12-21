import re
import string as strlib

def tokenize(string: str):
    string = re.sub(r';.+?\n', '', string)
    chars = list(string)
    tokens = []
    while len(chars) != 0:
        char = chars.pop(0)
        if char == '(':
            tokens.append('(')
            continue
        elif char == ')':
            tokens.append(')')
            continue
        elif char in strlib.ascii_letters + ':+-/*=!<>':
            symbol = "" + char
            while char in strlib.ascii_letters + ':+-/*=!<>0123456789':
                char = chars.pop(0)
                symbol += char
            symbol = symbol[:-1]
            tokens.append(symbol)
            if char in ('()'):
                tokens.append(char)
            continue
        elif char == '"':
            _string = '"'
            char = chars.pop(0)
            _string += char
            while char != '"':
                char = chars.pop(0)
                _string += char
            tokens.append(_string)
            if char in ('()'):
                tokens.append(char)
            continue
        elif char in list('0123456789'):
            number = "" + char
            while char in list('0123456789'):
                char = chars.pop(0)
                number += char
            number = number[:-1]
            tokens.append(number)
            if char in ('()'):
                tokens.append(char)
            continue
    return tokens