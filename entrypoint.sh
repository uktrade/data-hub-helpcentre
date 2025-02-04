#!/usr/bin/env bash

set -e

python manage.py migrate --noinput

waitress-serve --ident='' --trusted-proxy '*' --trusted-proxy-headers 'x-forwarded-proto' --port=$PORT config.wsgi:application
