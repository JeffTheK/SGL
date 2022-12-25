import re
import string as strlib
from .error import error

class Token:
    def __init__(self, value, line) -> None:
        self.value = value
        self.line = line
    
    def __eq__(self, __o: object) -> bool:
        return self.value == __o.value

def tokenize(string: str, file_path=None):
    string = re.sub(r';.+?\n', '', string)
    chars = list(string)
    tokens = []
    line = 1
    try:
        while len(chars) != 0:
            char = chars.pop(0)
            if char == '(':
                tokens.append(Token('(', line))
                continue
            elif char == ')':
                tokens.append(Token(')', line))
                continue
            elif char in strlib.ascii_letters + ':+-/*=!<>%':
                symbol = "" + char
                while char in strlib.ascii_letters + ':+-/*=!<>%0123456789':
                    char = chars.pop(0)
                    symbol += char
                symbol = symbol[:-1]
                tokens.append(Token(symbol, line))
                if char in ('()'):
                    tokens.append(Token(char, line))
                continue
            elif char == '"':
                _string = '"'
                char = chars.pop(0)
                _string += char
                while char != '"':
                    char = chars.pop(0)
                    _string += char
                tokens.append(Token(_string, line))
                if char in ('()'):
                    tokens.append(Token(char, line))
                continue
            elif char in list('0123456789'):
                number = "" + char
                while char in list('0123456789'):
                    char = chars.pop(0)
                    number += char
                number = number[:-1]
                tokens.append(Token(number, line))
                if char in ('()'):
                    tokens.append(Token(char, line))
                continue
            elif char == '\n':
                line += 1
        return tokens
    except Exception as e:
        error(f"Lexer error", e, line, file_path)