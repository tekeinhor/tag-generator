#!/bin/sh
# This script reflects the latest changes of pyproject.toml
#  into both the poetry.lock file and the virtualenv.
#  by running `poetry update && poetry install --sync`
# It first configures poetry to use the right python for creation of the virtual env
set -x
set -e
DIR="$( cd "$( dirname "$0" )" && pwd )"
ROOT_DIR="${DIR}/.."
echo $DIR
echo $ROOT_DIR

poetry version
VERSION=$(poetry version | awk '{print $2}')

if [ "$(uname)" = "Darwin" ]; then export SEP=" "; else SEP=""; fi

. ${DIR}/projects.sh
_projects=$PROJECTS

echo "Running on following projects: ${_projects}"
for p in $_projects
do
  cd "${DIR}/../${p}" || exit
  # sed -i$SEP'' "s|{.*path.*|\"^$VERSION\"|" pyproject.toml
  # include project changelog
  cp  "$ROOT_DIR/CHANGELOG.md" ./
  poetry build
  mkdir -p info
  # export deps, with updated path deps
  poetry export -f requirements.txt --output ./info/requirements.txt --without-hashes --with-credentials
  sed -i$SEP'' "s/ @ file.*;/==$VERSION;/" "./info/requirements.txt"
  ls -altr ./dist/

done

# mkdir -p "${ROOT_DIR}/dist"
# for p in $_projects
# do
#   ls -altr "${ROOT_DIR}/${p}/dist/"
#   cp $FLAG "${ROOT_DIR}/${p}/dist/"*".whl" "${ROOT_DIR}/dist/"
# done
# echo "=========="
# ls -altr "${ROOT_DIR}/dist/"