#!/bin/bash
source .flaskenv

until flask db upgrade
do
    echo "Waiting for database..."
    sleep 2
done

exec gunicorn -b :5000 --access-logfile - --error-logfile - microblog:app