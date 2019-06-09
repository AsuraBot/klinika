from django.db import models
from users.models import UserProfile


class Review(models.Model):
    name = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='Имя', related_name='reviews')
    text = models.TextField(verbose_name='Отзыв')
    answer = models.TextField(verbose_name='Ответ', blank=True, null=True)
    date = models.DateField(verbose_name='Дата публикации', auto_now_add=True)
    is_active = models.BooleanField(verbose_name='Опубликовать', default=False)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return '%s, %s' % (self.name, self.date)