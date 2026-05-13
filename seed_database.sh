#!/bin/bash

rm db.sqlite3
rm -rf ./adventurerscodexapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations adventurerscodexapi
python3 manage.py migrate adventurerscodexapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens
python3 manage.py loaddata races

