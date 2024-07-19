from django.db import models

from users.models import User, NULLABLE


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        verbose_name="Опиcание", help_text="Введите описание категории"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Products(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование"
    )
    description = models.TextField(
        verbose_name="Опиcание"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="categories",
        verbose_name="Категория"
    )
    image = models.ImageField(
        upload_to="catalog/media",
        blank=True,
        null=True,
        verbose_name="Изображение"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена"
    )
    owner = models.ForeignKey(
        User,
        verbose_name='Владелец',
        on_delete=models.CASCADE,
        related_name="products", **NULLABLE
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Изменен")
    view_counter = models.PositiveIntegerField(
        default=0,
        verbose_name="Счетчик проcмотров"
    )

    def __str__(self):
        return f"{self.name} {self.description} {self.price}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class ProductVersions(models.Model):
    name = models.ForeignKey(
        Products,
        on_delete=models.CASCADE,
        related_name="product",
        verbose_name="Наименование"
    )
    version_number = models.PositiveIntegerField(
        verbose_name="номер версии"
    )
    version_name = models.CharField(
        max_length=100,
        verbose_name="наименование версии"
    )
    current_version = models.BooleanField(
        default=False,
        verbose_name="Признак текущей версии"
    )

    def __str__(self):
        return f"{self.name} {self.version_number} {self.version_name}"

    class Meta:
        verbose_name = "Версия продукта"
        verbose_name_plural = "Версии продуктов"
