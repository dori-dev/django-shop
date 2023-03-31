import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

celery_app = Celery('config')
celery_app.autodiscover_tasks()

celery_app.conf.broker_url = 'redis://localhost:6379'
celery_app.conf.result_backend = 'redis://localhost:6379'
