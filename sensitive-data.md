# Python & Sensitive Data

You've written a script to connect with an API. It uses your personal API key. Now you want to share the script, but not your key. Here's how to keep your sensitive data private while making it easy for others to use.

## Install `python-decouple`

The advantage of [python-decouple](https://pypi.org/project/python-decouple/) over other `.env` methods is the ability to 'cast' variables as the correct data type. I arrived at `python-decouple` because other `.env` methods conflict with Tkinter file dialogs (weird but true). 

```
py -m pip install python-decouple
```

## Create Files

At your project root create these files:

* `.gitignore`
* `.configure`
* `.env`
* `.env.example`

**IMPORTANT:** Add `.env` to `.gitignore`. 

## Add secrets to `.env` file.

```
SECRET_STRING = 'lsiuidu457sd2768_gh4879`
SECRET_FLOAT = 42.57
SECRET_BOOL = True
```

## Create Globals in `.configure`

```
from decouple import config

TEST_STR = config('SECRET_STRING')
TEST_INT = config('SECRET_FLOAT', cast=float)
TEST_BOOL = config('SECRET_BOOL', default=False, cast=bool)
```

## Supply a `.env.example`

This is a copy of `.env` with sensitive values removed. 

