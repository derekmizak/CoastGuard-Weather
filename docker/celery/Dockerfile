FROM python:3.11
# Set work directory
WORKDIR /app
# Install dependencies
COPY ./requirements.txt /app/
RUN pip install --no-cache-dir -r celery.txt
# Copy project
COPY . /app/
