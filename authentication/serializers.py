from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=120, write_only=True)

    class Meta:
        model = User
        fields = "__all__"
    
    def create_user(self, validated_data):
        already_exists_user = validated_data.get("username")

        if already_exists_user:
            validated_data.pop("username")
        user = User.objects.create_user(**validated_data)
        
        return user