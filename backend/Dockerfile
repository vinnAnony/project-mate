# Use an official Python runtime as the base image
FROM python:3.11.4-slim

# Set the working directory in the container
WORKDIR /app

# Required packages for psycopg2
RUN apt-get update
RUN apt-get install libpq-dev python3-dev gcc -y

# Install required packages for pdf generation
RUN apt-get install xvfb -y

RUN apt-get install wget -y
RUN wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.focal_amd64.deb

RUN wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2_amd64.deb
RUN dpkg -i ./libssl1.1_1.1.1f-1ubuntu2_amd64.deb
RUN rm ./libssl1.1_1.1.1f-1ubuntu2_amd64.deb

RUN wget http://archive.ubuntu.com/ubuntu/pool/main/libj/libjpeg-turbo/libjpeg-turbo8_2.0.3-0ubuntu1_amd64.deb
RUN dpkg -i ./libjpeg-turbo8_2.0.3-0ubuntu1_amd64.deb
RUN rm ./libjpeg-turbo8_2.0.3-0ubuntu1_amd64.deb

RUN apt-get install libssl1.1 libjpeg-turbo8 -y
RUN apt-get install ./wkhtmltox_0.12.6-1.focal_amd64.deb -y
RUN rm ./wkhtmltox_0.12.6-1.focal_amd64.deb

# Copy the requirements.txt file and install dependencies
COPY requirements.txt .
RUN pip install pip --upgrade
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire Django project to the container
COPY . .


EXPOSE 8000

# Link and use Railway Env variables
ARG DJANGO_SUPERUSER_FIRSTNAME
ENV DJANGO_SUPERUSER_FIRSTNAME=$DJANGO_SUPERUSER_FIRSTNAME
ARG DJANGO_SUPERUSER_LASTNAME
ENV DJANGO_SUPERUSER_LASTNAME=$DJANGO_SUPERUSER_LASTNAME
ARG DJANGO_SUPERUSER_USERNAME
ENV DJANGO_SUPERUSER_USERNAME=$DJANGO_SUPERUSER_USERNAME
ARG DJANGO_SUPERUSER_EMAIL
ENV DJANGO_SUPERUSER_EMAIL=$DJANGO_SUPERUSER_EMAIL
ARG DJANGO_SUPERUSER_PASSWORD
ENV DJANGO_SUPERUSER_PASSWORD=$DJANGO_SUPERUSER_PASSWORD

# entrypoint
CMD ["sh", "entrypoint.sh"]