import os
from django.conf import settings
from celery import Celery


# Set the default Django settings module fo the "celery" program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce_mele.settings")

app = Celery("ecommerce_mele")

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
