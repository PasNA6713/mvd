# Generated by Django 3.1.3 on 2021-04-28 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawlers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsmodel',
            name='link',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='loc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='org',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='per',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='posted',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
