# Intake

[![Join the chat at https://gitter.im/codeforamerica/intake](https://badges.gitter.im/codeforamerica/intake.svg)](https://gitter.im/codeforamerica/intake?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

[![Build Status](https://travis-ci.org/codeforamerica/intake.svg?branch=master)](https://travis-ci.org/codeforamerica/intake) [![Test Coverage](https://codeclimate.com/github/codeforamerica/intake/badges/coverage.svg)](https://codeclimate.com/github/codeforamerica/intake/coverage) [![Code Climate](https://codeclimate.com/github/codeforamerica/intake/badges/gpa.svg)](https://codeclimate.com/github/codeforamerica/intake) 
[![Requirements Status](https://requires.io/github/codeforamerica/intake/requirements.svg?branch=master)](https://requires.io/github/codeforamerica/intake/requirements/?branch=master)

## Requirements
To get a local version of intake running, you'll need to have the following installed:
*   [python 3.5](https://github.com/codeforamerica/howto/blob/master/Python-Virtualenv.md) (note that python 3.5 includes venv, a standard library module. A separate installation of virtualenv is  unnecessary)
*   [Node.js and npm](https://github.com/codeforamerica/howto/blob/master/Node.js.md)
*   [Gulp](https://github.com/gulpjs/gulp/blob/master/docs/getting-started.md), simply follow step 1 to enable the `gulp` command from your terminal.
*   [Local PostreSQL](https://github.com/codeforamerica/howto/blob/master/PostgreSQL.md)

## Installation and Setup

### Quickstart

An overview of the command line steps to get started
```
git clone https://github.com/codeforamerica/intake.git
cd intake
createdb intake
cp ./local_settings.py.example ./local_settings.py
# add database connection info to local_settings.py
python3 -m venv .
source bin/activate
make install
./manage.py collectstatic
make db.setup  # migrate the database and add seed data
make serve   # run the server
```

### Installation

Be sure to install all the dependencies in a python virtual environment. `make install` will install both npm packages as well as python packages.

```
git clone https://github.com/codeforamerica/intake.git
cd intake
python3 -m venv .  # or virtualenv .
source bin/activate
make install
```

### Copy the local settings

```
cp ./local_settings.py.example ./local_settings.py
```


### Set up the database

Make sure you have a local PostgreSQL database, and that you know the login information. Add this database information to `local_settings.py`. If you're not sure how to setup a PostgreSQL database, [read more documentation]([Local PostreSQL](https://github.com/codeforamerica/howto/blob/master/PostgreSQL.md)) before proceeding.

For example, if I have a default user named `postgres`:

```
# create a database named "intake"
createdb intake
```

```python
# in local_settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'intake',
        'USER': 'postgres',
    }
}
```


With the database connection information in place, the following command will migrate the database and add seed data:

```
make db.setup
```


### Build static assets

This only needs to be run the first time you set up.

```
./manage.py collectstatic
```

## Run the local server

The following command will spin up a local server at [http://localhost:8000/](http://localhost:8000/)

```
make serve
```

## Testing

To run the test suite, use:
```
make test
```


If you'd like to see coverage results you can use:
```
make test.coverage
```

To target a particular test, you can add a `SCOPE` variable. For example if I want to just test that an org user can only see applications to their own organization on the app index page, I would run:
```
make test \
SCOPE=intake.tests.views.test_admin_views.TestApplicationIndex.test_that_org_user_can_only_see_apps_to_own_org
```

As you can see, the `SCOPE` variable should use the syntax of a python import path.

