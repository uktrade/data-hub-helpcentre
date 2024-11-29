#!/usr/bin/env bash

set -e

python manage.py migrate --noinput

if [[ -z "$COPILOT_ENVIRONMENT_NAME" ]]; then
  echo "we are on gov paas, preparing assets"
  python manage.py compilescss
  python manage.py collectstatic --noinput
fi

waitress-serve --port=$PORT config.wsgi:application
