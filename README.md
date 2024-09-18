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

### Add entry to hosts
Append entry `127.0.0.1       data-workspace-sso.test` to hosts file (probably located at /etc/hosts).

### Set up and run the site:

```bash
make migrate
make front-end
make up
```

### Superuser privileges
These are needed to develop on the CMS site of the platform in Wagtail. Go to the user.user table in the helpcentre database (running in Postgres container locally) and change the value of 'is_superuser' to true on your test user (vyvyan.holland@email.com).

### Run website locally

Browse the website at http://localhost:8000

## Run unit tests

```bash
make test
```

## Changing requirements files

Make any changes using poetry, then run:

```bash
make all-requirements
```

## Building the front end styles

```bash
make front-end
```

## Accessing Wagtail Admin
