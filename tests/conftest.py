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
    """Просто делает GET и возвращает response. Проверки статуса делает тест."""
    def _try_get_url(url: str):
        return client.get(url)
    return _try_get_url


@pytest.fixture(scope="function")
def posts():
    """Создаёт 3 опубликованных поста с разными категориями."""
    cat_travel = Category.objects.create(name="Путешествия", slug="travel")
    cat_adventure = Category.objects.create(name="Приключения", slug="adventure")
    cat_city = Category.objects.create(name="Город", slug="city")

    now = timezone.now()

    post1 = Post.objects.create(
        title="Шторм и крушение",
        slug="storm-and-wreck",
        content=(
            "Всю ночь и весь день шёл дождь и дул сильный "
            "порывистый ветер. Корабль за ночь разбило в щепки."
        ),
        date=now.date(),
        location="Остров отчаяния",
        category=cat_travel,
        is_published=True,
    )
    post2 = Post.objects.create(
        title="Корабль снялся с мели",
        slug="ship-unstuck",
        content=(
            "После шторма корабль наконец снялся с мели, "
            "и команда смогла продолжить путь."
        ),
        date=now.date(),
        location="Берег острова",
        category=cat_adventure,
        is_published=True,
    )
    post3 = Post.objects.create(
        title="Третий пост: город",
        slug="third-post",
        content=(
            "Прогулка по городу в пасмурный день: "
            "старые дома, узкие улочки и запах дождя."
        ),
        date=now.date(),
        location="Город",
        category=cat_travel,
        is_published=True,
    )

    return [post1, post2, post3]
