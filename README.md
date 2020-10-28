# data-hub-helpcentre (aka Data Services Helpcentre)

## Coding Styles

We use the following tools to maintain a consistent coding style

- [black](https://black.readthedocs.io/) - for python code formatting
- [flake8](https://flake8.pycqa.org/en/latest/) - Python code style
- [prettier](https://prettier.io/) - for javascript and sass code formatting

These style rules are enforced by CircleCI *so please check your code locally before pushing changes!*

### Quickly check coding quality locally

    make prettier
    make black
    make flake8

## Local Development - Python

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

### Set up and run the site:

```bash
make migrate
make front-end
make up
```

### Run website locally

Browse the website at http://localhost:8000

## Changing requirements files

Make any changes to requirements.in files and then run (uses pip tools - https://github.com/jazzband/pip-tools):

```bash
make all-requirements
```

## Building the front end styles

```bash
make front-end
```
