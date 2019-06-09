from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.core.validators import MaxValueValidator
# from django.db.models.signals import post_save
# from django.dispatch import receiver
from tinymce import HTMLField
from cities.models import UserCity


class Discount(models.Model):
    discount = models.PositiveSmallIntegerField(verbose_name='Процент скидки', default=0, validators=[MaxValueValidator(100)])

    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'
        ordering = ['discount']


    def __str__(self):
        return '%s' % self.discount


class DoctorMain(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название')

    class Meta:
        verbose_name = 'Специальность врача'
        verbose_name_plural = 'Специальности врачей'

    def __str__ (self):
        return '%s' % self.name


class MyGroup(Group):

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class UserProfile(AbstractUser):
    sur_name = models.CharField(max_length=50, verbose_name='Отчество', blank=True, null=True)
    adress = models.CharField(max_length=250, verbose_name='Адрес', blank=True, null=True)
    dob = models.DateField(verbose_name='Дата рождения', blank=True, null=True)
    phone = models.CharField(max_length=30, verbose_name='Телефон', blank=True, null=True)
    city = models.ForeignKey(UserCity, on_delete=models.SET_NULL, related_name='users', verbose_name='Город', blank=True, null=True)

    discount = models.ForeignKey(Discount, on_delete=models.SET_DEFAULT, verbose_name='Скидка', related_name='users', default=0)

    doctor_main = models.ManyToManyField(DoctorMain,verbose_name='Специальность',related_name='users', blank=True)
    ref_doc = models.PositiveSmallIntegerField(verbose_name='Процент специалиста', default=0, validators=[MaxValueValidator(100)])
    oklad = models.PositiveIntegerField(verbose_name='Оклад', default=0)
    information = HTMLField(verbose_name='Информация', null=True, blank=True)

    def get_picture_url(self, filename):
        ext = filename.split('.')[-1]
        filename = '%s.%s' % (self.id, ext)
        return 'images/users/%s' % filename

    image = models.ImageField(verbose_name='Фото', upload_to=get_picture_url, blank=True, null=True)

    agency = models.CharField(max_length=250, verbose_name='Мед. учреждение', blank=True, null=True)

    def __str__(self):
        return '%s %s %s' % (self.last_name, self.first_name, self.sur_name)

    # def save(self, *args, **kwargs):
    #     if len(self.doctor_main.all()):
    #         print (len(self.doctor_main.all()))
    #         group = MyGroup.objects.get(name='Врач')
    #         if not group in self.groups.filter(name='Врач'):
    #             group.user_set.add(self)

    #     super(UserProfile, self).save(*args, **kwargs)
    

# @receiver(post_save, sender=UserProfile)
# def update_groups(sender, instance, **kwargs):
#     if len(instance.doctor_main.all()):
#         group = MyGroup.objects.get(name='Врач')
#         if group not in instance.groups.filter(name='Врач'):
#         group.user_set.add(instance)