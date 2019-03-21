from django.db import models
from django.core.validators import MaxValueValidator
from peoples.models import Doctor

# Create your models here.


class ServiceMain(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название услуги')
    ref_doc = models.PositiveSmallIntegerField(verbose_name='Процент специалиста',default=0,validators=[MaxValueValidator(100)])
    ref_napr = models.PositiveSmallIntegerField(verbose_name='Процент направившего',default=0,validators=[MaxValueValidator(100)])
    ref_agent = models.PositiveSmallIntegerField(verbose_name='Процент агента',default=0,validators=[MaxValueValidator(100)])
    is_active = models.BooleanField(verbose_name='Активна', default=True, help_text='Предоставляется ли услуга')

    class Meta:
        verbose_name = 'Тип услуги'
        verbose_name_plural = 'Тип услуг'
        ordering = ['name']

    def __str__(self):
        return '%s' % self.name


class Service(models.Model):
    service_main = models.ForeignKey(ServiceMain,on_delete=models.CASCADE,verbose_name='Тип услуги',related_name='services') 
    name = models.CharField(max_length=250, verbose_name='Название услуги')
    price = models.PositiveIntegerField(verbose_name='Цена услуги')
    doctors = models.ManyToManyField(Doctor, verbose_name='Врачи', related_name='services', blank=True)
    ref_doc = models.PositiveSmallIntegerField(verbose_name='Процент специалиста',default=0,validators=[MaxValueValidator(100)])
    ref_napr = models.PositiveSmallIntegerField(verbose_name='Процент направившего',default=0,validators=[MaxValueValidator(100)])
    ref_agent = models.PositiveSmallIntegerField(verbose_name='Процент агента',default=0,validators=[MaxValueValidator(100)])
    is_active = models.BooleanField(verbose_name='Активна', default=True, help_text='Предоставляется ли услуга')

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['name']

    def __str__(self):
        return ''
    
    def save(self, *args, **kwargs):
        if self.ref_doc == 0 and self.ref_napr == 0 and self.ref_agent == 0:
            self.ref_doc = self.service_main.ref_doc
            self.ref_napr = self.service_main.ref_napr
            self.ref_agent = self.service_main.ref_agent
        super(Service,self).save(*args,**kwargs)