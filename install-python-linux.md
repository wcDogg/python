# Install Multiple Versions of Python on Linux

Tools like Nox run tests against multiple versions of Python. Here's how to use [pyenv](https://github.com/pyenv/pyenv) to manage multiple versions of Python and make those versions available during testing.


# Existing Python?

I've used distros where no Python is installed and where multiple versions are installed. If it's reasonable, go for a blank slate by uninstalling existing Python.

```bash
# See what's there
dpkg -l

# Purge
sudo apt purge python3 
sudo apt purge python3.10 

# Clean up after purge
sudo apt autoremove
sudo apt clean
```

# Install pyenv

```bash
# Install pyenv from ~/
curl https://pyenv.run | bash

# Set up Bash
# https://github.com/pyenv/pyenv#set-up-your-shell-environment-for-pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc

# Restart shell
exec "$SHELL"

# Install build dependencies
# https://github.com/pyenv/pyenv/wiki#suggested-build-environment
sudo apt update
sudo apt -y install make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```

## Install Python

```bash
# List versions that can be installed
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

## Install pipx

Use [pipx](https://pypa.github.io/pipx/) to install end-user apps that should be available across projects - Nox, Scrapy, Poetry.

```bash
# Install
pip install --user pipx

# Note path warnings
WARNING: The script userpath is installed in '/home/wcd/.local/bin' which is not on PATH.
WARNING: The script pipx is installed in '/home/wcd/.local/bin' which is not on PATH.

# Add the needed path to .bashrc
echo 'export PATH=$PATH:"/home/wcd/.local/bin"' >> ~/.bashrc
exec "$SHELL"

# Restart shell and test
pipx

# Update
python -m pip install --user -U pipx

# Install a package
# https://pypa.github.io/pipx/examples/
pipx install pycowsay
```

## Make Multiple Versions Available

When it’s time to run Nox tests, make all the needed versions available by running this in the project directory:

```bash
pyenv local 3.7.9 3.8.10 3.9.13 3.10.6
```

## venv

Tools like Poetry + Scrapy create their own virtual environments. For other projects, you need to create a virtual environment. Here's how.

```bash
# Create a project directory and cd into it
mkdir test-project
cd test-project

# Create virtual environment
python -m venv venv

# Activate environment
source venv/bin/activate
# Prompt now displays [venv]

# Install the minimums
python -m pip install --upgrade pip setuptools wheel

# Open folder in VS Code
code .

# Deactivate venv in bash
deactivate
```
