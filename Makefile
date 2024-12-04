SHELL := /bin/bash
APPLICATION_NAME="data-hub-helpcentre"
APPLICATION_VERSION=1.0
VENV_PATH=~/Envs/traderem-api/bin

# Colour coding for output
COLOUR_NONE=\033[0m
COLOUR_GREEN=\033[32;01m
COLOUR_YELLOW=\033[33;01m


.PHONY: help test
help:
	@echo -e "$(COLOUR_GREEN)|--- $(APPLICATION_NAME) [$(APPLICATION_VERSION)] ---|$(COLOUR_NONE)"
	@echo -e "$(COLOUR_YELLOW)make prettier$(COLOUR_NONE) : Check sass files using prettier"
	@echo -e "$(COLOUR_YELLOW)make flake8$(COLOUR_NONE) : Check python files using flake8"
	@echo -e "$(COLOUR_YELLOW)make black$(COLOUR_NONE) : Check python files using black"
	@echo -e "$(COLOUR_YELLOW)make all-requirements$(COLOUR_NONE) : Generate requirements files"
	@echo -e "$(COLOUR_YELLOW)make build$(COLOUR_NONE) : docker-compose build"
	@echo -e "$(COLOUR_YELLOW)make up$(COLOUR_NONE) : docker-compose up"
	@echo -e "$(COLOUR_YELLOW)make down$(COLOUR_NONE) : docker-compose down"
	@echo -e "$(COLOUR_YELLOW)make shell$(COLOUR_NONE) : Run Django shell"
	@echo -e "$(COLOUR_YELLOW)make test$(COLOUR_NONE) : Run Django tests"
	@echo -e "$(COLOUR_YELLOW)make migrations$(COLOUR_NONE) : Create Django migrations"
	@echo -e "$(COLOUR_YELLOW)make migrate$(COLOUR_NONE) : Run Django migrate"
	@echo -e "$(COLOUR_YELLOW)make front-end$(COLOUR_NONE) : Generate front end for first use"


run = docker compose run --rm helpcentre
poetry = $(run) poetry --quiet


prettier:
	docker run -it --rm -v node_modules:/app/node_modules -v "$(CURDIR):/app" node sh -c 'cd /app && npm i && npx prettier --check "frontend/sass/**/*.{scss,js}"'

prettier-fix:
	docker run -it --rm -v node_modules:/app/node_modules -v "$(CURDIR):/app" node sh -c 'cd /app && npm i && npx prettier --write "frontend/sass/**/*.{scss,js}"'

flake8:
	$(run) flake8

black:
	$(run) black . --check

black-change:
	$(run) black .

build:
	docker compose build

up:
	docker compose up

down:
	docker compose down

shell:
	$(run) python manage.py shell

bash:
	$(run) bash

test:
	$(run) python manage.py test

migrations:
	$(run) python manage.py makemigrations

migrate:
	$(run) python manage.py migrate

front-end:
	docker run -w /app/ -it --rm --name frontend -v `pwd`:/app node bash -c 'cd /app && yarn && yarn sass'

compilescss:
	$(run) python manage.py compilescss

collectstatic:
	$(run) python manage.py collectstatic

elevate:
	$(run) python manage.py elevate_sso_user_permissions --email=$(email)