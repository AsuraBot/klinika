from django.db import models
from django.urls import reverse
from tinymce import HTMLField

# Create your models here.


class Novost(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    text = HTMLField(verbose_name='Новость')
    date = models.DateField(verbose_name='Дата публикации', auto_now_add=True)
    is_active = models.BooleanField(verbose_name='Опубликовать', default=True)

    def get_picture_url(self, filename):
        ext = filename.split('.')[-1]
        filename = '%s.%s' % (self.title, ext)
        return 'images/news/%s' % filename

    image = models.ImageField(upload_to=get_picture_url, verbose_name='Фотография')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-date']

    def __str__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return reverse("news_detail", args=[self.id])