# Generated by Django 2.1.7 on 2019-03-05 12:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('peoples', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name': 'Клиент', 'verbose_name_plural': 'Клиенты'},
        ),
        migrations.AlterModelOptions(
            name='doctor',
            options={'verbose_name': 'Врач', 'verbose_name_plural': 'Врачи'},
        ),
        migrations.AddField(
            model_name='doctor',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to=settings.AUTH_USER_MODEL, verbose_name='Профиль'),
        ),
    ]
