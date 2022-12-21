from .types import Symbol
from .eval import eval
from .core_funcs import CORE_FUNCS
from .operators import OPERATOR_FUNCS
from .list import LIST_FUNCS
from .random import RANDOM_FUNCS
from .term import TERM_FUNCS

BUILTIN_FUNCS = {
    **CORE_FUNCS,
    **OPERATOR_FUNCS,
    **LIST_FUNCS,
    **RANDOM_FUNCS,
    **TERM_FUNCS
}