SHELL := /bin/bash
APPLICATION_NAME="Trade Remedies Caseworker"
APPLICATION_VERSION=1.0
VENV_PATH=~/Envs/traderem-api/bin

# Colour coding for output
COLOUR_NONE=\033[0m
COLOUR_GREEN=\033[32;01m
COLOUR_YELLOW=\033[33;01m


.PHONY: help test
help:
		@echo -e "$(COLOUR_GREEN)|--- $(APPLICATION_NAME) [$(APPLICATION_VERSION)] ---|$(COLOUR_NONE)"
		@echo -e "$(COLOUR_YELLOW)make build-docker-cli$(COLOUR_NONE) : Rebuild the dockerized environment for development"

prettier:
		docker run -it --rm -v node_modules:/app/node_modules -v "$(CURDIR):/app" node sh -c 'cd /app && npm i && npx prettier --check "frontend/sass/**/*.{scss,js}"'

flake8:
		docker run -it --rm -v requirements:/usr/local -v "$(CURDIR):/app" python sh -c "cd /app && pip install -r requirements-dev.txt && flake8 --count" 

black:
		docker run -it --rm -v requirements:/usr/local -v "$(CURDIR):/app" python sh -c "cd /app && pip install -r requirements-dev.txt && black . --check"


