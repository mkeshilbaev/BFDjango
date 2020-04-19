from django.contrib.auth.models import AbstractUser

from django.db import models

class MyUser(AbstractUser):
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f'{self.id}: {self.username}'


class Profile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    bio = models.TextField(default='')
