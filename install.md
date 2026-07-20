
# Install Python on Windows 11

[UV](https://docs.astral.sh/uv/)

## 1. Install UV Globally

```powershell
# PowerShell as Admin
# Install
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Restart shell and validate
uv  --version

# Update
        uv self update

```

## 2. Install Build Tools

**Build Tools for Visual Studio** provides MSVC - a common requirement when you need to use Python bindings for C.

1. https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2022
2. Scroll down to `All Downloads` and expand the `Tools for Visual Studio` section.
3. Download `Build Tools 2026` and run installer.
4. In the main window, check the box for: `Desktop development with C++`.
5. In the right panel, use the default options. Note that `Optional > MSVC` should be checked.
6. In the bottom-right corner, click `Install`. 

### 2.1 Example Error

Installing Build Tools fixed this error from `libtiff`. 

```powershell
error: subprocess-exited-with-error
...
from numpy.distutils.core import setup, Extension
```

## 3. Install VS Code Extensions

- Microsoft Python extension for Visual Studio Code


## 4. Initialize Project + venv

```powershell

# New project and directory
cd E:
uv init test-uv

# New project and directory, no Git
cd E:
uv init test-uv --vcs none

# Existing project
cd E:\text-uv
uv init --vcs none

# Add dependencies
uv add requests

# Initialize .venv
uv run main.py

```

## 4. VS Code: venv

**Important** VS Code may display a prompt saying no Python is installed and ask if you want to install using UV. Say NO to this prompt. If needed, point the project to the venv that UV created for the project: 

1. Open the project folder in VS Code. 
2. Press `Ctrl+Shift+P` to open the Command Palette.
3. Type `Python: Select Interpreter`.
4. Choose the UV venv environment. 


## 5. For Command Line Scripts

[rich](https://rich.readthedocs.io/en/stable/introduction.html)

[typer](https://typer.tiangolo.com/)

[Textual](https://textual.textualize.io/)



