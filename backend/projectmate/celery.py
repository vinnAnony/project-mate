import os

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projectmate.settings")
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1') #to fix error in Windows host

app = Celery("projectmate")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()