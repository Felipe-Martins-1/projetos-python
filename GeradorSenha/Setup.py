import sys
from cx_Freeze import setup, Executable

# COMANDO: python .\Setup.py build

build_exe_options = {"packages": ["os"], "includes": ["PySimpleGUI"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Gerador de Senha",
    version="2.0",
    description="Gerador de senhas gratuito!",
    options={"build_exe": build_exe_options},
    executables=[Executable("Principal.py", base=base)]
)