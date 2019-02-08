from pycountry import countries

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


COUNTRY_CHOICES = sorted((country.name, country.name) for country in countries)
# Create your models here.


class House(models.Model):
    """
    This model describes a house to be rent.
    """
    name = models.CharField(max_length=100, blank=True, default='')
    city = models.CharField(max_length=100, blank=False, default='Minsk')
    country = models.CharField(choices=COUNTRY_CHOICES, default='Belarus', max_length=100)

    number_of_rooms = models.IntegerField(blank=False, default=1, validators=[MaxValueValidator(100),
                                                                              MinValueValidator(1)])

    rating = models.IntegerField(blank=False, default=1, validators=[MaxValueValidator(5),
                                                                     MinValueValidator(1)])

    price_per_day = models.DecimalField(decimal_places=2, max_digits=10000)
    created = models.DateTimeField(auto_now_add=True)
    avaliable = models.BooleanField(default=True)

    owner = models.ForeignKey('auth.User', related_name='houses', on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)
