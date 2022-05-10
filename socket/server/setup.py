from cx_Freeze import setup, Executable

# COMANDO: py .\setup.py build

build_exe_options = {
    "packages": ["os"],
    "includes": ["threading", "socket", "getpass4"],
}
# build_exe_options = {"packages": ["os"]}

setup(
    name="Servidor",
    version="1.0",
    description="",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=None)],
)
