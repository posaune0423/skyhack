from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserManager(UserManager):
    pass


class User(AbstractUser):
    username = models.CharField(_('username'), max_length=150, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    thumbnail_path = models.ImageField(upload_to='', blank=True, null=True, default='no-user.jpg')
    bio = models.TextField(max_length=150, blank=True)

    objects = UserManager()
