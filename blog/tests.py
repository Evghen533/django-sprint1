import pytest
from django.utils import timezone
from blog.models import Post

@pytest.mark.django_db
def test_post_creation():
    post = Post.objects.create(
        title="Тестовый пост",
        text="Это тестовый текст для проверки модели.",
        location="Москва",
        category="Разное"
    )
    assert post.title == "Тестовый пост"
    assert post.text == "Это тестовый текст для проверки модели."
    assert post.location == "Москва"
    assert post.category == "Разное"
    assert post.date is not None
    assert isinstance(post.date, timezone.datetime)
