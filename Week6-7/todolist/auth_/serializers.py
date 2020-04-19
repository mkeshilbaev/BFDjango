from rest_framework import serializers
from .models import MyUser, Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('bio', 'address')


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    profile = ProfileSerializer()

    class Meta:
        model = MyUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'profile', 'password')

    def create(self, validated_data):
        profile = validated_data.pop('profile')
        user = MyUser.objects.create_user(**validated_data)
        profile = Profile.objects.create(user=user, **profile)
        return user