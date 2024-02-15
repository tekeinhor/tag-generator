# tag-generator
[![checks](https://github.com/tekeinhor/tag-generator/actions/workflows/checks.yaml/badge.svg)](https://github.com/tekeinhor/tag-generator/actions/workflows/checks.yaml)
![coverage](./reports/coverage.svg?dummy=8484744)


Functionally the tag-generator project aim at showcasing a NLP ML project.
The aim is to autoatically tag "a Title and a Body" of text, of say question forum like... StackOverflow.
I use the stackoverflow dataset, questions from 2008 to 2023. To showcase what an industrialised python ML project could look like.
There is three aspects to this project:

- The ML aspect where I train a model, perform a prediction with it, package it within an API and show the result with a UI.

- The Software engineer aspect where I create tools for continous integration and development

- The OPS/MLOPS aspect where each using infracsture as code, the resource for deployment are created through code.

## The project divers aspects

### The ML Aspect
- Extract, Transform (sample) and store the data
- Perform an Exploratory Data Analysis (EDA)
- Select and Train a model


### The Software Engineer Aspect

This projects use the following tools to demonstrate the ability to automatically package and deliver a projet:

🐍 Python:
- ✌🏾 Version: 3.11
- 📦 Package management: Poetry
- 🧪 Testing: Pytest, Coverage

⚒️ Code Audit Tool within [tools](./libs/tools/):
- 💄Lint: Pylama
- 📋 Formatter: black, isort
- 🔒 Security Checker: bandit, pip-audit

🚚 Release and deploy:
- 🏷️ Automatic releaser and tagger: python-semantic-release, custom bash script for release [build.sh](./scripts/build.sh)
- 🐳 Containerization: Docker

☁️ Cloud Deployment:
- 💻 Infrastructure as Code: Terraform
- 🧡 AWS: 
    - IAM Identity Center (IAM IC)
    - Elastic Container Registry (ECR)
    - Elastic Container Services (ECS)
    - Simple Storage Service (S3)

### The Ops/MLOps Aspects
I believe this to be the core MLOPs principles that
- Experiments Reproducibility
- CI/CD Automation
- Workflow Orchestration
- Model and Data versioning
- Continuous Training and Evaluation
- Monitoring

While some points would need a couple of tools and platform to be showcase, others (like below) will be adressed in this project.

🤖 CICD:
- 🕹️ Github Actions

- Workflow Orchestration and Continuous Training

- Monitoring




## The project organisation

### Structure

I use a monorepo approach to this project. It is a strategy in which the code for a number of projects is stored in the same repository.
Here we have: 
- the core ML (training and prediction) part in `core/taggenerator`
- the API in `api/`
- the UI in `ui/`
- the deployment within `iac/terraform`
- common code used within the different sub-projects under `libs/`

Below, we can find the general structure of the monorepo.

```tree
├── 📁 .github
│   └── 📁 workflow       # the github action workflow definitions
├── 📖 CHANGELOG.md       # change log doc
├── 📖 README.md          # readme doc
├── 📁 api                # api definition code
├── 📁 core
├── 📁 iac              
│   └── 📁 terraform      # resource definition and deployment code
├── 📁 libs              
│   └── 📁 tools          # code audit tool
├── 🔒 poetry.lock        # python dependencies for reproducible builds
├── ⚙️ poetry.toml         # poetry config file
├── ⚙️ pyproject.toml      # python package declaration
├── 📁 reports            # test coverage badge goes here
├── 📁 scripts            # bash script for build and test
└── 📁 ui                 # streamlit UI
```



### How to install

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

TODO: 
Caused by this warning

```
Warning: poetry-plugin-export will not be installed by default in a future version of Poetry.
In order to avoid a breaking change and make your automation forward-compatible, please install poetry-plugin-export explicitly. See https://python-poetry.org/docs/plugins/#using-plugins for details on how to install a plugin.
To disable this warning run 'poetry config warnings.export false'.
```

```bash
$ poetry self add poetry-plugin-export
```