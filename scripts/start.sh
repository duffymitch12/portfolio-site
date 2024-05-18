#!/bin/bash

echo "----Starting up Virtual Env----"
source venv/bin/activate

echo "----Starting Local Development Server----"
FLASK_APP=app.py FLASK_ENV=development flask run --host=localhost --port=8000
