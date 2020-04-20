from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager, AbstractUser
from django.db import models


class MyUser(AbstractUser):
    USER_ROLES = (
        (1, 'admin'),
        (2, 'editor'),
    )
    role = models.IntegerField(choices=USER_ROLES)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f'{self.id}: {self.username}'


class Profile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500)
    address = models.CharField(max_length=300)

    def __str__(self):
        return self.user.username

