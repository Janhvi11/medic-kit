# Generated by Django 4.1 on 2022-09-07 16:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0006_alter_timeline_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeline',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 7, 16, 44, 21, 181710, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
