import pytest
from django.test import Client


@pytest.fixture
def client():
    return Client()


@pytest.mark.django_db
def test_category_posts_renders_correct_template(client):
    response = client.get('/category/travel/')
    assert response.status_code == 200
    assert len(response.templates) > 0, 'Шаблон не был использован'
    assert response.templates[0].name == 'category.html'


@pytest.mark.django_db
def test_category_posts_passes_slug_to_context(client):
    response = client.get('/category/adventure/')
    assert response.status_code == 200
    assert 'category' in response.context, 'В контексте нет переменной category'
    assert response.context['category'].slug == 'adventure'
