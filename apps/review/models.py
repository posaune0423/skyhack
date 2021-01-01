from django.db import models

from apps.airport.models import Airport
from apps.user.models import User


class Review(models.Model):

    RATES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )

    title = models.CharField(max_length=150)
    body = models.TextField(blank=True)
    created_at = models.DateField('date created')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE, default="")
    rate = models.IntegerField(choices=RATES)

    class Meta:
        db_table = 'reviews'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return self.title
