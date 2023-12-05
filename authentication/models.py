from django.db import models
from django.contrib.auth import settings
import jwt
from datetime import timedelta
# Create your models here.

class Profile(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    
    @property
    def token(self):
        token = jwt.encode(
            {"username":self.username, "password":self.password, "exp":timedelta(minutes=30)},
            settings.SECERET_KEY, algorithm="HS26"
        )
        return token