# BizCore

A web app to help in management of an organization - especially software dev team, to manage project, invoicing and payments.

## Features

BizMate provides the following features:

- Create, edit and delete projects
- Create, edit and delete clients
- Linking clients to their customized projects (company products)
- Create, edit and delete client subscription packages
- Create and send invoices to clients (via email & Whatsapp)
- Create, edit and delete payments -from clients
- Store encrypted credentials with MFA
- User authentication and authorization
- User profile management

> To install BizMate, follow these steps:

- Create a virtual environment and activate it:

  ```bash

          python -m venv env
          source env/bin/activate
  ```

- Install the required packages:
  ```bash
          pip install -r requirements.txt
  ```
  > To run docker image:
- Pull docker container image:

```yaml
docker pull vinnjeru/bizcore-django
```

- Run docker container image:

```yaml
docker run -it -p 8111:8111 --env-file .env vinnjeru/bizcore-django
```

#### Creating database and database user

```yaml
CREATE DATABASE bizcore;

CREATE USER bizcore_user WITH PASSWORD 'pa$$word';

GRANT ALL PRIVILEGES ON DATABASE bizcore TO bizcore_user;
```

- Modify a few of the connection settings for your user to speed up database operations.

```yaml
ALTER ROLE bizcore_user SET client_encoding TO 'utf8';

ALTER ROLE bizcore_user SET default_transaction_isolation TO 'read committed';

ALTER ROLE bizcore_user SET timezone TO 'UTC';
```

> In case you get migration issues (permission denied for schema public), run the below command to add db user as the database owner

```yaml
GRANT CREATE ON SCHEMA public TO bizcore_user;
ALTER DATABASE bizcore OWNER TO bizcore_user;
```

##### Running Celery

> Run celery scheduler - for periodic tasks

```yaml
celery -A bizcore  beat -l info
```

> Run celery background worker

```yaml
celery -A bizcore worker -l info
```
