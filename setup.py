from cx_Freeze import setup, Executable

base = None
executables = [Executable("__main__.py", base=base)]

packages = []


setup(
    name = "Minesweeper",
    version = "1.0",
    description = 'Text based minesweeper',
    executables = executables
)
