from django.db import models
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(
        max_length=200,
        help_text="Введите заголовок поста, он должен быть уникальным и понятным для читателя",
    )
    slug = models.SlugField(unique=True)
    content = models.TextField()
    date = models.CharField(
        "Дата", max_length=100, help_text="Например: 30 сентября 1659 года"
    )
    location = models.CharField(
        "Место", max_length=200, help_text="Например: Остров отчаянья"
    )
    created_at = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)
    published_at = models.DateTimeField(null=True, blank=True)
    image = models.ImageField(upload_to="posts/", blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, related_name="posts"
    )

    def __str__(self):
        return self.title
