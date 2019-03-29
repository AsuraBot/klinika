from django.db import models
from tinymce import HTMLField

# Create your models here.


class Slider(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок слайда')
    text = HTMLField(max_length=250, verbose_name='Текст слайда')

    def get_picture_url(self, filename):
        ext = filename.split('.')[-1]
        filename = '%s.%s' % (self.title, ext)
        return 'images/slides/%s' % filename
    
    image = models.ImageField(upload_to=get_picture_url,verbose_name='Фото слайда')

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'

    is_active = models.BooleanField(default=True, verbose_name='Показывать слайд')

    def __str__(self):
        return '%s' % self.title