# Generated by Django 4.1 on 2022-09-11 09:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0023_alter_timeline_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeline',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 11, 9, 34, 35, 659682, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
