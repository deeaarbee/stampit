from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
import datetime


def get_created_at():
    return datetime.datetime.today().timestamp()


class CustomUserManager(UserManager):
    def create_superuser(self, username, email, password, **extra_fields):
        super().create_superuser(email=email, password=password,
                                 username=username, is_superuser=True)


class User(AbstractUser):
    objects = CustomUserManager()


class Html(models.Model):

    unique_code = models.CharField(max_length=32, null=False, unique=True)
    name = models.CharField(max_length=256, null=False)
    user = models.ForeignKey(
        User,
        related_name="signatures",
        on_delete=models.SET_NULL,
        null=True,
        default=None
    )
    html_code = models.TextField(null=False)
    count = models.IntegerField(default=0)
    category = models.CharField(max_length=256)
    status = models.CharField(max_length=256, default="public")
    code_type = models.CharField(max_length=32)
    created_at = models.FloatField(null=False, default=get_created_at)
    updated_at = models.FloatField(null=False, default=get_created_at)

    def save(self, *args, **kwargs):
        self.updated_at = datetime.datetime.now().timestamp()
        super(Html, self).save(*args, **kwargs)
