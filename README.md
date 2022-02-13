# ipython-profile

A slightly opinionated template for iPython configuration for interactive development.
**Auto-reload** and **no imports** for packages and modules in the project.

## Usage

Install the library using your favorite package manager:
```bash
# With poetry
poetry add ipython-profile

# With pip
pip install ipython-profile
```

Now you can use `ipython-profile` in the project directory:
```bash
$ cd ~/awesome-project
$ ipython-profile            # If installed with pip
$ poetry run ipython-profile # If installed locally with poetry
[ipython-profile] Created .ipython-profile directory with default config.
[ipython-profile] It seems that you are using git in this project. Consider adding .ipython-profile to .gitignore.
Python 3.9.6 (default, Jun 29 2021, 05:25:02)
Type 'copyright', 'credits' or 'license' for more information
IPython 8.0.1 -- An enhanced Interactive Python. Type '?' for help.

IPython profile: .ipython-profile

In [1]:
```

It loads modules automatically (magic!) if the called name wasn't found in the environment using [ipython-autoimport](https://github.com/anntzer/ipython-autoimport).

It also automatically reloads modules on changes using [iPython autoreload extension](https://ipython.readthedocs.io/en/stable/config/extensions/autoreload.html).

```python
In [1]: requests.get('https://google.com/')
Autoimport: import requests
Out[1]: <Response [200]>

In [2]: libs.auth.get_token()
Autoimport: import libs
Autoimport: import libs.auth
Out[2]: 1

In [3]: # I'm changing libs/auth.py

In [4]: libs.auth.get_token()
Out[4]: 2
```

`ipython-profile` by default creates an iPython profile directory in `./.ipython-profile`.
If you want to set a different directory, use `--profile-dir` option.

## How it works?

The template is small and straightforward underneath: it installs `ipython-autoimport` and creates this iPython configuration file:
```python
## lines of code to run at IPython startup.
#  Default: []
c.InteractiveShellApp.exec_lines = [
    '%autoreload 2'
]

## A list of dotted module names of IPython extensions to load.
#  Default: []
c.InteractiveShellApp.extensions = ['autoreload', 'ipython_autoimport']
```

Basically, it enables auto-import and auto-reload for all modules.

In the future the profile might include some tools to simplify using it with web frameworks (Django, FastAPI) and testing frameworks.
