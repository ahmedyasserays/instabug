#!/bin/sh

set -e

python manage.py collectstatic --noinput
python manage.py migrate --noinput
gunicorn --workers 2 --bind 0.0.0.0:4000 --preload instabug.wsgi:application
