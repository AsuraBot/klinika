# Generated by Django 2.1.7 on 2019-03-28 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='novost',
            options={'ordering': ['-date'], 'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
    ]