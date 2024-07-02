from django.db import models


class Blog(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name='заголовок'
    )
    slug = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='ссылка'
    )
    body = models.TextField(
        verbose_name='содержимое'
    )
    image = models.ImageField(
        upload_to='blog/media',
        blank=True, null=True, verbose_name='изображение',
        help_text='загрузите изображение'
    )
    publish = models.BooleanField(
        default=False,
        verbose_name='публиковать'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='создан'
    )
    view_counter = models.PositiveIntegerField(
        default=0,
        verbose_name='счетчик проcмотров',
        help_text='укажите количество просмотров'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
