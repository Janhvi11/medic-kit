# Generated by Django 4.1 on 2022-10-01 06:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0007_alter_todoitem_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 1, 6, 15, 58, 134266, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
