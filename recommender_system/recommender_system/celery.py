import os


from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recommender_system.settings')

app  =  Celery('recommender_system')


# CELERY
app.config_from_object('django.conf:settings', namespace='CELERY')

# app.conf.broker_url = 'redis://localhost:6379/0' # this is the default value if we don't specify it in settings.py of django project
# app.conf.result_backend = 'redis://localhost:6379/0' # this is the default value if we don't specify it in settings.py of django project
# The result_backend is the place where Celery will store the results of the tasks that it executes, like the return value of the task.
# The result backend can be a database, a message broker like Redis, or even a file system.
# The result backend can be used to store the results of of recommendations, so that we can retrieve them later.

app.autodiscover_tasks()

app.conf.beat_scheduler = {
    "run_movie_rating_avg_every_30": {
        'task': 'task_calculate_movie_ratings',
        'schedule': 60 * 30, # 30 minutes
        'kwargs': {'count': 20_000}
}
}