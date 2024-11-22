#!/usr/bin/env bash

# Exit early if something goes wrong
set -e
pip install -r requirements.txt

# Add commands below to run inside the container after all the other buildpacks have been applied
