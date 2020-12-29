from django.db import models
from apps.users.models import User


class Post(models.Model):

    RATES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )

    title = models.CharField(max_length=150)
    body = models.TextField(blank=True)
    country = models.CharField(max_length=150, blank=True)
    pub_date = models.DateTimeField('date published')
    image_path = models.ImageField(upload_to='', blank=True, null=True, default='noimage.png')
    image_path2 = models.ImageField(upload_to='', blank=True, null=True, default='noimage.png')
    image_path3 = models.ImageField(upload_to='', blank=True, null=True, default='noimage.png')
    image_path4 = models.ImageField(upload_to='', blank=True, null=True, default='noimage.png')
    image_path5 = models.ImageField(upload_to='', blank=True, null=True, default='noimage.png')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    rate = models.IntegerField(choices=RATES)

    def __str__(self):
        return self.title
