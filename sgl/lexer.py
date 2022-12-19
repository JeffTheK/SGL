import re

def tokenize(string: str):
    string = re.sub(r';.+?\n', '', string)
    return string.replace("(", " ( ").replace(")", " ) ").split()