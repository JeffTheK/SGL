from .types import Exp, Symbol, Number, String, List, Env
from .error import error

def eval_string(string: str, env: Env, file_path=None):
    from .lexer import tokenize
    from .parser import parse
    return eval(parse(tokenize(string, file_path), file_path), env)

def eval(x: Exp, env: Env, file_path=None) -> Exp:
    try:
        "Evaluate an expression in an environment."
        if type(x) is Symbol:        # variable reference
            try: return env.funcs[x]
            except KeyError:
                return env.vars[x]
        elif type(x) is Number:      # constant number
            return x.value
        elif type(x) is String:
            return x.value.replace("\\s", " ").replace("\\op", "(").replace("\\cp", ")")
        elif type(x) is List:
            return x.elements
        elif x[0] in env.funcs.keys():
            return env.funcs[x[0]](x[1:], env)
        else:                            # procedure call
            proc = eval(x[0], env)
            args = [eval(arg, env) for arg in x[1:]]
            return proc(*args)
    except AssertionError as e:
        raise e
    except Exception as e:
        error("Eval error", e, None, file_path)