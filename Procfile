<<<<<<< HEAD
web: bash entrypoint.sh
=======
web: python manage.py migrate --noinput && python manage.py compilescss && python manage.py collectstatic --noinput && waitress-serve --ident='' --trusted-proxy '*' --trusted-proxy-headers 'x-forwarded-proto' --port=$PORT config.wsgi:application
>>>>>>> master
