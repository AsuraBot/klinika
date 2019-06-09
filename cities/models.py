from django.db import models

# Create your models here.


class UserCity(models.Model):
    city = models.CharField(max_length=50, verbose_name='Город')
    address = models.CharField(max_length=250, verbose_name='Адрес')
    phone = models.CharField(max_length=250, verbose_name='Телефон')

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return '%s' % self.city