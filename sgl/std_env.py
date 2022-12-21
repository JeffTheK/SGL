from .builtin import BUILTIN_FUNCS
from .std_vars import STD_VARS
from .types import Env

STD_ENV = Env(STD_VARS, BUILTIN_FUNCS)