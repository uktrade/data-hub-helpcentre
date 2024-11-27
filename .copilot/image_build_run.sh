#!/usr/bin/env bash

# Exit early if something goes wrong
set -e
# Taken from circle ci config 
export ALLOWED_HOSTS='["*"]'
export CSRF_TRUSTED_ORIGINS='["https://*"]'
export DJANGO_SETTINGS_MODULE="config.settings.test"
export DATABASE_URL="postgres://postgres:postgres@localhost:5432/helpcentre"
export SECRET_KEY="test"
export AUTHBROKER_CLIENT_ID="not_the_real_client_id"
export AUTHBROKER_CLIENT_SECRET="not_the_real_client_secret"
export AUTHBROKER_URL="https://url.to.sso"
export FEED_API_TOKEN="test"
export FEEDBACK_URL="http://path.to.feedback"
export DEBUG="True"
python manage.py compilescss
python manage.py collectstatic --noinput
# Add commands below to run inside the container after all the other buildpacks have been applied
