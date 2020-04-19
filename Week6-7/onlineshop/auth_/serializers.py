from rest_framework import serializers

from auth_.models import MyUser


class UserSerializer(serializers.ModelSerializer):
    # password = serializers.CharField()
    class Meta:
        model = MyUser
        fields = ('id', 'username', 'password', 'email',)