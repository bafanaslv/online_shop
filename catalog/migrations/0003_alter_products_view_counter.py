# Generated by Django 5.0.6 on 2024-07-01 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_products_view_counter_alter_products_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='view_counter',
            field=models.PositiveIntegerField(default=0, help_text='Укажите количество просмотров', verbose_name='Счетчик проcмотров'),
        ),
    ]
