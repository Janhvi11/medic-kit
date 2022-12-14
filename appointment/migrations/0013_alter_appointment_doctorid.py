# Generated by Django 4.1 on 2022-10-14 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0010_user_is_admin'),
        ('appointment', '0012_alter_appointment_doctorid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='doctorId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='register.doc', to_field='username'),
        ),
    ]
