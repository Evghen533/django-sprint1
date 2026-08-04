import pytest
from django.test import Client
from blog.models import Post

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
        created = Post.objects.bulk_create([
            Post(title="Пост 1", text="Текст первого поста", date="2025-01-01", location="Москва", category="travel"),
            Post(title="Пост 2", text="Текст второго поста", date="2025-01-02", location="Санкт-Петербург", category="adventure"),
            Post(title="Пост 3", text="Текст третьего поста", date="2025-01-03", location="Казань", category="city"),
        ])
    return list(created)

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
