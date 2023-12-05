from rest_framework import serializers
from .models import Profile

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["__all__"]

    def create(self, validated_data):
        user = Profile.objects.create(**validated_data)
        return user

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["username", "password", "token"]
        read_only_fields = ["token"]