#!/bin/bash

if [ ! -d "venv" ]; then
   virtualenv --no-site-packages venv
fi

source ./venv/bin/activate || exit 1

easy_install turbogears
easy_install sqlalchemy
easy_install psycopg2

