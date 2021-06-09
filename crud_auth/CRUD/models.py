from django.db import models
from django.contrib.auth.models import User


class User(models.Model):

    username = models.CharField(max_length=150)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    password = User.objects.get(username='w39z').password
    # is_active = models.BooleanField(default=True)
    is_active = User.objects.get(username='w39z').is_active
    last_login = User.objects.get(username='w39z').last_login
    is_superuser = User.objects.get(username='w39z').is_superuser

    # def __str__(self):
    #     return f'Id {self.id}: {self.username}'
