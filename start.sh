#!/bin/bash
python manage.py migrate
gunicorn ghorbani.wsgi