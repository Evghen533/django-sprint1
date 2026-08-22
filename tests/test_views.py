import pytest
from django.test import RequestFactory
from blog.views import category_posts

# 1. Создаем свои тестовые данные.
# Они могут отличаться от тех, что у тебя в views.py, это нормально.
# Главное — проверить логику фильтрации.
TEST_POSTS = [
    {'id': 0, 'location': 'Остров отчаянья', 'date': '30 сентября 1659', 'text': 'Текст про остров', 'category': 'travel'},
    {'id': 1, 'location': 'Плохой день', 'date': '1 января 1660', 'text': 'Текст про неудачу', 'category': 'not-my-day'},
    {'id': 2, 'location': 'Кругосветка', 'date': '5 мая 1661', 'text': 'Текст про плавание', 'category': 'travel'},
]

@pytest.fixture
def rf():
    """Фикстура для создания фейковых запросов"""
    return RequestFactory()

@pytest.fixture
def mock_posts(monkeypatch):
    """Фикстура, которая временно подменяет список posts в views.py на наш TEST_POSTS"""
    monkeypatch.setattr('blog.views.posts', TEST_POSTS)

def test_category_posts_filters_travel(rf, mock_posts):
    """Тест: проверяем, что для категории 'travel' возвращаются только посты этой категории"""
    request = rf.get('/category/travel/')
    response = category_posts(request, 'travel')

    # Проверяем, что страница открылась (статус 200)
    assert response.status_code == 200

    # Проверяем контекст: в нем должен быть ключ 'posts'
    assert 'posts' in response.context_data

    filtered_posts = response.context_data['posts']

    # Логика проверки:
    # 1. Должно быть ровно 2 поста (Остров и Кругосветка)
    assert len(filtered_posts) == 2

    # 2. Проверяем, что все они действительно из категории travel
    for post in filtered_posts:
        assert post['category'] == 'travel'

    # 3. Проверяем, что пост из другой категории НЕ попал в список
    # (косвенная проверка: если длина 2 и все travel, значит not-my-day отфильтрован)

def test_category_posts_empty_for_unknown(rf, mock_posts):
    """Тест: проверяем, что для несуществующей категории список пуст"""
    request = rf.get('/category/unknown/')
    response = category_posts(request, 'unknown')

    assert response.status_code == 200
    assert 'posts' in response.context_data

    filtered_posts = response.context_data['posts']
    assert len(filtered_posts) == 0
