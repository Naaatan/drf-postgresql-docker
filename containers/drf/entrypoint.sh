#!/bin/sh
python manage.py makemigrations --noinput
python manage.py migrate --noinput
# シェルスクリプトでは`[`と`$DEBUG`、`True`と`]`の間にスペースを一つ空けておかないと[]内の式を認識できないので注意
if [ $DEBUG = 'True' ]; then
    python manage.py runserver 0.0.0.0:8000
else
    python manage.py collectstatic --noinput
    python manage.py runserver 0.0.0.0:8000
fi