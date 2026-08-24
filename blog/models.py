from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок", blank=True)
    text = models.TextField(verbose_name="Текст")
    content = models.TextField(blank=True, null=True)  # оставляем как просили
    slug = models.SlugField(unique=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    location = models.CharField(max_length=100, verbose_name="Место", blank=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        null=True,
        blank=True,
        related_name="posts",
    )

    def save(self, *args, **kwargs):
        if not self.slug and self.title:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
