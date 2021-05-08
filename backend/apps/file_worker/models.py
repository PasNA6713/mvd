
from django.db import models


class ImgModel(models.Model):
    file = models.FileField(upload_to='uploads/images/')
    uploaded = models.DateTimeField(auto_now=True)


class FormatedImgModel(models.Model):
    file = models.FileField(upload_to='uploads/formated-img/')
    parent = models.OneToOneField(
        ImgModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )


from django.contrib import admin
admin.site.register(ImgModel)
admin.site.register(FormatedImgModel)