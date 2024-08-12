#!/bin/bash

envName="demnistify-environment"
envConfig="environment.yml"

# Check if the environment exists
conda env list | grep -w $envName > /dev/null 2>&1
envExists=$?

if [ $envExists -eq 0 ]; then # Update the environment
    echo "Environment '$envName' exists. Checking for updates..."
    conda env update --name $envName --file $envConfig --prune
else # Create the environment
    echo "Environment '$envName' does not exist. Creating it..."
    conda env create --name $envName --file $envConfig
fi

# Activate the environment
source activate $envName
echo "Environment '$envName' is up to date and activated."