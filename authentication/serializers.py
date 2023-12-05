from rest_framework import serializers
from .models import UserProfile
from django.contrib.auth.models import User

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ["username", "email"]
    
    def create_user(self, **validated_data):
        user = User.objects.create_user(**validated_data)
        profile = UserProfile.objects.create(user=user, **validated_data)
        return user