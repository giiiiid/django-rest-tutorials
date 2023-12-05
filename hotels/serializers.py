from rest_framework import serializers
from .models import Hotel

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['name', 'location', "token"]
        read_only_fields = ["token"]

        def create(self, validated_data):
            hotel = Hotel.objects.create(**validated_data)
            return hotel