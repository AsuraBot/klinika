# Generated by Django 2.1.7 on 2019-03-05 12:11

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('peoples', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название услуги')),
                ('price', models.PositiveIntegerField(verbose_name='Цена услуги')),
                ('ref_doc', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Процент специалиста')),
                ('ref_napr', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Процент направившего')),
                ('ref_agent', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Процент агента')),
                ('is_active', models.BooleanField(default=True, help_text='Предоставляется ли услуга', verbose_name='Активна')),
                ('doctors', models.ManyToManyField(blank=True, related_name='services', to='peoples.Doctor', verbose_name='Врачи')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ServiceMain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название услуги')),
                ('ref_doc', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Процент специалиста')),
                ('ref_napr', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Процент направившего')),
                ('ref_agent', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Процент агента')),
                ('is_active', models.BooleanField(default=True, help_text='Предоставляется ли услуга', verbose_name='Активна')),
            ],
            options={
                'verbose_name': 'Тип услуги',
                'verbose_name_plural': 'Тип услуг',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='service',
            name='service_main',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='services.ServiceMain', verbose_name='Тип услуги'),
        ),
    ]
