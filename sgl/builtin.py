from .types import Symbol
from .eval import eval
from .core_funcs import CORE_FUNCS
from .operators import OPERATOR_FUNCS

BUILTIN_FUNCS = {
    **CORE_FUNCS,
    **OPERATOR_FUNCS
}