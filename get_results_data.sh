#!/bin/bash

echo "Creating results folder"
mkdir -p results && cd results
echo "Downloading result files"
wget https://zenodo.org/record/321599/files/user_study_dataset.zip
unzip user_study_dataset.zip
rm -rf user_study_dataset.zip