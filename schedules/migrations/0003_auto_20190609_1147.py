# Generated by Django 2.1.7 on 2019-06-09 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0002_auto_20190602_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workdate',
            name='workcity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workdates', to='cities.UserCity', verbose_name='Город приёма'),
        ),
        migrations.DeleteModel(
            name='WorkCity',
        ),
    ]
