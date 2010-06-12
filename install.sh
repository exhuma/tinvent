#!/bin/bash

if [ ! -d "venv" ]; then
   virtualenv --no-site-packages venv
fi

source ./venv/bin/activate || exit 1

easy_install -i http://www.turbogears.org/2.0/downloads/current/index tg.devtools
easy_install sqlalchemy
easy_install sqlalchemy-migrate
easy_install psycopg2

