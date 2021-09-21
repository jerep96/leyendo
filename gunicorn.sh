#!/bin/bash
cd /var/www/leyendo
#source venv/bin/activate
gunicorn social_django.wsgi -t 600 -b 0.0.0.0:8000 -w 6 --user=root --log-file=/var/www/leyendo/gunicorn.log