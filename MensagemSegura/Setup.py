import sys
from cx_Freeze import setup, Executable

# COMANDO: python .\Setup.py build

build_exe_options = {"packages": ["os"], "includes": ["PySimpleGUI"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Mensagem segura",
    version="1.0",
    description="Criptografa e descriptografa uma mensagem.",
    options={"build_exe": build_exe_options},
    executables=[Executable("Principal.py", base=base)]
)