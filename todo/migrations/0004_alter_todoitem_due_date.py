# Generated by Django 4.1 on 2022-09-03 14:39

from django.db import migrations, models
import todo.models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_remove_todoitem_name_of_admin_todolist_name_of_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='due_date',
            field=models.DateTimeField(blank=True, default=todo.models.one_week_hence),
        ),
    ]
