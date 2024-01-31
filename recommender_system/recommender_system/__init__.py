from .celery import app as celery_app

__all__ = ('celery_app') # this __all__  dangling variable  is always used in __init__.py files to import all the modules in the current package