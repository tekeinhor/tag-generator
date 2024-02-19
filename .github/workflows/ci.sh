#!/usr/bin/env bash

create_ecr_repo () {
    REPO_NAME=$1
    echo "repository name: ${REPO_NAME}"
    aws --version
    #redirect stdout in case of success and stderr otherwise, in output
    output=$(aws ecr describe-repositories --repository-names ${REPO_NAME} 2>&1)
    # store the exit code of the previous cmd
    status_code=$?
    echo "status of cmd: ${status_code}"
    if [ $status_code -ne 0 ]; then # cmd was not successfull
        if echo ${output} | grep -q RepositoryNotFoundException; then
            echo "echo repository doesn't exist, will create it"
            aws ecr create-repository --repository-name ${REPO_NAME}
            echo "created ${REPO_NAME}"
        else
        # redirect output to stderr if the error different from RepositoryNotFoundException
        >&2 echo ${output}
        fi
    else
        echo "repository already exist"
    fi
}