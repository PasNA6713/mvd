from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone


class MapItem(models.Model):
    datetime = models.DateTimeField('datetime', default=timezone.now)

    parent_region = models.CharField('parent_region', max_length=150)
    region = models.CharField('region', max_length=150)
    address = models.CharField('region', max_length=150, blank=True, null=True)
    
    lat = models.FloatField('latitude')
    long = models.FloatField('longitude')
   
    category = models.TextField(blank=True, null=True)
    light = models.CharField('light', max_length=150, blank=True, null=True)

    organization = models.TextField(null=True, blank=True)
    criminal_type = models.CharField(max_length=100, null=True, blank=True)
    employee = models.TextField(null=True, blank=True)
    is_operative = models.BooleanField(default=False)
    crime_qualification = models.IntegerField(null=True, blank=True)
    yk_qualification = models.CharField(max_length=15, null=True, blank=True)
    severity = models.TextField(null=True, blank=True)
    is_attempt = models.CharField(max_length=40, null=True, blank=True)
    damage = models.CharField(max_length=40, null=True, blank=True)
    crime_direction = models.CharField(max_length=40, null=True, blank=True)
    money = models.FloatField(null=True, blank=True)
    drug_name = models.TextField(null=True, blank=True)
    drug_weight = models.FloatField(null=True, blank=True)
    crime = models.TextField(null=True, blank=True)
    victim_number = models.IntegerField(default=0)
    dead_num = models.IntegerField(default=0)

    def __repr__(self):
        return f'{self.datetime}/{self.region}'

    def __str__(self):
        return f'{self.datetime}/{self.region}'