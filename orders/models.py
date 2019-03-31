from django.db import models
from django.core.validators import MaxValueValidator
from services.models import Service
from analysis.models import Analysis
from peoples.models import Doctor

# Create your models here.


class ServiceInOrder(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='services_order', verbose_name='Заказ')
    service = models.CharField(max_length=250, verbose_name='Услуга')
    doctor = models.CharField(max_length=250, verbose_name='Врач')
    date = models.DateField(verbose_name='Дата')
    time = models.TimeField(verbose_name='Время')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')

    class Meta:
        verbose_name = 'Услуга в заказе'
        verbose_name_plural = 'Услуги в заказе'

    def __str__(self):
        return '%s %s %s' % (self.service, self.doctor, self.date)


class AnalysisInOrder(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='analysis_order', verbose_name='Заказ')
    analysis = models.CharField(max_length=250, verbose_name='Анализ')
    doctor = models.CharField(max_length=250, verbose_name='Врач')
    date = models.DateField(verbose_name='Дата')
    time = models.TimeField(verbose_name='Время')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')

    class Meta:
        verbose_name = 'Анализ в заказе'
        verbose_name_plural = 'Анализы в заказе'

    def __str__(self):
        return '%s %s %s' % (self.analysis, self.doctor, self.date)


class Order(models.Model):
    client_name = models.CharField(max_length=250, verbose_name='Заказчик')
    clinet_address = models.CharField(max_length=250, verbose_name='Адрес', null=True, blank=True)
    client_phone = models.CharField(max_length=30, verbose_name='телефон', null=True, blank=True)
    client_dob = models.DateField(verbose_name='Дата рождения')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Итоговая цена')
    discount = models.PositiveSmallIntegerField(verbose_name='Скидка', default=0, validators=[MaxValueValidator(100)])
    status = models.BooleanField(verbose_name='Оплачен', default=False)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return '%s %s' % (self.client_name, self.client_dob)