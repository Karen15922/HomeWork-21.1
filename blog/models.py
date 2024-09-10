from django.db import models
from datetime import datetime

NULLABLE = {'null':True, 'blank':True}

class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    content = models.TextField(verbose_name='содержимое', **NULLABLE)
    image = models.ImageField(upload_to='blogs/', verbose_name='превью', **NULLABLE)
    created_at = models.DateField(default=datetime.now)
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    views_count = models.PositiveIntegerField(default=0, verbose_name='просмотры')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'