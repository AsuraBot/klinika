# Generated by Django 2.1.7 on 2019-03-05 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workdate',
            name='worktimes',
            field=models.ManyToManyField(related_name='workdates', to='schedules.WorkTime', verbose_name='Рабочие часы'),
        ),
    ]
