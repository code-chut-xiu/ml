#!/usr/bin/env bash
echo "Creating a virtual environment"
python3 -m venv ./venv

echo "Activate the virtual environment"
source ./venv/bin/activate

echo "Running pip install for Tensorflow, spaCy, and boto3"
pip install -U tensorflow
pip install -U spacy
pip install -U boto3

