# Generated by Django 2.1.7 on 2019-04-28 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_servicemain_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicemain',
            name='service_counter',
            field=models.PositiveIntegerField(default=0, verbose_name='Популярность'),
        ),
    ]