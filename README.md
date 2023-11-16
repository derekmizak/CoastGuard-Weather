# Greystone Coastguard Weather Service
To install Django with Celery and Postgres, you need to install the following first:

- Python 3.11 or higher
- Docker

after cloning the repository, you will need to run setup.sh to install the required packages.
First change permission on setup.sh to make it executable:

```chmod +x setup.sh```

Then run the script:

```./setup.sh```

This will install the required packages, create local django project called project, and create a docker-compose.yml and docker file.

Django settings in ```project/settings.py``` need to be updated to include the following:

```
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG', 'False') == 'True'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': 'db',  # This should match the service name in docker-compose
        'PORT': '5432',
    }
}
```

To build docker containers, run the following command:

```docker-compose up --build```

