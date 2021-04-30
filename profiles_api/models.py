from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


# Create your models here.


class UserProfileManager(BaseUserManager):
    #manager for user profiles

    def create_user(self, email, name, password=None):
        #create a new user profile
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def creat_superuser(self,email,name,password):
        # Create and save new super user with given details
        user = self.creat_superuser(email,name,password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    # Database model for users in the system
    email = models.EmailField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']


    def get_full_name(self):
        #retrieve full name of the user
        return self.name

    def get_short_name(self):
        #retrive short name of the user
        return self.name

    def __str__(self):
        #returning the string representation of our user
        return self.email