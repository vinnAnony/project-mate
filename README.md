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
