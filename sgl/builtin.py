from .types import Symbol
from .eval import eval
from .core_funcs import CORE_FUNCS
from .operators import OPERATOR_FUNCS
from .list import LIST_FUNCS
from .string import STRING_FUNCS
from .random import RANDOM_FUNCS
from .term import TERM_FUNCS
from .packager import PACKAGER_FUNCS

BUILTIN_FUNCS = {
    **CORE_FUNCS,
    **OPERATOR_FUNCS,
    **LIST_FUNCS,
    **STRING_FUNCS,
    **RANDOM_FUNCS,
    **TERM_FUNCS,
    **PACKAGER_FUNCS
}