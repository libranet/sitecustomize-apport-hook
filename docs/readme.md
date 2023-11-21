[![Testing](https://img.shields.io/github/actions/workflow/status/libranet/sitecustomize-hello/testing.yaml?branch=main&longCache=true&style=flat-square&label=tests&logo=GitHub%20Actions&logoColor=fff")](https://github.com/libranet/sitecustomize-hello/actions/workflows/testing.yaml)
[![Linting](https://img.shields.io/github/actions/workflow/status/libranet/sitecustomize-hello/linting.yaml?branch=main&longCache=true&style=flat-square&label=linting&logo=GitHub%20Actions&logoColor=fff")](https://github.com/libranet/sitecustomize-hello/actions/workflows/linting.yaml)
[![Read the Docs](https://readthedocs.org/projects/sitecustomize-hello/badge/?version=latest)](https://sitecustomize-hello.readthedocs.io/en/latest/)
[![Codecov](https://codecov.io/gh/libranet/sitecustomize-hello/branch/main/graph/badge.svg?token=AFP6UMXEN5)](https://codecov.io/gh/libranet/sitecustomize-hello)
[![PyPi Package](https://img.shields.io/pypi/v/sitecustomize-hello?color=%2334D058&label=pypi%20package)](https://pypi.org/project/sitecustomize-hello/)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/libranet/sitecustomize-hello/blob/main/docs/license.md)



https://app.codecov.io/gh/libranet/sitecustomize-hello
# sitecustomize-hello



## How does it work?

We register the ``sitecustomize_help.entrypoint()``-function to the ``sitecustomize``-module that is installed by the
[sitecustomize-entrypoints](http://pypi.python.org/pypi/sitecustomize-entrypoints)-package.

The registered function will print "Hello" to the standard output.


## Installation

Install via pip:

```bash
> bin/pip install sitecustomize-hello
```

Or add to your poetry-based project:

```bash
> poetry add sitecustomize-hello
```


## Validate & Usage
After installing this package there is nothing left to do explicitly.
We can validate that the plugin work correctly by starting a python-session and checking the hello-message being printed:

```bash
> bin/python
```

```bash
bin/python
Hello.
   >>> (interactive python-shell)
```

```bash
bin/ipython
Hello.
   >>> (interactive ipython-shell)
```

```bash
bin/black
Hello.
(black output)
```

```bash
bin/pytest
Hello.
(pytest output)
```

## Registered sitecustomize-entrypoint

The ``sitecustomize_hello``-function is registered as a ``sitecustomize``-entrypoint in our pyproject.toml_:

``` toml
    [tool.poetry.plugins]
    [tool.poetry.plugins."sitecustomize"]
    sitecustomize_hello = "sitecustomize_hello:entrypoint"
```

Sitecustomize and all its registered entrypoints will be executed at the start of *every* python-process.
For more information, please see [sitecustomize-entrypoints](http://pypi.python.org/pypi/sitecustomize-entrypoints)


## Compatibility

 [![Python Version](https://img.shields.io/pypi/pyversions/sitecustomize-hello?:alt:PyPI-PythonVersion)](https://pypi.org/project/sitecustomize-hello/)
 [![PyPI - Implementation](https://img.shields.io/pypi/implementation/sitecustomize-hello?:alt:PyPI-Implementation)](https://pypi.org/project/sitecustomize-hello/)

``sitecustomize-hello``  works on Python 3.8+, including PyPy3. Tested until Python 3.11,


## Notable dependencies

- [sitecustomize-entrypoints](http://pypi.python.org/pypi/sitecustomize-entrypoints)


