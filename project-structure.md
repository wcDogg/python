# Project Structure


## A simple command line tool

```
F: project
  .env
  .gitignore
  README.md
  setup.py
  _init_.py
  configure.py 
  app.py
```

## A more complex app

```
F: project
  .env
  .gitignore
  README.md
  setup.py
  /app
    _init_.py
    configure.py
    main.py
    /modules
      _init_.py
    /helpers
      _init_.py
    /tests
      _init_.py
    /assets
  /docs
```

## Project Directory

OS agnostic way to capture the project's root path.

```
from pathlib import Path

# In a file at project root
DIR_PROJECT = Path(__file__).parent

# In a project subdirectory
DIR_PROJECT = Path(__file__).parent.parent
```


## About `appdirs`

`appdirs` + `pathlib` provide an OS-agnostic way to get common system directories. Not to be confused with `os.path` module - shared syntax, main difference is with `open()`

* See `configure.py`
* https://pypi.org/project/appdirs/
* https://docs.python.org/3/library/pathlib.html


## About `python-decouple`

How to use a `.env` file + `python-decouple` to use sensitive data - like API keys - without revealing them in the app.

The advantage of [python-decouple](https://pypi.org/project/python-decouple/) over other `.env` methods is the ability to 'cast' variables as the correct data type. I arrived at `python-decouple` because other `.env` methods conflict with Tkinter file dialogs (weird but true). 

* See `.env` and `configure.py`
* https://pypi.org/project/python-decouple/

**Create a `.env` file.**

This file stores sensitive data. 

* Be sure to **add `.env` to `.gitignore`**. 
* Supply a `.env.example` as needed. 

**Add secrets to `.env` file.**
```
SECRET_STRING = 'lsiuidu457sd2768_gh4879`
SECRET_FLOAT = 42.57
SECRET_BOOL = True
```
**Create Globals in `.configure`**
```
from decouple import config

TEST_STR = config('SECRET_STRING')
TEST_INT = config('SECRET_FLOAT', cast=float)
TEST_BOOL = config('SECRET_BOOL', default=False, cast=bool)
```


