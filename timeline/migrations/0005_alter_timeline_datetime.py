# Generated by Django 4.1 on 2022-09-06 03:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0004_alter_timeline_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeline',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 6, 3, 8, 22, 197660, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
