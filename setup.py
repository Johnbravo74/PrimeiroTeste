#Para criar o EXE basta alterar o Executable e digitar no cmd python setup.py build
from cx_Freeze import setup, Executable
import sys

base = None

if sys.platform == 'win32':
    base = None


executables = [Executable("arrecada.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {

        'packages':packages,
    },

}

setup(
    name = "Nome Executavel",
    options = options,
    version = "1.0",
    description = 'Descricao do seu arquivo',
    executables = executables
)