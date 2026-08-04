from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=200, blank=True)
    category = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title
