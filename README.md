# Initial Django with Postgres Celery and Redis

To install the weather portal, you will need to install the following:

- Python 3.11 or higher
- Virtual environement (venv)
- Django
- Create a project called project

Create .venv file in the root folder of the project. Add the following:

```# PostgreSQL settings
POSTGRES_DB=db-name
POSTGRES_USER=db-user
POSTGRES_PASSWORD=change-me

# Django settings
DJANGO_SETTINGS_MODULE=project.settings
SECRET_KEY=change-secret-key to-a-random-string
DEBUG=True

# Redis settings (optional, if you need to customize)
REDIS_URL=redis://redis:6379/0
```

To create virtual environment, run the following command:

```python3.11 -m venv venv```

To activate the virtual environment, run the following command:

```source venv/bin/activate```

To install Django, run the following command:

```pip install django~=4.2.0```

Create django project:

```django-admin startproject project .```

In the folder ./project update __init__.py with the following:

```from __future__ import absolute_import, unicode_literals
__all__ = ('celery_app',)
```

In settings.py add the following:

```# Example for Redis
CELERY_BROKER_URL = 'redis://redis:6379/0'
```





