from django.db import models

from django.contrib.auth.models import User, AbstractUser, AbstractBaseUser, PermissionsMixin, UserManager


class MyUser(User):
    class Meta:
        proxy = True

