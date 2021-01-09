from django.db import models
from cloudinary.models import CloudinaryField
from django_countries.fields import CountryField


class Airport(models.Model):

    RATES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )

    title = models.CharField('Airport Name', max_length=50)
    body = models.TextField(blank=True)
    country = CountryField()
    created_at = models.DateTimeField('date created')
    image1 = CloudinaryField('Image 1', blank=True, null=True, default='v1610122704/media/noimage_r2hsre.png')
    image2 = CloudinaryField('Image 2', blank=True, null=True, default='v1610122704/media/noimage_r2hsre.png')
    image3 = CloudinaryField('Image 3', blank=True, null=True, default='v1610122704/media/noimage_r2hsre.png')
    image4 = CloudinaryField('Image 4', blank=True, null=True, default='v1610122704/media/noimage_r2hsre.png')
    image5 = CloudinaryField('Image 5', blank=True, null=True, default='v1610122704/media/noimage_r2hsre.png')
    rate = models.IntegerField(choices=RATES)

    class Meta:
        db_table = 'airports'
        verbose_name_plural = 'Airports'

    def __str__(self):
        return self.title
