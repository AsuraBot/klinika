from django.db import models
from peoples.models import Doctor

# Create your models here.


class WorkTime(models.Model):
    time = models.TimeField(verbose_name='Время приёма')
    is_free = models.BooleanField(default=True, verbose_name='Свободно')

    class Meta:
        verbose_name = 'Время приёма'
        verbose_name_plural = 'Время приёма'
        ordering = ['time']

    def __str__(self):
        return '%s' % self.time


class WorkDate(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='workdates', verbose_name='Врач')
    date = models.DateField(verbose_name='Дата приёма')
    worktimes = models.ManyToManyField(WorkTime, verbose_name='Рабочие часы', related_name='workdates')
    is_work = models.BooleanField(default=False, verbose_name='Рабочий день')

    class Meta:
        verbose_name = 'Дата приёма'
        verbose_name_plural = 'Даты приёма'
        ordering = ['date']

    def __str__(self):
        return '%s - %s' % (self.doctor, self.date)