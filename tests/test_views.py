import pytest


@pytest.mark.django_db
def test_category_posts_renders_correct_template(client):
    response = client.get('/category/travel/')
    assert response.status_code == 200
    assert len(response.templates) > 0, 'Шаблон не был использован'
    assert response.templates[0].name == 'blog/category.html'


@pytest.mark.django_db
def test_category_posts_passes_slug_to_context(client):
    response = client.get('/category/adventure/')
    assert response.status_code == 200
    assert 'category_slug' in response.context, 'В контексте нет переменной category_slug'
    assert response.context['category_slug'] == 'adventure'


@pytest.mark.django_db
def test_blog_posts(client):
    response = client.get('/')
    assert response.status_code == 200
    posts = response.context.get('posts')
    assert posts is not None, 'Контекст не содержит ключ "posts"'
    assert len(posts) == 3, f'Ожидается 3 поста, а получено {len(posts)}'
    # Проверяем, что у каждого поста есть id, location, date, category, text
    for post in posts:
        assert 'id' in post
        assert 'location' in post
        assert 'date' in post
        assert 'category' in post
        assert 'text' in post
