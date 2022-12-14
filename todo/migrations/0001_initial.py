# Generated by Django 4.1 on 2022-09-26 06:20

import datetime
from django.db import migrations, models
import django.db.models.deletion
import todo.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('username', models.CharField(default='admin', max_length=50)),
                ('type', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ToDoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime(2022, 9, 26, 6, 20, 27, 897383, tzinfo=datetime.timezone.utc), null=True)),
                ('due_date', models.DateTimeField(blank=True, default=todo.models.one_week_hence, null=True)),
                ('todo_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.todolist')),
            ],
        ),
    ]
