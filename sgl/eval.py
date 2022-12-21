from .types import Exp, Symbol, Number, String, Env

def eval_string(string: str, env: Env):
    from .lexer import tokenize
    from .parser import parse
    return eval(parse(tokenize(string)), env)

def eval(x: Exp, env: Env) -> Exp:
    "Evaluate an expression in an environment."
    if type(x) is Symbol:        # variable reference
        try: return env.funcs[x]
        except KeyError:
            return env.vars[x]
    elif type(x) is Number:      # constant number
        return x.value
    elif type(x) is String:
        return x.value
    elif x[0] in env.funcs.keys():
        return env.funcs[x[0]](x[1:], env)
    else:                            # procedure call
        proc = eval(x[0], env)
        args = [eval(arg, env) for arg in x[1:]]
        return proc(*args)
