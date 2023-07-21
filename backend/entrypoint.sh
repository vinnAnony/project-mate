#!/bin/sh

deploy(){

	python manage.py migrate

	python manage.py setup_admin

	python manage.py collectstatic --no-input

	#Print wkhtmltopdf installation path - needed to be placed in environment variables
	echo "<<< wkhtmltopdf path >>>"
	which wkhtmltopdf
	echo ">>> wkhtmltopdf path <<<"

    gunicorn projectmate.wsgi:application --bind 0.0.0.0:${APP_PORT}
}

deploy