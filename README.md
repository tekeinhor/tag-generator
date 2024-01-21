# tag-generator
[![build](https://github.com/tekeinhor/tag-generator/actions/workflows/build.yaml/badge.svg)](https://github.com/tekeinhor/tag-generator/actions/workflows/build.yaml)
[![coverage](./reports/coverage.svg?dummy=8484744)]

A simple tag-generator project to showcase MLOps principles.
- Core feature (when the training and the inference is done)
- An API, to perform the predictions
- aça ùarche streamlit UI to showcase everything
- Infrastructure as Code to create the different AWS resources


## installing the project

### dev tools

```sh
#your cwd is the root of the project
# install dev tool in side
$ poetry install

# spawn a poetry venv
$ poetry shell

# run the different script for lintint, formatting and testing.
$ poetry run fmt
$ poetry run lint
$ poetry run all
$ poetry run pytest

# if you want to lint a specific subproject
# poetry run fmt -p relative_path_to_project
$ poetry run fmt -p libs/tools
$ poetry run fmt -p core

# exit the venv
$ exit (or deactivate)

```


For mypy to work correctly it requires
```sh
# install mypy stubs
$ mypy --install-types
```