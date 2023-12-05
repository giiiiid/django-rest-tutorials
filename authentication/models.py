from django.db import models
from typing import Any
from django.contrib.auth.models import UserManager, AbstractBaseUser
import jwt
from django.contrib.auth import settings
from datetime import timedelta

# Create your models here.
class MyUserManager(UserManager):
    def create_user(self, name:str, email:str, password:str, **extra_fields:Any) -> Any :
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email=email)
        user = self.model(name=name, email=email, **extra_fields)

        user.set_password(password)

        user.save()
        return user
    
    def create_superuser(self, name:str, email:str, password:str, **extra_fields:Any) -> Any :
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if not extra_fields.get("is_staff") == True:
            raise ValueError('is_staff must be true')
        if not extra_fields.get("is_superuser") == True:
            raise ValueError("is_superuser must be true")
        return self.create_user(name=name, email=email, password=password, **extra_fields)


class User(AbstractBaseUser):
    username = models.CharField(max_length=200, unique=False, blank=False, null=True)
    email = models.EmailField(max_length=200, unique=True, blank=False, null=True)
    # password = models.CharField(max_length=200, blank=False, null=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = MyUserManager()
    USERNAME_FIELD = 'username'

    @property
    def token(self):
        token = jwt.encode(
            {
                "username":self.username, "email":self.email,"exp":timedelta(minutes=30)
            },
            settings.SECRET_KEY, algorithm="HS26"
        )
        return token
