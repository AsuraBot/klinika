# Generated by Django 2.1.7 on 2019-03-05 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='discount',
            options={'ordering': ['discount'], 'verbose_name': 'Скидка', 'verbose_name_plural': 'Скидки'},
        ),
    ]
