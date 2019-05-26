from django.db import models
from users.models import UserProfile

# Create your models here.


class WorkTime(models.Model):
    time = models.TimeField(verbose_name='Время приёма')

    class Meta:
        verbose_name = 'Время приёма'
        verbose_name_plural = 'Время приёма'
        ordering = ['time']

    def __str__(self):
        return '%s' % self.time


class WorkDate(models.Model):
    doctor = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='Врач', related_name='workdates')
    date = models.DateField(verbose_name='Дата приёма')
    worktimes = models.ManyToManyField(WorkTime, verbose_name='Рабочие часы', related_name='workdates')
    workcity = models.ForeignKey('WorkCity', on_delete=models.CASCADE, verbose_name='Город приёма', related_name='workdates')
    is_work = models.BooleanField(default=False, verbose_name='Рабочий день')

    class Meta:
        verbose_name = 'Дата приёма'
        verbose_name_plural = 'Даты приёма'
        ordering = ['date']

    def __str__(self):
        return '%s - %s' % (self.doctor, self.date)


class WorkCity(models.Model):
    city = models.CharField(max_length=50, verbose_name='Город')
    address = models.CharField(max_length=250, verbose_name='Адрес')
    phone = models.CharField(max_length=250, verbose_name='Телефон')

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return '%s' % self.city