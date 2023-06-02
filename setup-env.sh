#!/bin/bash

# Read and install packages from requirements.txt
cat req.txt | while read line; do
    pipenv install $line
done
