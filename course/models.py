from django.db import models

# Create your models here.
from django.urls import reverse


class Course(models.Model):
    title = models.CharField('Название курса обучения', max_length=150)
    description = models.TextField('Краткое описание')
    price = models.DecimalField('Цена', max_digits=5, decimal_places=0)
    image = models.ImageField('Картинка', upload_to='course/'+str(title))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс обучения'
        verbose_name_plural = 'Курсы обучения'
        ordering = ['id']

    def get_absolute_url(self):
        return reverse('singleCourse', kwargs={'pk': self.pk})
