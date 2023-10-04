from django.db import models

# Create your models here.
from django.contrib.auth.models import *

class UserProfileManager(BaseUserManager):
    def create_user(self,email,first_name,last_name,password=None):
        if not email:
            raise ValueError('email not exist')
        ne=self.normalize_email(email)
        UO=self.model(email=email,first_name=first_name,last_name=last_name)
        UO.set_password(password)
        UO.save()
        return UO
    def create_superuser(self,email,first_name,last_name,password):
        Uo=self.create_user(email,first_name,last_name,password)
        Uo.is_staff=True
        Uo.is_superuser=True
        Uo.save()

class UserProfile(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(max_length=100,primary_key=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)

    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)

    objects=UserProfileManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name']
