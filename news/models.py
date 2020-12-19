from django.db import models
from django.urls import reverse

# Create your models here.


class News(models.Model):
    title = models.CharField('Заголовок', max_length=150)
    text = models.TextField('Текст')
    created_at = models.DateField('Дата публикации', auto_now_add=True)
    published = models.BooleanField('Опубликовано', default=True)
    image = models.ImageField('Картинка', upload_to='news/%Y/%m/%d', blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория', default='6', related_name='news')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def get_absolute_url(self):
        return reverse('singlePost', kwargs={'pk': self.pk})

class Category(models.Model):
    title = models.CharField('Название', max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('newsByCategory', kwargs={'title': self.title})

    def getdd(self):
        return len(Category)
