from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    username = models.CharField(_('username'), max_length=150, unique=True)
    email = models.EmailField(_('mail address'), unique=True)
    thumbnail = models.ImageField(upload_to='', default='no-user.jpg')
    bio = models.TextField(max_length=150, blank=True)

    objects = UserManager()

    class Meta:
        db_table = 'users'
        verbose_name_plural = 'Users'