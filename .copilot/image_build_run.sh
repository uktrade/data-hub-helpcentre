#!/usr/bin/env bash

# Exit early if something goes wrong
set -e
export $(grep -v '^#' sample.env | xargs)
python manage.py compilescss
python manage.py collectstatic --noinput
# Add commands below to run inside the container after all the other buildpacks have been applied
