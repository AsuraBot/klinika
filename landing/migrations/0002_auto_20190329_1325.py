# Generated by Django 2.1.7 on 2019-03-29 10:25

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='text',
            field=tinymce.models.HTMLField(max_length=250, verbose_name='Текст слайда'),
        ),
    ]
