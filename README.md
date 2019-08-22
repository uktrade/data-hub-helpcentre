# data-hub-helpcentre

## Local Development

Pre-requisites
- python3
- pip
- docker
- homebrew

#### Animated gif support on macOS

The Wand pip package requires `imagemagick` to be installed for animated gif support

http://docs.wand-py.org/en/0.4.2/guide/install.html

https://github.com/wagtail/wagtail/issues/2505

```bash
brew install imagemagick
```

Configure Python Dev Environment

```
python3 -m venv env
source env/bin/activate

pip install -U pip
pip install -r requirements.txt
```

### Create a local env file

```
cp app/sample.env app/.env
```

Fill in the blanks for `AUTHBROKER`

```
AUTHBROKER_CLIENT_ID=you_can_get_this
AUTHBROKER_CLIENT_SECRET=from_webopp
AUTHBROKER_URL=if_you_have_access
```

### Start the database container


```bash
docker-compose up -d
```

#### Run website locally

```bash
source env/bin/activate

python app/manage.py migrate
python app/manage.py createsuperuser

python app/manage.py runserver
```



# Issues with local dev

## macOs

### Unable to install pip dependencies

```
writing manifest file 'pip-egg-info/psycopg2.egg-info/SOURCES.txt'

    Error: pg_config executable not found.

    pg_config is required to build psycopg2 from source.  Please add the directory
```

Try 

    brew install postgresql
