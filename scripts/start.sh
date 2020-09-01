#!/usr/bin/env bash

python manage.py makemigrations
python manage.py migrate
python manage.py seeddb --create-super-user

if [[ ${DJANGO_BIND_ADDRESS+x} ]] && [[ ${DJANGO_BIND_PORT+x} ]];
then
    echo "OK! Using custom ADRESSS $DJANGO_BIND_ADDRESS and PORT $DJANGO_BIND_PORT to set Django runserver command"
    python manage.py runserver ${DJANGO_BIND_ADDRESS}:${DJANGO_BIND_PORT}
else
    echo "Using 0.0.0.0:8000 as parameter for Django runserver command"
    python manage.py runserver 0.0.0.0:8000
fi
