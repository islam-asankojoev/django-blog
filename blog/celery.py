import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')

app = Celery('blog')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'parsing_5_news_from_sputnik.kg_everyday': {
        'task': 'news.tasks.parsing',
        'schedule': crontab(minute='*/1'),
    },
}
