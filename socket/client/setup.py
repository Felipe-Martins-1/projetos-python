import sys
from cx_Freeze import setup, Executable

# COMANDO: py .\setup.py build

build_exe_options = {
    "packages": ["os"],
    "includes": ["PySimpleGUI", "socket", "threading"],
}

# Para interfaces
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Cliente",
    version="1.0",
    description="",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base)],
)
