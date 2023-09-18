#!/bin/bash


/app/env/bin/python manage.py migrate --noinput &&
if cat /var/run/gunicorn/dev.pid
then
    kill $(cat /var/run/gunicorn/dev.pid)
    rm /var/run/gunicorn/dev.pid
fi
/app/env/bin/gunicorn -c /app/core/gunicorn.conf.py
tail -f /var/log/gunicorn/dev.log
