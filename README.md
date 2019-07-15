# data-hub-helpdesk

## Getting started

## Local Development

Pre-requisites
- python3
- pip
- docker

#### Restore dependencies

```
python3 -m venv env
source env/bin/activate

cd helpdesk
pip install -r requirements.txt
```

### Create a local env file

```
cp sample.env .env
```

Fill in the blanks for `AUTHBROKER`

```
AUTHBROKER_CLIENT_ID=you_can_get_this
AUTHBROKER_CLIENT_SECRET=from_webopp
AUTHBROKER_URL=if_you_have_access
```

#### Start docker containers

from project root
```
docker-compose up -d
```

#### Run website locally

```
source env/bin/activate
export $(cat .env)
cd helpdesk
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Animated gif support

The Wand pip package requires `imagemagick` to be installed for animated gif support

http://docs.wand-py.org/en/0.4.2/guide/install.html

https://github.com/wagtail/wagtail/issues/2505

```
brew install imagemagick
```

# Issues with local dev

## Unable to install pip dependencies

```
writing manifest file 'pip-egg-info/psycopg2.egg-info/SOURCES.txt'

    Error: pg_config executable not found.

    pg_config is required to build psycopg2 from source.  Please add the directory
```

Try 

    brew install postgresql


