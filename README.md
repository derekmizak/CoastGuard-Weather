# Initial Django with Postgres Celery and Redis

To install Django with Celery and Postgres, you need to install the following first:

- Python 3.11 or higher
- Docker

after cloning the repository, you will need to run setup.sh to install the required packages.
First change permission on setup.sh to make it executable:

```chmod +x setup.sh```

Then run the script:

```./setup.sh```

This will install the required packages, create local django project called project, and create a docker-compose.yml and docker file.

To build docker containers, run the following command:

```docker-compose up --build```


