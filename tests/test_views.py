# tests/test_views.py
import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_post_list_page_has_posts(try_get_url, posts):
    """
    Проверяет, что главная страница (/) возвращает статус 200
    и содержит хотя бы один опубликованный пост из фикстуры posts.
    """
    response = try_get_url("/")
    assert response.status_code == 200, f"URL / должен возвращать 200, получил {response.status_code}"

    html = response.content.decode("utf-8")

    # Проверяем, что хотя бы один опубликованный пост виден на странице
    published_posts = [p for p in posts if p.is_published]
    assert len(published_posts) > 0, "Нет опубликованных постов для теста — проверь фикстуру posts в conftest.py"

    for post in published_posts:
        assert post.title in html, f"Заголовок '{post.title}' не найден в HTML главной страницы"


@pytest.mark.django_db
def test_blog_posts(try_get_url, posts):
    """
    Проверяет логику отображения постов на главной странице.
    Использует фикстуру 'posts' — никаких ручных create/get_or_create здесь быть не должно.
    Не проверяет жёстко тексты внутри content, только заголовки и наличие в контексте/HTML.
    """
    url = reverse("blog:index")
    response = try_get_url(url)
    assert response.status_code == 200

    posts_in_context = response.context.get("posts")
    assert posts_in_context is not None
    assert len(posts_in_context) >= 1, "На главной должно быть хотя бы 1 опубликованный пост"

    # Собираем список заголовков из контекста
    context_titles = [p.title for p in posts_in_context]

    # Проверяем, что все опубликованные посты из фикстуры есть в контексте
    for post in posts:
        if post.is_published:
            assert post.title in context_titles, f"Пост '{post.title}' опубликован, но не найден в контексте"

    # Проверяем наличие заголовков в HTML
    html = response.content.decode("utf-8")
    for post in posts:
        if post.is_published:
            assert post.title in html, f"Заголовок '{post.title}' не найден в HTML"
