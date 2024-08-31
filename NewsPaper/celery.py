import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsPaper.settings')

app = Celery('NewsPaper',
             broker='redis://:VDIYPtmGr0Itc6SCThzAATAkB9ZpeAHX@redis-17935.c258.us-east-1-4.ec2.redns.redis-cloud.com:17935/',
             backend='redis://:VDIYPtmGr0Itc6SCThzAATAkB9ZpeAHX@redis-17935.c258.us-east-1-4.ec2.redns.redis-cloud.com:17935/')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'weekly-news-digest': {
        'task': 'news.tasks.send_weekly_news',
        'schedule': crontab(hour=8, minute=0, day_of_week='monday'),
        'args': (),  # если аргументы не нужны, оставляем пустой кортеж
    },
}