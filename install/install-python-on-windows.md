# Install Multiple Versions of Python on Windows

Tools like Nox run tests against multiple versions of Python. Here's how to use [pyenv-win](https://github.com/pyenv-win/pyenv-win#python-pip) to manage multiple versions of Python and make those versions available during testing.

## Existing Python?

There's a good chance you already have Python installed. Check:

- Start > Settings > Apps > Apps & Features

Python listed here is installed at the user level. It may have been installed via the Microsoft Store or Python.org. Note it does not display the Python 2 instance used by the Windows OS.

Uninstall all Python listed here and restart your computer. In the next step we'll be using `pyenv-win` to install and manage multiple versions of Python.

## Disable Python Launchers

- Start > Manage App Execution Aliases
- Disable the App installers for `python.exe` and `python3.exe`.

## Install pyenv-win

To manage multiple Python versions, use [pyenv-win](https://github.com/pyenv-win/pyenv-win). There are several installation options. From PowerShell:

```powershell
# Install pyenv-win
Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"

# Check version
pyenv --version
```

## Check User Environment Variables

If you installed `pyenv-win` via PowerShell, these variables should already be set.

1. Start > Edit environment variables for your account.
2. In the User Variables section, confirm these are present (wcd is my user name):

```
PYENV       C:\Users\wcd\.pyenv\pyenv-win\
PYENV_ROOT  C:\Users\wcd\.pyenv\pyenv-win\
PYENV_HOME  C:\Users\wcd\.pyenv\pyenv-win\
```

3. In the User Variables section, select the `Path` variable > Edit.
4. Confirm these paths are present:

```
C:\Users\wcd\.pyenv\pyenv-win\bin
C:\Users\wcd\.pyenv\pyenv-win\shims
```

Other installation methods may require you to set them as a separate step. From PowerShell:

```powershell
[System.Environment]::SetEnvironmentVariable('PYENV',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")
[System.Environment]::SetEnvironmentVariable('PYENV_ROOT',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")
[System.Environment]::SetEnvironmentVariable('PYENV_HOME',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")

[System.Environment]::SetEnvironmentVariable('path', $env:USERPROFILE + "\.pyenv\pyenv-win\bin;" + $env:USERPROFILE + "\.pyenv\pyenv-win\shims;" + [System.Environment]::GetEnvironmentVariable('path', "User"),"User")
```

## Install Python

```powershell
# List what can be installed
pyenv install -l

# Install needed versions
pyenv install 3.7.9 3.8.10 3.9.13 3.10.6

# Confirm installed
pyenv versions

# Set the global version
pyenv global 3.10.6

# See which version is currently in use
pyenv version
python --version

# Confirm pip - should point to pyenv
pip --version

# Update the global version
python -m pip install --upgrade pip setuptools wheel

# Refresh the Python environment
pyenv rehash

# Uninstall versions
pyenv uninstall 3.10.4
```

## Install Build Tools

Work with Python long enough and eventually you'll use bindings to C libraries - for me this cam up with `libtiff`. Depending on the library, you may see an error that includes the following:

```powershell
error: subprocess-exited-with-error
...
from numpy.distutils.core import setup, Extension
```

To prevent / fix this, install [Build Tools for Visual Studio 2022](https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2022). This provides MSVC - a common requirement when you need to use Python bindings for C.

- Install Workload: Desktop development with C++ - note it has MVSVC.
- Use the default options - the MSVC box is under Optional and should be checked.


## Install pipx

Use [pipx](https://pypa.github.io/pipx/) to install end-user apps that should be available across projects - Nox, Scrapy, Poetry.

```bash
# Install
python -m pip install --user pipx

# Add to PATH
cd C:\Users\wcd\.local\bin
python -m pipx ensurepath

# Update
python -m pip install --user -U pipx

# Install a package
# https://pypa.github.io/pipx/examples/
python -m pipx install pycowsay
```

## Make Multiple Versions Available

When it's time to run Nox tests, make all the needed versions available by running this in the project directory:

```powershell
pyenv local 3.7.9 3.8.10 3.9.13 3.10.6
```
