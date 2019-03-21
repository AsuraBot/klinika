from django.db import models
from django.core.validators import MaxValueValidator
from services.models import Service
from users.models import UserProfile

# Create your models here.


# class ServiceInOrder(models.Model):
#     service = models.ForeignKey(Service,on_delete=models.CASCADE,verbose_name='Услуга',related_name='service_items')
#     doctor = models.ForeignKey()
#     ref_doc = models.PositiveSmallIntegerField(verbose_name='Процент специалиста',default=0,validators=[MaxValueValidator(100)])
#     ref_napr = models.PositiveSmallIntegerField(verbose_name='Процент направившего',default=0,validators=[MaxValueValidator(100)])
#     ref_agent = models.PositiveSmallIntegerField(verbose_name='Процент агента',default=0,validators=[MaxValueValidator(100)])
#     is_active = models.BooleanField(verbose_name='Активна', default=True, help_text='Предоставляется ли услуга')

#     class Meta:
#         verbose_name = 'Тип услуги'
#         verbose_name_plural = 'Тип услуг'
#         ordering = ['name']

#     def __str__(self):
#         return '%s' % self.name


# class AnalysisInOrder(models.Model):
#     service = models.ForeignKey(Service,on_delete=models.CASCADE,verbose_name='Услуга',related_name='items')
#     name = models.CharField(max_length=250, verbose_name='Услуга')
#     ref_doc = models.PositiveSmallIntegerField(verbose_name='Процент специалиста',default=0,validators=[MaxValueValidator(100)])
#     ref_napr = models.PositiveSmallIntegerField(verbose_name='Процент направившего',default=0,validators=[MaxValueValidator(100)])
#     ref_agent = models.PositiveSmallIntegerField(verbose_name='Процент агента',default=0,validators=[MaxValueValidator(100)])
#     is_active = models.BooleanField(verbose_name='Активна', default=True, help_text='Предоставляется ли услуга')

#     class Meta:
#         verbose_name = 'Тип услуги'
#         verbose_name_plural = 'Тип услуг'
#         ordering = ['name']

#     def __str__(self):
#         return '%s' % self.name


# class Order(models.Model):
#     service = models.ForeignKey(Service,on_delete=models.CASCADE,verbose_name='Услуга',related_name='services')
#     name = models.CharField(max_length=250, verbose_name='Услуга')
#     ref_doc = models.PositiveSmallIntegerField(verbose_name='Процент специалиста',default=0,validators=[MaxValueValidator(100)])
#     ref_napr = models.PositiveSmallIntegerField(verbose_name='Процент направившего',default=0,validators=[MaxValueValidator(100)])
#     ref_agent = models.PositiveSmallIntegerField(verbose_name='Процент агента',default=0,validators=[MaxValueValidator(100)])
#     is_active = models.BooleanField(verbose_name='Активна', default=True, help_text='Предоставляется ли услуга')

#     class Meta:
#         verbose_name = 'Тип услуги'
#         verbose_name_plural = 'Тип услуг'
#         ordering = ['name']

#     def __str__(self):
#         return '%s' % self.name