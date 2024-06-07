from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование', help_text='Введите наименование категории')
    description = models.TextField(verbose_name='Опиcание', help_text='Введите описание категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Products(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование', help_text='Введите наименование продукта')
    description = models.TextField(verbose_name='Опиcание', help_text='Введите описание продукта')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='catgories')
    image = models.ImageField(upload_to='catalog/media', blank=True, null=True, verbose_name='Изображение', help_text='Загрузите изображение продукта')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена', help_text='Введите цену продукта')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} {self.description} {self.price}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
