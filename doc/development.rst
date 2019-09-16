=================
Development notes
=================

This project uses `pipenv` to manage python dependecies. The `requirements.txt`
is generated accordingly. Please refer to http://docs.pipenv.org for more
information. The `Pipfile` has some development dependencies (`-d` option of
`pipenv`), they concerns mainly static code analysis tools and documentation
building.

Development environment can be setup using the normal setuptools workflow, in a
pipenv environment:

.. code-block:: console

    cd clalogger
    pipenv shell
    python setup.py develop

.. note::
    Since ``python setup.py develop`` "installs" the package out of the pipenv
    control, using ``pipenv clean`` will drop the package, so that ``python
    setup.py develop`` has to be re-executed


The code can be verified versus style, conventions, bad patterns and risks
using the ``codequality/check.sh`` script. The conventions are the ones of the
author (e.g. camel case, etc.) and shall not be changed. Anyway, exceptions are
allowed (`pylint: disable=`, `noqa`, `nosec`, etc.) but reason of the exception
must be clearly documented using comments. 

.. warning::
    The target is to avoid committing non-compliant.

    In any case, a build cannot contain non-compliant code.
