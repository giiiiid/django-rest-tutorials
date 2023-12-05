from django.db import models
from django.contrib.auth.models import User
import jwt
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=200, unique=True, default='')
    email = models.EmailField(max_length=200, unique=True, default='')
    
    def __str__(self):
        return self.username