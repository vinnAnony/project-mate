# ProjectMate

A web app to help in management of an organization - to manage project, invoicing and payments.

## Features

ProjectMate provides the following features:

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
- [x] Create, edit and delete payments (clients' invoices and also pay-outs)
- [ ] Encrypted credentials manager with MFA
- [ ] User profile management
- [x] Mpesa integration

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
docker build -t projectmate-django .
```

- Run docker container image:

```yaml
docker run -it -p 8000:8000 --env-file .env projectmate-django
```

#### Creating database and database user

```yaml
CREATE DATABASE projectmate;

CREATE USER projectmate_user WITH PASSWORD 'pa$$word';

GRANT ALL PRIVILEGES ON DATABASE projectmate TO projectmate_user;
```

- Modify a few of the connection settings for your user to speed up database operations.

```yaml
ALTER ROLE projectmate_user SET client_encoding TO 'utf8';

ALTER ROLE projectmate_user SET default_transaction_isolation TO 'read committed';

ALTER ROLE projectmate_user SET timezone TO 'UTC';
```

> In case you get migration issues (permission denied for schema public), run the below command to add db user as the database owner

```yaml
GRANT CREATE ON SCHEMA public TO projectmate_user;
ALTER DATABASE projectmate OWNER TO projectmate_user;
```

#### Running Celery

- Run celery scheduler - for periodic tasks

```yaml
celery -A projectmate  beat -l info
```

- Run celery background worker

```yaml
celery -A projectmate worker -l info
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

#### Mpesa Integration

- Set all the required credentials values in the .env file

> Note: For B2C, the certificate is required and should be placed in the **`backend/mpesa/certs/`** folder. The name of the certificate file should be either 'sandbox' or 'production', the appropriate one will be used depending on your MPESA_ENVIRONMENT.

> I have included both the sandbox and production cert files provided from the Daraja API.
