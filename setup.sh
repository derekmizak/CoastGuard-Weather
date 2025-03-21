#!/bin/bash

# Function to exit script on error
exit_on_error() {
    echo "Error occurred: $1"
    exit 1
}

# Create .env file and add environment variables
echo "Creating .env file..."
cat <<EOT > .env
# PostgreSQL settings
POSTGRES_DB=db-name
POSTGRES_USER=db-user
POSTGRES_PASSWORD=$(openssl rand -base64 20)

# Django settings
DJANGO_SETTINGS_MODULE=project.settings
SECRET_KEY=$(openssl rand -base64 32)
DEBUG=True

# Redis settings (optional, if you need to customize)
REDIS_URL=redis://redis:6379/0
EOT
[ $? -eq 0 ] || exit_on_error "Failed to create .env file"

# Create a Python virtual environment
echo "Creating Python virtual environment..."
python -m venv venv
[ $? -eq 0 ] || exit_on_error "Failed to create Python virtual environment"

# Activate the virtual environment
echo "Activating Python virtual environment..."
source venv/bin/activate
pip install --upgrade pip
[ $? -eq 0 ] || exit_on_error "Failed to activate Python virtual environment"

# Install Django
echo "Installing packages"
pip install -r requirements.txt
[ $? -eq 0 ] || exit_on_error "Failed to install packages"

# Create Django project
echo "Creating Django project..."
django-admin startproject project .
[ $? -eq 0 ] || exit_on_error "Failed to create Django project"

# Update __init__.py
echo "Updating __init__.py..."
cd project
echo "from __future__ import absolute_import, unicode_literals" > __init__.py
echo "__all__ = ('celery_app',)" >> __init__.py
[ $? -eq 0 ] || exit_on_error "Failed to update __init__.py"

# Update settings.py
echo "Updating settings.py..."
echo "# Example for Redis" >> ./settings.py
echo "CELERY_BROKER_URL = 'redis://redis:6379/0'" >> ./settings.py
[ $? -eq 0 ] || exit_on_error "Failed to update settings.py"

# Create celery.py
echo "Creating celery.py..."
cat <<EOT > ./celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('project')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
EOT
[ $? -eq 0 ] || exit_on_error "Failed to create celery.py"

# Success message
echo "********************************************"
echo "Setup completed successfully!"
echo "********************************************"
