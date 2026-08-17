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
    response = try_get_url("/")
    assert response.status_code == 200

    # Проверяем, что view передаёт список постов в контекст
    posts_in_context = response.context.get("posts")
    assert posts_in_context is not None, "В контексте страницы нет переменной posts"
    assert len(posts_in_context) >= 3, "На странице должно быть как минимум 3 поста"

    html = response.content.decode("utf-8")

    # Проверяем, что все опубликованные посты из фикстуры есть в контексте и в HTML
    for post in posts:
        if post.is_published:
            assert post.title in [p.title for p in posts_in_context], \
                f"Пост '{post.title}' опубликован, но не найден в контексте"
            assert post.title in html,  \
                f"Заголовок '{post.title}' не найден в HTML страницы"

    # Дополнительная страховка: все посты на странице должны быть опубликованными
    for p in posts_in_context:
        assert p.is_published is True, f"В списке постов на странице оказался неопубликованный пост: {p.title}"
