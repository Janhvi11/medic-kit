# Generated by Django 4.1 on 2022-09-09 03:08

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0006_alter_doc_username_alter_pharma_username_and_more'),
        ('timeline', '0007_alter_timeline_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeline',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 9, 3, 8, 23, 985008, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.CreateModel(
            name='timline_pharma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(default=datetime.datetime(2022, 9, 9, 3, 8, 23, 985008, tzinfo=datetime.timezone.utc), null=True)),
                ('update', models.TextField(max_length=500)),
                ('pharmaId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.pharma')),
            ],
        ),
        migrations.CreateModel(
            name='timline_doc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(default=datetime.datetime(2022, 9, 9, 3, 8, 23, 985008, tzinfo=datetime.timezone.utc), null=True)),
                ('update', models.TextField(max_length=500)),
                ('docId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.doc')),
            ],
        ),
    ]
