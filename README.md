# Greystone Coastguard Weather Service
To install Django with Celery and Postgres, you need to install the following first:

- Python 3.11 or higher
- Docker

## Installation

For system to work, you need to create a .env file in the root directory of the project. The .env file should contain the following:

```# PostgreSQL settings
POSTGRES_DB=change-me
POSTGRES_USER=some-user-name
POSTGRES_PASSWORD=change-me-to-a-random-string

# Django settings
DJANGO_SETTINGS_MODULE=project.settings
SECRET_KEY=change-me-to-a-random-string
DEBUG=True

# Redis settings (optional, if you need to customize)
REDIS_URL=redis://redis:6379/0

ALLOWED_HOSTS = localhost, 127.0.0.1
SITE_NAME = http://localhost, http://127.0.0.1

```

To build docker containers, run the following command:


```docker-compose up -d --build```

