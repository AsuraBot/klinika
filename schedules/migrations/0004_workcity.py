# Generated by Django 2.1.7 on 2019-04-01 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0003_workdate_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkCity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50, verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
        ),
    ]
