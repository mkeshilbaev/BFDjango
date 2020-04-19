from django.contrib.auth.models import AbstractUser
from django.db import models

class MyUser(AbstractUser):
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f'{self.id}: {self.username}'


# class MyUserManager(UserManager):
#     def create_editor(self, username, email=None, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_superuser', False)
#         extra_fields.setdefault('is_editor', True)
#         return self._create_user(username, email, password, **extra_fields)
#
#
# class MyAbstractUser(AbstractBaseUser,PermissionsMixin):
#     username = models.CharField(max_length=100, unique=True)
#     first_name = models.CharField(50, blank=True)
#     last_name = models.CharField(max_length=50, blank=True)
#     email = models.EmailField(blank=True)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=False)
#     data_joined = models.DateTimeField()
#
#     objects = UserManager()
#
#     EMAIL_FIELD = 'email'
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email']
#
#     class Meta:
#         abstract = True
#         verbose_name = ('user')
#         verbose_name_plural = ('users')
#
#     def get_full_name(self):
#         full_name = '%s %s' % (self.first_name, self.last_name)
#         return full_name
#
#     def get_short_name(self):
#         return self.first_name


class Profile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500)
    address = models.CharField(max_length=300)

    def __str__(self):
        return self.user.username
