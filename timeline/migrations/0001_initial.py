# Generated by Django 4.1 on 2022-10-09 16:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('register', '0009_doc_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='timeline_pharma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(default=datetime.datetime(2022, 10, 9, 16, 13, 39, 728805, tzinfo=datetime.timezone.utc), null=True)),
                ('update', models.TextField(max_length=500)),
                ('type', models.CharField(blank=True, default='pharma', max_length=20, null=True)),
                ('pharmaId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.pharma')),
            ],
        ),
        migrations.CreateModel(
            name='timeline_doc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(default=datetime.datetime(2022, 10, 9, 16, 13, 39, 727805, tzinfo=datetime.timezone.utc), null=True)),
                ('update', models.TextField(max_length=500)),
                ('type', models.CharField(blank=True, default='doc', max_length=20, null=True)),
                ('docId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.doc')),
            ],
        ),
        migrations.CreateModel(
            name='timeline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(default=datetime.datetime(2022, 10, 9, 16, 13, 39, 727805, tzinfo=datetime.timezone.utc), null=True)),
                ('update', models.TextField(max_length=500)),
                ('type', models.CharField(blank=True, default='user', max_length=20, null=True)),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.user')),
            ],
        ),
    ]
