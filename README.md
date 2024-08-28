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

### Set up and run the site:

```bash
make migrate
make front-end
make up
```

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
