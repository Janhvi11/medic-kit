# Generated by Django 4.1 on 2022-10-09 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0009_doc_image'),
        ('appointment', '0009_alter_appointment_doctorid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='doctorId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='register.doc'),
        ),
    ]
