# Generated by Django 4.1 on 2022-09-11 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('medhistory', '0002_medhistory_doctorid_medhistory_patientid'),
        ('register', '0006_alter_doc_username_alter_pharma_username_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isavailable', models.BooleanField(default=False)),
                ('d_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.doc')),
                ('medh_pres', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='medhistory.medhistory')),
                ('u_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.user')),
            ],
        ),
    ]
