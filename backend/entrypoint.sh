#!/bin/sh

deploy(){

	python manage.py migrate

	python manage.py createsuperuser --first_name=${DJANGO_SUPERUSER_FIRSTNAME} --last_name=${DJANGO_SUPERUSER_LASTNAME} --username ${DJANGO_SUPERUSER_USERNAME} --email ${DJANGO_SUPERUSER_EMAIL} --noinput

	# celery -A bizcore worker
	# celery -A bizcore  beat

	python manage.py collectstatic

	#Print wkhtmltopdf installation path
	echo "wkhtmltopdf path >>>"
	which wkhtmltopdf
	echo "wkhtmltopdf path <<<"

	#Print list of users
	echo "list of users >>>"
	getent passwd
	echo "list of users <<<"

    gunicorn bizcore.wsgi

	celery -A bizcore.celery:app worker --loglevel=info --uid 65534
}

deploy