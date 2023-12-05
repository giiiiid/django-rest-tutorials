from django.db import models
import jwt
from django.contrib.auth import settings
from datetime import timedelta, datetime
# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.location

class Hotel(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=50)

    @property
    def token(self):
        token = jwt.encode(
            {"name":self.name, "location":self.location, "exp":datetime.utcnow() + timedelta(minutes=30)},
            settings.SECRET_KEY
        )
        return token

    def __str__(self):
        return self.name
