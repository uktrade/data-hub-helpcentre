web: python manage.py migrate --noinput && python manage.py compilescss && python manage.py collectstatic --noinput && waitress-serve --port=$PORT helpcentre.wsgi:application
