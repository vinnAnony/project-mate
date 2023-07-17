#!/bin/sh

deploy(){

	python manage.py migrate

	python manage.py setup_admin

	python manage.py collectstatic --no-input

	#Print wkhtmltopdf installation path - needed to be placed in environment variables
	echo "wkhtmltopdf path >>>"
	which wkhtmltopdf
	echo "wkhtmltopdf path <<<"

	#Print list of users - to get UID of a non-root user (required in some cases)
	echo "list of users >>>"
	getent passwd
	echo "list of users <<<"

    gunicorn bizcore.wsgi:application --bind 0.0.0.0:${APP_PORT}
}

deploy