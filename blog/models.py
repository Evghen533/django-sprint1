from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    date = models.DateField("Дата")
    location = models.CharField(
        "Место", max_length=200, help_text="Например: Остров отчаянья"
    )
    created_at = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)
    image = models.ImageField(upload_to="posts/", blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, related_name="posts"
    )

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title
