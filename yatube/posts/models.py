from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import UniqueConstraint

User = get_user_model()


class Group(models.Model):
    """Модель представления Группы(сообщества)
    имеет следующую структуру и ограничения:
    имя - tittle (длина не более 200 символов)
    адрес - slug (уникальное значение);
    описание - description
    """
    title = models.CharField(
        max_length=200,
        verbose_name='Название группы',
        help_text='Введите название группы',
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='Уникальный идентификатор группы',
        help_text='Введите уникальный идентификатор группы',
    )
    description = models.TextField(
        verbose_name='Описание группы',
        help_text='Введите описание группы',
    )

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self) -> str:
        return self.title


class Post(models.Model):
    """Модель представления Постов(записей)
    имеет следующую стркутуру и ограничения:
    текст - text;
    дата публикации - pub_date(автоматически
    добавляется текущая дата);
    автор - author (ссылка на модель User)
    сообщество - group (ссылка на модель Group)"""
    text = models.TextField(
        verbose_name='Текст поста',
        help_text='Введите текст поста'
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True,
        help_text='Укажите дату публикации',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор поста',
        help_text='Укажите автора поста',
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='posts',
        blank=True,
        null=True,
        verbose_name='Группа',
        help_text='Выбор группы',
    )
    image = models.ImageField(
        'Картинка',
        upload_to='posts/',
        blank=True,
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self) -> str:
        return self.text[:settings.CROP_TEXT]


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Пост',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор данного комментария',
        help_text='Укажите автора комментария',
    )
    text = models.TextField(
        verbose_name='Текст комментария',
        help_text="Укажите дату публикации"
    )
    created = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True,
        help_text='Укажите дату публикации',
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Коментарии'


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик',
        help_text='Имя подписчика',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор контента',
    )

    class Meta:
        UniqueConstraint(fields=['author', 'user'], name='follow_unique')
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
