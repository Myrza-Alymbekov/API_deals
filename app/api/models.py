from django.db import models
from django.contrib.auth.models import User


class BookmarkType(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')

    class Meta:
        verbose_name = 'Тип ссылки'
        verbose_name_plural = 'Типы ссылок'

    def __str__(self):
        return self.name


class Bookmark(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок страницы', null=True, blank=True)
    description = models.TextField(verbose_name='Краткое описание', null=True, blank=True)
    link = models.URLField(verbose_name='Ссылка на страницу')
    type = models.ForeignKey(BookmarkType, on_delete=models.PROTECT, verbose_name='Тип ссылки')
    preview_image = models.URLField(blank=True, null=True, verbose_name='Картинка превью')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата и время изменения')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    class Meta:
        verbose_name = 'Закладка страницы'
        verbose_name_plural = 'Закладки страниц'

    def __str__(self):
        return f'{self.title} - {self.type.name}'


class Collection(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата и время изменения')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    bookmarks = models.ManyToManyField(Bookmark, blank=True, verbose_name='Закладки страницы')

    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'

    def __str__(self):
        return self.title
