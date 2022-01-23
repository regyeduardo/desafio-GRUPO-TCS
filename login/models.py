from django.contrib.auth.models import AbstractUser
from django_celery_beat.models import PeriodicTask
from django.db import models

class User(AbstractUser):
    periodic_task_id = models.OneToOneField(PeriodicTask, on_delete=models.SET_NULL, null=True)