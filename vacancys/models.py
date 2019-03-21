from django.db import models
from tinymce import HTMLField

# Create your models here.

class Vacancy(models.Model):
    name = models.CharField(max_length=250, verbose_name='Вакансия')
    jobinfo = HTMLField(verbose_name='О вакансии')

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return '%s' % self.name