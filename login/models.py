from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    periodicidade = models.IntegerField(null=True)