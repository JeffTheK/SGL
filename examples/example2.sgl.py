
from sgl.interpreter import exec_string
from sgl.stdlib import STD_ENV
CODE = "(print (new-str This program was made in SGL and bundled into exe))"
exec_string(CODE, STD_ENV)
