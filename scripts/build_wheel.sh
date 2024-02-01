#!/bin/sh
# This script reflects the latest changes of pyproject.toml and does the following
# - get the versions of the differents packages
# - build the different packages
# - create a dependency tree of all the packages (a depends on b and c)
# - based on the dependency copy the wheel of b and c in a
# set -x
# set -e
DIR="$( cd "$( dirname "$0" )" && pwd )"
readonly ROOT_DIR="${DIR}/.."
readonly deps_wheel_destination="deps"


if [ "$(uname)" = "Darwin" ]; then export SEP=" "; else SEP=""; fi

# retrieve map from project.sh file
. ${DIR}/projects.sh

declare -A PKG_WHEEL_NAMES
echo "Extracting versions on projects..."
for pkg_path in ${PROJECTS_MAP[@]}; do 
    cd "${DIR}/../${pkg_path}" || exit
  
    # for each pkg_path retrieve the package and its version
    pkg_name=$(poetry version | awk '{print $1}')
    pkg_version=$(poetry version | awk '{print $2}')
  
    # create a dict with pkg_name and their corresponding wheel location
    PKG_WHEEL_NAMES[$pkg_name]="${pkg_name}-${pkg_version}-py3-none-any.whl"
done


declare -A pkg_dependencies_tree
echo "Running on following projects: ${PROJECTS_MAP[@]}"

for pkg_name in ${!PROJECTS_MAP[@]}; do
  echo "Processing ${pkg_name}..."
  echo "--------------------------------------------------------------------"

  pkg_path=${PROJECTS_MAP[${pkg_name}]}

  cd "${DIR}/../${pkg_path}" || exit
  
  # include project changelog
  cp  "$ROOT_DIR/CHANGELOG.md" ./

  # build package and export deps
  poetry build -q
  mkdir -p info
  requirements_path="./info/requirements.txt"
  poetry export -f requirements.txt --output ${requirements_path} --without-hashes --with-credentials


  # create dependencies tree for the current pkg
  echo "Creating dependencies map ${pkg_path}"
  before_txt="\(\S*\) @ file:.*$"
  replace_with="\1"
  readarray -t dependencies < <(sed -n "s/$before_txt/$replace_with/p" "./info/requirements.txt")
  pkg_dependencies_tree[$pkg_name]=${dependencies[@]}


  # updated path for local packages with their wheel files
  echo "Replacing pkg with their local wheel file: ${pkg_path}"
  for pkg_name in ${!PKG_WHEEL_NAMES[@]}; do
    findValue=${pkg_name}
    before_txt="\($findValue\) @ file:.*"
    replace_with="./${deps_wheel_destination}/${PKG_WHEEL_NAMES[$findValue]}"
    sed -i$SEP'' "s#$before_txt#$replace_with#" "./info/requirements.txt"
  done

  # see content of build folder
done

echo "Copying wheels..."

# based on the dependencies tree copy the wheel of b and c in a (when a depends on b and c)
for pkg_name in ${!PROJECTS_MAP[@]}
do
  for dep_pkg_name in ${pkg_dependencies_tree[${pkg_name}]}
  do
    echo "copy ${dep_pkg_name} to ${pkg_name} deps folder"

    project_path=${PROJECTS_MAP[${dep_pkg_name}]}
    SOURCE="${ROOT_DIR}/${project_path}/dist/${PKG_WHEEL_NAMES[${dep_pkg_name}]}"
    DEST="${ROOT_DIR}/${PROJECTS_MAP[${pkg_name}]}/${deps_wheel_destination}/"

    echo "xxxxxxxxxxxxx" $SOURCE $DEST
    mkdir -p "${ROOT_DIR}/${PROJECTS_MAP[${pkg_name}]}/${deps_wheel_destination}"
    cp $FLAG $SOURCE $DEST
  done
done
