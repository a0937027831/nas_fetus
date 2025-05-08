#!/bin/sh

set -e

python manage.py collectstatic --noinput
python manage.py wait_for_db
# 自動產生 migration（若無變動則跳過）
python manage.py makemigrations --noinput
python manage.py migrate

uwsgi --socket :9000 --workers 4 --master --enable-threads --module fetus.wsgi