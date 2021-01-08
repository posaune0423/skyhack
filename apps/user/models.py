from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from cloudinary.models import CloudinaryField

class User(AbstractUser):
    username = models.CharField('username', max_length=150, unique=True)
    email = models.EmailField('mail address', unique=True)
    thumbnail = CloudinaryField('media/', blank=True, null=True, default='v1610122704/media/no-user_b9riju.jpg')
    bio = models.TextField(max_length=150, blank=True)

    objects = UserManager()

    class Meta:
        db_table = 'users'
        verbose_name_plural = 'Users'
