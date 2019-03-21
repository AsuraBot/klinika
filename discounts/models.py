from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.

class Discount(models.Model):
    discount = models.PositiveSmallIntegerField(verbose_name='Процент скидки', default=0, validators=[MaxValueValidator(100)])

    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'
        ordering = ['discount']


    def __str__(self):
        return '%s' % self.discount