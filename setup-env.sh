#!/bin/bash

# Read and install packages from requirements.txt
cat requirements.txt | while read line; do
    pipenv install $line
done
