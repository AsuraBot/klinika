# Generated by Django 2.1.7 on 2019-03-31 09:21

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnalysisInOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('analysis', models.CharField(max_length=250, verbose_name='Анализ')),
                ('doctor', models.CharField(max_length=250, verbose_name='Врач')),
                ('date', models.DateField(verbose_name='Дата')),
                ('time', models.TimeField(verbose_name='Время')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Анализ в заказе',
                'verbose_name_plural': 'Анализы в заказе',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=250, verbose_name='Заказчик')),
                ('clinet_address', models.CharField(blank=True, max_length=250, null=True, verbose_name='Адрес')),
                ('client_phone', models.CharField(blank=True, max_length=30, null=True, verbose_name='телефон')),
                ('client_dob', models.DateField(verbose_name='Дата рождения')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Итоговая цена')),
                ('discount', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Скидка')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='ServiceInOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=250, verbose_name='Услуга')),
                ('doctor', models.CharField(max_length=250, verbose_name='Врач')),
                ('date', models.DateField(verbose_name='Дата')),
                ('time', models.TimeField(verbose_name='Время')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services_order', to='orders.Order', verbose_name='Заказ')),
            ],
            options={
                'verbose_name': 'Услуга в заказе',
                'verbose_name_plural': 'Услуги в заказе',
            },
        ),
        migrations.AddField(
            model_name='analysisinorder',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analysis_order', to='orders.Order', verbose_name='Заказ'),
        ),
    ]