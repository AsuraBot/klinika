# Generated by Django 2.1.7 on 2019-05-26 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190526_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='doctor_main',
            field=models.ManyToManyField(blank=True, related_name='users', to='users.DoctorMain', verbose_name='Специальность'),
        ),
    ]
