#!/bin/sh
set -x
set -e

DIR="$( cd "$( dirname "$0" )" && pwd )"
ROOT_DIR="${DIR}/.."

echo $ROOT_DIR 

coverage run -m pytest -vv
coverage report
coverage html
coverage xml
COVERAGE_SVG=reports/coverage.svg
genbadge coverage -i coverage.xml  -o $COVERAGE_SVG