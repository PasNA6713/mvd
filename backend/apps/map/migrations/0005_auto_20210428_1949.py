# Generated by Django 3.1.3 on 2021-04-28 16:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0004_auto_20210428_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapitem',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 28, 16, 48, 59, 510322, tzinfo=utc), verbose_name='datetime'),
        ),
    ]