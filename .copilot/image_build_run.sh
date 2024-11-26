#!/usr/bin/env bash

# Exit early if something goes wrong
set -e

export COPILOT_ENVIRONMENT_NAME=nonprod

# Add commands below to run inside the container after all the other buildpacks have been applied
python manage.py compilescss
python manage.py collectstatic --noinput
