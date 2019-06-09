from django.db import models
from users.models import UserProfile
from cities.models import UserCity

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
    worktimes = models.ManyToManyField(WorkTime, verbose_name='Рабочие часы', related_name='workdates', blank=True)
    workcity = models.ForeignKey(UserCity, on_delete=models.CASCADE, verbose_name='Город приёма', related_name='workdates')
    is_work = models.BooleanField(default=False, verbose_name='Рабочий день')

    class Meta:
        verbose_name = 'Дата приёма'
        verbose_name_plural = 'Даты приёма'
        ordering = ['date']

    def __str__(self):
        return '%s - %s' % (self.doctor, self.date)