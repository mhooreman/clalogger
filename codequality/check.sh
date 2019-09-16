#!/usr/bin/env bash

package=clalogger
mydir=$(realpath $(dirname $0))
prjdir=$(realpath $mydir/..)
srcdir=${prjdir}/src
libdir=${srcdir}/${package}
pylintrc=$mydir/pylintrc
setuppy=${prjdir}/setup.py

cat << EOF
================================================================================
                                RUNNING FLAKE 8
================================================================================
EOF
cd $libdir
flake8 --ignore W504 --max-complexity 50 --show-source --statistics \
    $(find . -name "*.py") $setuppy 2>&1
echo ""
cd $curdir

cat << EOF
================================================================================
                                RUNNING PYLINT
================================================================================
EOF
cd $srcdir
pylint --rcfile $pylintrc $package $setuppy 2>&1
echo ""
cd $curdir

cat << EOF
================================================================================
                          RUNNING ISORT (check only)
================================================================================
EOF
cd $libdir
isort --force-alphabetical-sort-within-sections --combine-as --combine-star \
    --check-only $(find . -name "*.py") $setuppy 2>&1
echo ""
cd $curdir

cat << EOF
================================================================================
                                RUNNING BANDIT
================================================================================
EOF
cd $srcdir
bandit --recursive $package $setuppy 2>&1
echo ""
cd $curdir

cat << EOF
================================================================================
                                RUNNING SAFETY
================================================================================
EOF
safety check 2>&1  # it checks the current environment, no pwd impact
echo ""
