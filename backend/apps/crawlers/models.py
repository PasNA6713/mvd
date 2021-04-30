from django.db import models
from django.contrib.postgres.fields import ArrayField


class NewsModel(models.Model):
    title = models.CharField(max_length=200,null=True)
    link = models.CharField(max_length=200,null=True)
    posted = models.DateTimeField(null=True,blank=True)
    text = models.TextField(null=True)
    org = ArrayField(models.CharField(max_length=100,blank=True),blank=True,null=True)
    loc = ArrayField(models.CharField(max_length=100,blank=True),blank=True,null=True)
    per = ArrayField(models.CharField(max_length=100,blank=True),blank=True,null=True)

    def __str__(self):
        return self.title