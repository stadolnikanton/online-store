import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "store.settings")

app = Celery("store")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "add-every-30-seconds": {
        "task": "shop.tasks.add",
        "schedule": 10.0,
        "args": (6, 1),
    },
    "run-every-midnight": {
        "task": "shop.tasks.scheduled_task",
        "schedule": crontab(hour=0, minute=0),
        # "schedule": 10.0,
    },
}
