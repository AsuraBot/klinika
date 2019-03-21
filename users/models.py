from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class UserProfile(AbstractUser):
    sur_name = models.CharField(max_length=50, verbose_name='Отчество', blank=True, null=True)
    adress = models.CharField(max_length=250, verbose_name='Адрес', blank=True, null=True)
    dob = models.DateField(verbose_name='Дата рождения', blank=True, null=True)
    phone = models.CharField(max_length=30, verbose_name='Телефон', blank=True, null=True)

    def __str__(self):
        return '%s %s %s' % (self.last_name, self.first_name, self.sur_name)

