from django.db import models
from django.contrib.auth.models import User
import jwt
from django.contrib.auth import settings
from datetime import timedelta
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=200, unique=True, default='')
    email = models.EmailField(max_length=200, unique=True, default='')
    
    def __str__(self):
        return self.username
    
    @property
    def token(self):
        token = jwt.encode(
            {
                "username":self.username, "email":self.email, "exp":timedelta(minutes=30)
            },
            settings.SECRET_KEY, algorithm="HS26"
        )
        return token