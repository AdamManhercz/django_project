from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.settings")

app = Celery("food_planner")

app.conf.enable_utc = True

app.conf.update(timezone="Europe/Budapest")

app.config_from_object(settings, namespace="CELERY")

# CELERY BEAT

app.conf.beat_schedule = {
    "scrape-data":{
    "task": "food_planner.task.add_recipes_to_model",
    "schedule": crontab(hour=4, minute=0, day_of_week="*/2")
    }
}

app. autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")