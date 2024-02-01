#!/usr/bin/env bash

# all python packages, in topological order
declare -A PROJECTS_MAP=(["taggenerator"]="core/taggenerator" ["tools"]="libs/tools" ["api"]="api")
