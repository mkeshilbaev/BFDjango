from rest_framework import serializers
from .models import MyUser


class MyUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = MyUser
        fields = '__all__'

    def create(self, validated_data):
        user = MyUser.objects.create_user(username=validated_data['username'])
        return user