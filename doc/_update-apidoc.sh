cd $(dirname $0)
rm -fr api
sphinx-apidoc -o api --force --module-first ../src/clalogger
