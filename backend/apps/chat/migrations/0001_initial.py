# Generated by Django 3.1.3 on 2021-04-28 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SessionModel',
            fields=[
                ('token', models.TextField(primary_key=True, serialize=False)),
                ('session', models.TextField()),
            ],
        ),
    ]
