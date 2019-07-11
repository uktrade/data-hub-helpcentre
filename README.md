# data-hub-helpdesk

## Getting started

### Local Development

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
export $(cat .env)
cd helpdesk
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```


