# Generated by Django 2.1.7 on 2019-03-05 12:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('peoples', '0004_auto_20190305_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='people', to=settings.AUTH_USER_MODEL, verbose_name='Профиль'),
        ),
    ]
