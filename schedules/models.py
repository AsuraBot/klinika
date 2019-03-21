from django.db import models

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
    date = models.DateField(verbose_name='Дата приёма')
    is_work = models.BooleanField(default=False, verbose_name='Рабочий день')
    worktimes = models.ManyToManyField(WorkTime, verbose_name='Рабочие часы', related_name='workdates')

    class Meta:
        verbose_name = 'Дата приёма'
        verbose_name_plural = 'Даты приёма'
        ordering = ['date']

    def __str__(self):
        return '%s' % self.date