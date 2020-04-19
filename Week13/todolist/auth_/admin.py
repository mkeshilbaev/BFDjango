from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from auth_.models import MyUser, Profile


@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'bio')