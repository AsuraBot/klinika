# Generated by Django 2.1.7 on 2019-03-24 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('peoples', '0013_auto_20190324_1748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctormain',
            name='adress',
        ),
        migrations.RemoveField(
            model_name='doctormain',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='doctormain',
            name='email',
        ),
        migrations.RemoveField(
            model_name='doctormain',
            name='phone',
        ),
    ]
