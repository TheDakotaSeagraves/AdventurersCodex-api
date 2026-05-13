#!/bin/bash

rm -f db.sqlite3
python3 manage.py migrate
python3 manage.py loaddata users
python3 manage.py loaddata tokens
python3 manage.py loaddata dnd_classes
python3 manage.py loaddata races
