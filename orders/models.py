from django.db import models
from django.core.validators import MaxValueValidator
from services.models import Service
from analysis.models import Analysis
from users.models import UserProfile
from schedules.models import WorkTime, WorkDate

# Create your models here.


class ServiceInOrder(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='services_order', verbose_name='Заказ')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='services_order', verbose_name='Услуга')
    doctor = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='services_order', verbose_name='Врач')
    city = models.CharField(max_length=250, verbose_name='Город')
    date = models.DateField(verbose_name='Дата')
    time = models.TimeField(verbose_name='Время')
    price = models.PositiveIntegerField(verbose_name='Цена')

    class Meta:
        verbose_name = 'Услуга в заказе'
        verbose_name_plural = 'Услуги в заказе'

    def __str__(self):
        return '%s %s %s' % (self.service, self.doctor, self.date)


class AnalysisInOrder(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='analysis_order', verbose_name='Заказ')
    analysis = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='analysis_order', verbose_name='Анализ')
    doctor = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='analysis_order', verbose_name='Врач')
    city = models.CharField(max_length=250, verbose_name='Город')
    date = models.DateField(verbose_name='Дата')
    time = models.TimeField(verbose_name='Время')
    price = models.PositiveIntegerField(verbose_name='Цена')

    class Meta:
        verbose_name = 'Анализ в заказе'
        verbose_name_plural = 'Анализы в заказе'

    def __str__(self):
        return '%s %s %s' % (self.analysis, self.doctor, self.date)


class Order(models.Model):
    client_name = models.CharField(max_length=250, verbose_name='Заказчик')
    client_address = models.CharField(max_length=250, verbose_name='Адрес', null=True, blank=True)
    client_phone = models.CharField(max_length=30, verbose_name='Телефон', null=True, blank=True)
    client_dob = models.DateField(verbose_name='Дата рождения')
    client_mail = models.EmailField(max_length=250, verbose_name='E-mail', null=True, blank=True)
    discount = models.PositiveSmallIntegerField(verbose_name='Скидка', default=0, validators=[MaxValueValidator(100)])
    total_price = models.PositiveIntegerField(verbose_name='Итоговая цена', default=0)
    status = models.BooleanField(verbose_name='Оплачен', default=False)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return '%s %s' % (self.client_name, self.client_dob)

    def save(self, *args, **kwargs):
        if self.status:
            for item in self.services_order.all():
                doctor = item.doctor
                times = WorkTime.objects.filter(time=item.time)
                date = WorkDate.objects.get(doctor=doctor, date=item.date)
                for i in times:
                    date.worktimes.remove(i)
                date.save()
        super(Order, self).save(*args, **kwargs)