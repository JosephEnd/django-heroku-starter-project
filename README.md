# Happiness app (project structure inspiration mde-poc)

This back end is based on Django.
The stack consists of:

* [Python 3.7.3](https://docs.python.org/3.7/)
* [Django 2.2.7](https://docs.djangoproject.com/en/2.2/)


## Getting Started

1. Install [pyenv](https://github.com/pyenv/pyenv)[Python](https://www.python.org/).
1. The file `.python-version` in the root folder specifies the Python version required by this app.
   In the project root, execute `pyenv install` to install this Python version as described in `.python-version`.
1. Install [pipenv](https://pypi.python.org/pypi/pipenv) by executing `pip install pipenv --user`.
   Because of error:
   ERROR: Could not install packages due to an EnvironmentError: [Errno 13] Permission denied: '/Library/Python/2.7/site-packages/clonevirtualenv.py'
   Consider using the `--user` option or check the permissions.

1. Activate this project's virtualenv, run in project root folder `pipenv shell`.
   Alternatively, run a command inside the virtualenv with `pipenv run`.

1. NOTE!!: If altering the project or updating, rename/remove `Pipfile.lock`, change the Pipfile version
   numbers or add packages run; `pipenv update --dev`.
1. Create a new virtual environment with all dependencies by executing with `pipenv install --dev --ignore-pipfile`.
   The flag `ignore-pipfile` is used to indicate that the exact versions of the dependencies as specified in `Pipfile.lock` should be installed.
   The flag `dev` is used to also install development dependencies.

   If you run into issues due to an existing virtual environment for this app, delete that environment by executing `pipenv --rm`.

## Activating the virtual environment

Before executing any of the commands below, you need to activate the virtual environment for this app.
You can do so by executing `pipenv shell`.
Your command prompt should now indicate that you've activated the virtual environment.
It can be deactivated by executing `exit`.

## Setting environment variables

Create a file `.env` in the root of the project containing valid values for the variables listed in `.env.sample`.
Pipenv will set these environment variables each time you activate the virtual environment.

## Tests

Execute `pytest --cov=src` to run all tests once.
The flag `--cov=src` is used to display a simple report about code coverage.

Execute `pytest-watch -- --cov=src -vv --cov-report term-missing` to continuously run all tests.
The flag `--cov=src` is used to display a simple report about code coverage.
The flag `-vv` is used to trigger more verbose logging in case of failing tests.
The flag `--cov-report term-missing` is used to show the lines that are not covered by tests in the code-coverage report.

## Linting

Execute `flake8` to lint all code.

## Code formatting

Execute `black .` to format all code.


## To Do for environment Django project

- [ ] remove Yarn components.
- [ ] package.json dependency upgrades.
- [ ] upgrade general python version to 3.8.0
