# Generated by Django 4.1 on 2022-09-15 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='type',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
