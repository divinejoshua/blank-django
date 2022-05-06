import os

from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoprod.settings')

app = Celery('djangoprod')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Celery beat 
app.conf.beat_schedule = {

    # The Job 1
    'add_number_job': {

        # The location of the task (appname.page.function)
        'task': 'crudapp.tasks.add_number',

        # The schelduled time 
        'schedule': crontab(minute=0, hour=0), #Execute daily at midnight.


        # 'args': (arguments if any),
    },

}

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')