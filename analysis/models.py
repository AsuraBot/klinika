from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AnalysisType(models.Model):
    name = models.CharField(max_length=250, verbose_name='Тип анализа')
    is_active = models.BooleanField(verbose_name='Активен', default=True, help_text='Проводится ли анализ')

    class Meta:
        verbose_name = 'Тип анализа'
        verbose_name_plural = 'Типы анализов'
        ordering = ['name']

    def __str__(self):
        return '%s' % self.name


class AnalysisColor(models.Model):
    color = models.CharField(max_length=250, verbose_name='Цвет пробирки')

    class Meta:
        verbose_name = 'Цвет пробирки'
        verbose_name_plural = 'Цвета пробирок'

    def __str__(self):
        return '%s' % self.color


class Analysis(models.Model):
    type_of_analysis = models.ForeignKey(AnalysisType, on_delete=models.CASCADE, related_name='analyzes',verbose_name='Тип анализа')
    name = models.CharField(max_length=250, verbose_name='Название анализа')
    is_active = models.BooleanField(verbose_name='Активен', default=True, help_text='Проводится ли анализ')
    tubecolor = models.ForeignKey(AnalysisColor, on_delete=models.SET_NULL, related_name='analyzes', verbose_name='Цвет пробирки', null=True, blank=True)
    price = models.PositiveIntegerField(verbose_name='Цена анализа')

    class Meta:
        verbose_name = 'Анализ'
        verbose_name_plural = 'Анализы'
        ordering = ['name']

    def __str__(self):
        return '%s' % self.name


class Hospital(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название больницы')
    price = models.PositiveIntegerField(verbose_name='Цена анализа') 
    analysis = models.ForeignKey(Analysis, on_delete=models.CASCADE,related_name='hospitals',verbose_name='Анализ')
    is_active = models.BooleanField(verbose_name='Активен', default=True, help_text='Предоставляют ли они нам услуги')

    class Meta:
        verbose_name = 'Больница'
        verbose_name_plural = 'Больницы'
        ordering = ['name']

    def __str__(self):
        return '%s %s' % (self.name, self.analysis.name)
