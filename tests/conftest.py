import pytest
from django.test import Client
from blog.models import Post, Category
from datetime import datetime
import django.utils.timezone as timezone


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def try_get_url(client):
    def _try_get_url(url: str):
        response = client.get(url)
        if response.status_code < 300:
            return response
        raise AssertionError(f'Не удалось загрузить `{url}`: статус {response.status_code}')
    return _try_get_url


@pytest.fixture(scope="function")
def posts(django_db_blocker):
    with django_db_blocker.unblock():
        # Очищаем данные перед каждым тестом, чтобы не было пересечений
        Post.objects.all().delete()
        Category.objects.all().delete()

        cat_travel = Category.objects.create(title="Путешествия", slug="travel")
        cat_adventure = Category.objects.create(title="Приключения", slug="adventure")
        cat_city = Category.objects.create(title="Город", slug="city")

        # Создаём посты по одному — так мы точно контролируем порядок и можем легко менять поля
        p1 = Post.objects.create(
            title="Шторм и крушение",
            content="Текст первого поста",
            created_at=timezone.make_aware(datetime(2025, 1, 1, 10, 0, 0)),
            is_published=True,
            category=cat_travel,
        )
        p2 = Post.objects.create(
            title="Корабль сняло с мели",
            content="Текст второго поста",
            created_at=timezone.make_aware(datetime(2025, 1, 2, 11, 0, 0)),
            is_published=True,
            category=cat_adventure,
        )
        p3 = Post.objects.create(
            title="Третий пост",
            content="Текст третьего поста",
            created_at=timezone.make_aware(datetime(2025, 1, 3, 12, 0, 0)),
            is_published=True,
            category=cat_city,
        )

    return [p1, p2, p3]
