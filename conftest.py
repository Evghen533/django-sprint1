import os
import sys
import django
import pytest
from django.test import Client
from blog.models import Post, Category
from datetime import datetime
import django.utils.timezone as timezone

# ---------------------------------------------------------
# 1. ЖЁСТКАЯ НАСТРОЙКА ПУТИ К ПРОЕКТУ
# ---------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blogicum.settings")
django.setup()
# ---------------------------------------------------------


@pytest.fixture
def root_dir():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


@pytest.fixture
def project_dirname():
    return "django-sprint1"


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def try_get_url(client):
    def _try_get_url(url: str):
        response = client.get(url)
        if response.status_code < 300:
            return response
        raise AssertionError(
            f"Не удалось загрузить `{url}`: статус {response.status_code}"
        )
    return _try_get_url


@pytest.fixture(scope="function")
def posts(django_db_blocker):
    with django_db_blocker.unblock():
        Post.objects.all().delete()
        Category.objects.all().delete()

        cat_travel = Category.objects.create(
            name="Путешествия", slug="travel"
        )
        cat_adventure = Category.objects.create(
            name="Приключения", slug="adventure"
        )
        cat_city = Category.objects.create(
            name="Город", slug="city"
        )

        p1 = Post.objects.create(
            title="Шторм и крушение",
            content="Текст первого поста",
            created_at=timezone.make_aware(
                datetime(2025, 1, 1, 10, 0, 0)
            ),
            is_published=True,
            category=cat_travel,
        )
        p2 = Post.objects.create(
            title="Корабль сняло с мели",
            content="Текст второго поста",
            created_at=timezone.make_aware(
                datetime(2025, 1, 2, 11, 0, 0)
            ),
            is_published=True,
            category=cat_adventure,
        )
        p3 = Post.objects.create(
            title="Третий пост",
            content="Текст третьего поста",
            created_at=timezone.make_aware(
                datetime(2025, 1, 3, 12, 0, 0)
            ),
            is_published=True,
            category=cat_city,
        )
    return [p1, p2, p3]
