# Generated by Django 2.1.7 on 2019-04-15 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0006_auto_20190407_1455'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worktime',
            name='is_free',
        ),
    ]
