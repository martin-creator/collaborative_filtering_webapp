import os


from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recommender_system.settings')

app  =  Celery('recommender_system')


# CELERY
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()