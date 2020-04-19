from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from auth_.models import MyUser, Profile


class InlineProfile(admin.StackedInline):
    model = Profile
    verbose_name = 'Profile'
    verbose_name_plural = 'Profiles'
    can_delete = False


@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    inlines = [InlineProfile,]
    list_display = ('id', 'username', 'email',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'bio', 'address', 'user',)