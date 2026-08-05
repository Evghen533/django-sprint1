from django.db import models
from django.utils import timezone

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    # Добавь эти поля, если их нет:
    created_at = models.DateTimeField(default=timezone.now)  # Дата создания
    is_published = models.BooleanField(default=False)        # Флаг публикации
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title
