from django.db import models


class Airport(models.Model):

    RATES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )

    COUNTRIES = (
        ('Japan', 'Japan'),
        ('Korea', 'Korea'),
        ('Singapore', 'Singapore'),
        ('Australia', 'Australia'),
        ('Germany', 'Germany'),
    )

    title = models.CharField('Airport Name', max_length=50)
    body = models.TextField(blank=True)
    country = models.CharField('country', choices=COUNTRIES, max_length=50)
    created_at = models.DateTimeField('date created')
    image1 = models.ImageField(upload_to='', blank=True, null=True, default='noimage.png')
    image2 = models.ImageField(upload_to='', blank=True, null=True, default='noimage.png')
    image3 = models.ImageField(upload_to='', blank=True, null=True, default='noimage.png')
    image4 = models.ImageField(upload_to='', blank=True, null=True, default='noimage.png')
    image5 = models.ImageField(upload_to='', blank=True, null=True, default='noimage.png')
    rate = models.IntegerField(choices=RATES)

    class Meta:
        db_table = 'airports'
        verbose_name_plural = 'Airports'

    def __str__(self):
        return self.title
