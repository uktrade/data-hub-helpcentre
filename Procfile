web: python app/manage.py migrate && gunicorn --worker-class=gevent --worker-connections=$GUNICORN_CONNECTIONS --workers $GUNICORN_WORKERS helpcentre.wsgi:application --bind 0.0.0.0:$PORT
