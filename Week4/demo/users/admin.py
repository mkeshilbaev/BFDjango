from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import MyUser

@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
    )