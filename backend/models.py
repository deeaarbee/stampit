from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager


class CustomUserManager(UserManager):
    def create_superuser(self, username, email, password, **extra_fields):
        super().create_superuser(email=email, password=password,
                                 username=username, is_superuser=True)


class User(AbstractUser):
    objects = CustomUserManager()

