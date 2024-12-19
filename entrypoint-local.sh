#!/usr/bin/env bash

set -e

python manage.py migrate --noinput

python manage.py compilescss
python manage.py collectstatic --noinput
python manage.py runserver 0.0.0.0:8000
