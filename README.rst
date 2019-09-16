clalogger - Python logging from class point of view with easy configuration
===========================================================================

See ``doc/index.rst``
This project provides a python CaLogger class which have to be inherited and
provides logging which uses loggers based on the class name.

It also provides easy configuration features, via a `configfile` file.

Installation and requirements
-----------------------------

This requires `python >= 3.7`. It can be simply installed via `pip install
clalogger`.

Development also needs `pipenv`. You have to `cd` to the package directory and
run `pipenv shell`, followed by `pipenv install -d`. Development environment
can then easily be setup using `python setup.py develop`.

Building the documentation also requires `sphinx`. It is automatically
installed via `pipenv install d-`.