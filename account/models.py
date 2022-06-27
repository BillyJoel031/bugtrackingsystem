from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_admin = models.BooleanField('Is admin', default=False)
    is_manager = models.BooleanField('Is manager', default=False)
    is_developer = models.BooleanField('Is developer', default=False)
    is_tester = models.BooleanField('Is tester', default=False)

