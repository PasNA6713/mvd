from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone


class MapItem(models.Model):
    datetime = models.DateTimeField('datetime', default=timezone.now())

    parent_region = models.CharField('parent_region', max_length=150)
    region = models.CharField('region', max_length=150)
    address = models.CharField('region', max_length=150, blank=True, null=True)
    
    lat = models.FloatField('latitude')
    long = models.FloatField('longitude')
   
    category = models.CharField('category', max_length=150, blank=True, null=True)
    light = models.CharField('light', max_length=150, blank=True, null=True)

    def __repr__(self):
        return f'{self.datetime}/{self.region}'

    def __str__(self):
        return f'{self.datetime}/{self.region}'
