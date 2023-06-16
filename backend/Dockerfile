# base image
FROM python:3.11.4-alpine

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy whole project to docker home directory. 
COPY . /app

# set the work directory location of our app in the container
WORKDIR /app

# set up virtual environment
RUN python -m venv /opt/venv

# run this command to install all dependencies  
RUN /opt/venv/bin/pip install pip --upgrade && \
    /opt/venv/bin/pip install -r requirements.txt

# ENV VIRTUAL_ENV /venv
ENV PATH /venv/bin:$PATH

RUN chmod +x entrypoint.sh

# entrypoint
CMD ["sh", "entrypoint.sh"]