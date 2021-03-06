from django.db import models
from tinymce import HTMLField

# Create your models here.

class About(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    text = HTMLField(verbose_name='Текст')

    class Meta:
        verbose_name = 'О компании'
        verbose_name_plural = 'О компании'

    def __str__(self):
        return '%s' % self.title