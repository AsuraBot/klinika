# Generated by Django 2.1.7 on 2019-06-12 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название анализа')),
                ('is_active', models.BooleanField(default=True, help_text='Проводится ли анализ', verbose_name='Активен')),
                ('price', models.PositiveIntegerField(verbose_name='Цена анализа')),
            ],
            options={
                'verbose_name': 'Анализ',
                'verbose_name_plural': 'Анализы',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='AnalysisColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=250, verbose_name='Цвет пробирки')),
            ],
            options={
                'verbose_name': 'Цвет пробирки',
                'verbose_name_plural': 'Цвета пробирок',
            },
        ),
        migrations.CreateModel(
            name='AnalysisType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Тип анализа')),
                ('is_active', models.BooleanField(default=True, help_text='Проводится ли анализ', verbose_name='Активен')),
            ],
            options={
                'verbose_name': 'Тип анализа',
                'verbose_name_plural': 'Типы анализов',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название больницы')),
                ('price', models.PositiveIntegerField(verbose_name='Цена анализа')),
                ('is_active', models.BooleanField(default=True, help_text='Предоставляют ли они нам услуги', verbose_name='Активен')),
                ('analysis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hospitals', to='analysis.Analysis', verbose_name='Анализ')),
            ],
            options={
                'verbose_name': 'Больница',
                'verbose_name_plural': 'Больницы',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='analysis',
            name='tubecolor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='analyzes', to='analysis.AnalysisColor', verbose_name='Цвет пробирки'),
        ),
        migrations.AddField(
            model_name='analysis',
            name='type_of_analysis',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analyzes', to='analysis.AnalysisType', verbose_name='Тип анализа'),
        ),
    ]
