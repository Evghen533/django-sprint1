import pytest
from django.test import RequestFactory
from blog.views import category_posts

@pytest.fixture
def rf():
    return RequestFactory()

def test_category_posts_renders_correct_template(rf):
    request = rf.get('/category/travel/')
    response = category_posts(request, 'travel')
    assert response.status_code == 200
    # Проверяем, что используется нужный шаблон
    assert response.template_name == 'category.html'

def test_category_posts_passes_slug_to_context(rf):
    request = rf.get('/category/adventure/')
    response = category_posts(request, 'adventure')
    assert response.status_code == 200
    assert 'category_slug' in response.context_data
    assert response.context_data['category_slug'] == 'adventure'
