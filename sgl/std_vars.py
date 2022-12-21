from .types import Symbol
from .version import __version__

STD_VARS = {
    Symbol('true'): True,
    Symbol('false'): False,
    Symbol('sgl:version'): __version__,
    Symbol('sgl:authors'): "Dmytro Kolibabchuk"
}