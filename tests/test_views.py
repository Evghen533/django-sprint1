import pytest
from django.urls import reverse
from blog.models import Category, Post


@pytest.mark.django_db
def test_post_list_page_has_posts():
    """
    Проверяет, что главная страница (/) возвращает статус 200
    и содержит хотя бы один опубликованный пост.
    Этот тест сам создаёт данные, потому что не зависит от фикстуры posts.
    """
    category = Category.objects.create(title="Путешествия", slug="travel")

    Post.objects.create(
        title="Первый пост",
        slug="first-post",
        content="Текст первого поста",
        category=category,
        is_published=True,
    )

    from django.test import Client
    client = Client()
    response = client.get('/')
    assert response.status_code == 200

    html = response.content.decode("utf-8")
    assert "Первый пост" in html


@pytest.mark.django_db
def test_blog_posts(try_get_url, posts):
    """
    Проверяет логику отображения постов разных категорий.
    Использует фикстуру 'posts' из conftest.py — она уже создала все тестовые данные.
    Никаких дополнительных create/get_or_create здесь быть не должно.
    """
    url = reverse("blog:post_list")
    response = try_get_url(url)

    assert response.status_code == 200

    posts_in_context = response.context.get("posts")
    assert posts_in_context is not None
    assert len(posts_in_context) >= 3

    # Превращаем список постов в словарь по slug для удобной проверки
    posts_by_slug = {p.slug: p for p in posts_in_context}

    # Эти slug должны точно совпадать с теми, что создаёт фикстура posts в conftest.py
    expected_slugs = [
        "storm-and-wreck",
        "ship-unstuck",
        "third-post"
    ]

    for slug in expected_slugs:
        assert slug in posts_by_slug, f"Пост с slug='{slug}' не найден в контексте"

    # Проверяем контент строго по нужным постам
    # Здесь используем тот текст, который реально задан в conftest.py
    assert "Текст первого поста" in posts_by_slug["storm-and-wreck"].content
    assert "Текст второго поста" in posts_by_slug["ship-unstuck"].content
    assert "Текст третьего поста" in posts_by_slug["third-post"].content

    # Проверка категорий (опционально, но полезно)
    assert posts_by_slug["storm-and-wreck"].category.slug == "travel"
    assert posts_by_slug["ship-unstuck"].category.slug == "adventure"
    assert posts_by_slug["third-post"].category.slug == "city"
