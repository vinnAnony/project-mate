# BizCore

A web app to help in management of an organization - especially software dev team, to manage project, invoicing and payments.

## Features

BizCore provides the following features:

- [x] User authentication and authorization
- [x] Create, edit and delete projects
- [x] Create, edit and delete clients
- [x] Linking clients to their customized projects (company products)
- [x] Manage client subscriptions to projects
- [x] Create and send invoices to clients (via email & Whatsapp)
  - [x] via email
  - [ ] via Whatsapp
- [x] Automated email reminders for almost due invoices
  - [x] (1 week)
- [ ] Create, edit and delete payments -from clients
- [ ] Encrypted credentials manager with MFA
- [ ] User profile management
### Setting up:

- Create a virtual environment and activate it:

  ```bash

          python -m venv env
          source env/bin/activate
  ```

- Install the required packages:
  ```bash
          pip install -r requirements.txt
  ```
#### Using Docker:
- Navigate to the **`backend`** folder.

- Build docker image from the Dockerfile:

```yaml
docker build -t bizcore-django .
```

- Run docker container image:

```yaml
docker run -it -p 8000:8000 --env-file .env bizcore-django
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

#### Running Celery

- Run celery scheduler - for periodic tasks

```yaml
celery -A bizcore  beat -l info
```

- Run celery background worker

```yaml
celery -A bizcore worker -l info
```

#### PDF generation

- Install dependencies

  > (Ubuntu 20.04)

```yaml
sudo apt-get update

sudo apt-get install xvfb

wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.focal_amd64.deb

sudo apt install ./wkhtmltox_0.12.6-1.focal_amd64.deb
```

> Make sure you clean up, delete the downloaded installer when done
