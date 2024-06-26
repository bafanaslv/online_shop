# Generated by Django 5.0.6 on 2024-06-30 06:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='view_counter',
            field=models.PositiveIntegerField(default=0, help_text='Укажите количество просмотров', verbose_name='Счетчик промотров'),
        ),
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.ForeignKey(help_text='Выберите категорию из списка', on_delete=django.db.models.deletion.PROTECT, related_name='catgories', to='catalog.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='products',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Создан'),
        ),
        migrations.AlterField(
            model_name='products',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Изменен'),
        ),
    ]
