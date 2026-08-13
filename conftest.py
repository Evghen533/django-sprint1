import pytest
from django.test import Client
from blog.models import Post, Category
from django.utils import timezone


@pytest.fixture
def root_dir():
    import os
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
        # Очищаем данные перед каждым тестом
        Post.objects.all().delete()
        Category.objects.all().delete()

        # Создаём категории
        cat_travel = Category.objects.create(
            title="Путешествия",
            slug="travel"
        )
        cat_adventure = Category.objects.create(
            title="Приключения",
            slug="adventure"
        )

        # Создаём посты
        post1 = Post.objects.create(
            title="Шторм и крушение",
            slug="storm-and-wreck",
            content=(
                "Всю ночь и весь день шёл дождь и дул сильный "
                "порывистый ветер. Корабль за ночь разбило в щепки."
            ),
            category=cat_travel,
            published_at=timezone.now(),
            is_published=True,
        )
        post2 = Post.objects.create(
            title="Корабль снялся с мели",
            slug="ship-unstuck",
            content=(
                "После шторма корабль наконец снялся с мели, "
                "и команда смогла продолжить путь."
            ),
            category=cat_adventure,
            published_at=timezone.now(),
            is_published=True,
        )
        post3 = Post.objects.create(
            title="Третий пост: город",
            slug="third-post",
            content=(
                "Прогулка по городу в пасмурный день: "
                "старые дома, узкие улочки и запах дождя."
            ),
            category=cat_travel,
            published_at=timezone.now(),
            is_published=True,
        )

        return [post1, post2, post3]
