# celery.py

import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'healthmate.settings')

app = Celery('healthmate')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    'import-menu-daily': {
        'task': 'menu.task.fetch_and_update_menu',
        'schedule': crontab(minute=0, hour=8),
    },
}

app.conf.CELERYBEAT_FIRST_RUN_DELAY = 0