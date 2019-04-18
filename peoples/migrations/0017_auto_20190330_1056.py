# Generated by Django 2.1.7 on 2019-03-30 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peoples', '0016_doctor_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='doctor_main',
        ),
        migrations.AddField(
            model_name='doctor',
            name='doctor_main',
            field=models.ManyToManyField(related_name='doctors', to='peoples.DoctorMain', verbose_name='Специальность'),
        ),
    ]