# Generated by Django 4.1 on 2022-10-12 16:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_alter_chat_date_alter_chat_receiverid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 10, 12, 16, 51, 47, 863499, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
