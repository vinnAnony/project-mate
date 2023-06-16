#!/bin/sh

function deploy(){

	python manage.py migrate

	# python manage.py createsuperuser --username ${SUPER_USERNAME} --email ${SUPER_EMAIL} --password ${SUPER_PASSWORD}

    python manage.py runserver 0.0.0.0:${APP_PORT}
}
cd /app/

source /opt/venv/bin/activate

deploy