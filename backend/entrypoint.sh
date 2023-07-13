#!/bin/sh

deploy(){

	python manage.py migrate

	echo "Admin F Name: ${DJANGO_SUPERUSER_FIRSTNAME}"

	python manage.py createsuperuser --first_name=${DJANGO_SUPERUSER_FIRSTNAME} --last_name=${DJANGO_SUPERUSER_LASTNAME} --username ${DJANGO_SUPERUSER_USERNAME} --email ${DJANGO_SUPERUSER_EMAIL} --noinput

	# celery -A bizcore worker
	# celery -A bizcore  beat

	python manage.py collectstatic

    gunicorn bizcore.wsgi:application --bind 0.0.0.0:${APP_PORT}
}

deploy