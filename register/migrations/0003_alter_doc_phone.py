# Generated by Django 4.1 on 2022-09-01 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_alter_doc_age_alter_doc_experience_alter_doc_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doc',
            name='phone',
            field=models.BigIntegerField(),
        ),
    ]