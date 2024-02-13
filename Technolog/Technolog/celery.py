# Technolog/celery.py

import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Technolog.settings")

app = Celery("Technolog")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(settings.INSTALLED_APPS)


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

app.conf.beat_schedule = {
    'every': {
        'task': 'testing.tasks.repeat_order_make',
        'schedule': crontab(minute='1', hour='*'),
    },
    # },
    'writing_shutdowns':{
        'task': 'daemon.tasks.writerShutdown',
        'schedule': crontab(minute='0', hour='*'),
    },
    'test_1':{
        'task':'test1.tasks.test1',
        'schedule': crontab(minute='0',hour='*'),
    },
    'test_2':{
        'task':'test2.tasks.test2',
        'schedule': crontab(minute='0',hour='*'),
    }
}