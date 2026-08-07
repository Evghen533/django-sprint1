import pytest
from django.test import Client
from blog.models import Post, Category

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
        Post.objects.all().delete()
        Category.objects.all().delete()

        cat_travel = Category.objects.create(title="Travel", slug="travel")
        cat_adventure = Category.objects.create(title="Adventure", slug="adventure")
        cat_city = Category.objects.create(title="City", slug="city")

        from datetime import datetime
        import django.utils.timezone as timezone

        created = Post.objects.bulk_create([
            Post(
                title="Шторм и крушение",
                content="Текст первого поста",          # ← было text, стало content
                created_at=timezone.make_aware(datetime(2025, 1, 1, 10, 0, 0)),
                is_published=True,
                category=cat_travel,
            ),
            Post(
                title="Корабль сняло с мели",
                content="Текст второго поста",         # ← было text
                created_at=timezone.make_aware(datetime(2025, 1, 2, 11, 0, 0)),
                is_published=True,
                category=cat_adventure,
            ),
            Post(
                title="Третий пост",
                content="Текст третьего поста",        # ← было text
                created_at=timezone.make_aware(datetime(2025, 1, 3, 12, 0, 0)),
                is_published=True,
                category=cat_city,
            ),
        ])
    return created

@pytest.fixture()
def settings_app_name():
    return 'blogicum'


@pytest.fixture()
def root_dir():
    from pathlib import Path
    return str(Path(__file__).parent.parent)


@pytest.fixture()
def project_dirname():
    return 'blogicum'
