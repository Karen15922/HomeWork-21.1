# Generated by Django 5.1 on 2024-09-10 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='views_count',
            field=models.PositiveIntegerField(default=0, verbose_name='просмотры'),
        ),
    ]