from django.db import models
from django.core.validators import MaxValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from users.models import UserProfile
from discounts.models import Discount
from tinymce import HTMLField

# Create your models here.


class People(models.Model):
    name = models.CharField(max_length=250, verbose_name='ФИО', blank=True, null=True)
    phone = models.CharField(max_length=30, verbose_name='Контактный телефон', blank=True, null=True)
    adress = models.CharField(max_length=250, verbose_name='Адрес', blank=True, null=True)
    email = models.EmailField(max_length=250, verbose_name='Электронная почта', blank=True, null=True)
    dob = models.DateField(verbose_name='Дата рождения', blank=True, null=True)

    def __str__ (self):
        return '%s' % self.name

    class Meta:
        abstract = True


class Client(People):
    discount = models.ForeignKey(Discount, on_delete=models.SET_DEFAULT, verbose_name='Скидка', related_name='clients', default=1)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class DoctorMain(models.Model):
    name = models.CharField(max_length=250, verbose_name='Специальность')

    class Meta:
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'

    def __str__ (self):
        return '%s' % self.name


class Doctor(People):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, verbose_name='Профиль', null=True, blank=True, related_name='doctors')
    doctor_main = models.ManyToManyField(DoctorMain,verbose_name='Специальность',related_name='doctors')
    ref_doc = models.PositiveSmallIntegerField(verbose_name='Процент специалиста', default=0, validators=[MaxValueValidator(100)])
    oklad = models.PositiveIntegerField(verbose_name='Оклад', default=0)
    information = HTMLField(verbose_name='Информация')

    def get_picture_url(self, filename):
        ext = filename.split('.')[-1]
        filename = '%s.%s' % (self.user, ext)
        return 'images/doctors/%s' % filename

    image = models.ImageField(verbose_name='Фото', upload_to=get_picture_url, blank=True, null=True)

    class Meta:
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'

    def save(self, *args, **kwargs):
        if self.user:
            self.name = str(self.user)
            self.phone = self.user.phone
            self.adress = self.user.adress
            self.dob = self.user.dob
            self.email = self.user.email
        super(Doctor,self).save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse("doctors_detail", args=[self.id])

class Operator(People):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, verbose_name='Профиль', null=True, blank=True, related_name='operators')

    class Meta:
        verbose_name = 'Оператор'
        verbose_name_plural = 'Операторы'

    def save(self, *args, **kwargs):
        if self.user:
            self.name = str(self.user)
            self.phone = self.user.phone
            self.adress = self.user.adress
            self.dob = self.user.dob
            self.email = self.user.email
        super(Operator,self).save(*args,**kwargs)


class MainOperator(People):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, verbose_name='Профиль', null=True, blank=True, related_name='mainoperators')

    class Meta:
        verbose_name = 'Старший оператор'
        verbose_name_plural = 'Старшие операторы'

    def save(self, *args, **kwargs):
        if self.user:
            self.name = str(self.user)
            self.phone = self.user.phone
            self.adress = self.user.adress
            self.dob = self.user.dob
            self.email = self.user.email
        super(MainOperator,self).save(*args,**kwargs)


class Director(People):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, verbose_name='Профиль', null=True, blank=True, related_name='directors')

    class Meta:
        verbose_name = 'Руководство'
        verbose_name_plural = 'Руководство'

    def save(self, *args, **kwargs):
        if self.user:
            self.name = str(self.user)
            self.phone = self.user.phone
            self.adress = self.user.adress
            self.dob = self.user.dob
            self.email = self.user.email
        super(Director,self).save(*args,**kwargs)