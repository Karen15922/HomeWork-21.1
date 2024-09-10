# Generated by Django 5.1 on 2024-09-10 13:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='заголовок')),
                ('slug', models.CharField(blank=True, max_length=150, null=True, verbose_name='slug')),
                ('content', models.TextField(blank=True, null=True, verbose_name='содержимое')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blogs/', verbose_name='превью')),
                ('created_at', models.DateField(default=datetime.datetime.now)),
                ('is_published', models.BooleanField(default=True, verbose_name='опубликовано')),
                ('views_count', models.PositiveIntegerField(default=0, verbose_name='просмотр')),
            ],
            options={
                'verbose_name': 'пост',
                'verbose_name_plural': 'посты',
            },
        ),
    ]