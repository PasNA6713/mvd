# Generated by Django 3.1.3 on 2021-04-28 15:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_auto_20210428_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapitem',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 28, 15, 26, 44, 794163, tzinfo=utc), verbose_name='datetime'),
        ),
    ]
