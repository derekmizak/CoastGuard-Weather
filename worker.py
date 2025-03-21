import django
# ❗ needs to be called *before* importing autoreload
django.setup()

from django.utils import autoreload

def run_celery():
    # ↓ import the Celery app object from your code
    from celery import Celery
    # ↓ usual celery arguments
    args = "-A project worker --loglevel=info"

    Celery('project').worker_main(args.split(" "))

print("Starting celery worker with autoreload...")
autoreload.run_with_reloader(run_celery)
