from .types import Symbol, Env
from .eval import eval
from .core_funcs import CORE_FUNCS
from .operators import OPERATOR_FUNCS
from .list import LIST_FUNCS
from .string import STRING_FUNCS
from ._class import CLASS_FUNCS
from .random import RANDOM_FUNCS
from .term import TERM_FUNCS
from .packager import PACKAGER_FUNCS
from .special import SPECIAL_VARS, SPECIAL_FUNCS
from .file import FILE_FUNCS

STD_VARS = {
    Symbol('true'): True,
    Symbol('false'): False,
    **SPECIAL_VARS
}

STD_FUNCS = {
    **CORE_FUNCS,
    **OPERATOR_FUNCS,
    **LIST_FUNCS,
    **STRING_FUNCS,
    **CLASS_FUNCS,
    **RANDOM_FUNCS,
    **TERM_FUNCS,
    **PACKAGER_FUNCS,
    **SPECIAL_FUNCS,
    **FILE_FUNCS
}

STD_ENV = Env(STD_VARS, STD_FUNCS)
