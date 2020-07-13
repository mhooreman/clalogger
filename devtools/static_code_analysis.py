#!/usr/bin/env python3

import pathlib
import subprocess
import sys

_DEVTOOLDIR = pathlib.Path(sys.argv[0]).parent.resolve()
_LIBDIR = _DEVTOOLDIR.parent.joinpath('src')
_PACKAGES = tuple(
    d.name for d in _LIBDIR.glob('*') if
    d.joinpath('__init__.py').exists()
)


class Main():
    def __init__(self):
        pass

    def __call__(self):
        self._runIsort()
        self._runFlake()
        self._runPylint()
        self._runMypy()

    def _sayRun(self, what):
        msg = "Running %s" % what
        msg = msg.upper()
        print("+-" + "-" * len(msg) + '-+')
        print("| " + msg + " |")
        print("+-" + "-" * len(msg) + '-+')

    def _runIsort(self):
        self._sayRun("isort")
        subprocess.run(
            [
                'isort', '--force-alphabetical-sort-within-sections',
                '--combine-as', '--combine-star'
            ],
            cwd=_LIBDIR
        )

    def _runFlake(self):
        self._sayRun("flake8")
        subprocess.run(
            [
                'flake8', '--ignore', 'W504', '--max-complexity', '50'
            ],
            cwd=_LIBDIR
        )

    def _runPylint(self):
        self._sayRun("pylint")
        subprocess.run(
            [
                'pylint', '--rcfile', _DEVTOOLDIR.joinpath('pylintrc'), "-rn",
            ] + list(_PACKAGES),
            cwd=_LIBDIR
        )

    def _runMypy(self):
        self._sayRun("mypy")
        subprocess.run(
            [
                'mypy', '--config-file', _DEVTOOLDIR.joinpath('mypy.ini'),
                #'-m'
            ] + list(_PACKAGES),
            cwd=_LIBDIR
        )


if __name__ == "__main__":
    Main()()
