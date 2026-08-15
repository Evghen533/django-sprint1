import pytest
from django.urls import reverse
from blog.models import Category, Post


@pytest.mark.django_db
def test_post_list_page_has_posts():
    """
    Проверяет, что главная страница (/) возвращает статус 200
    и содержит хотя бы один опубликованный пост.
    """
    category = Category.objects.create(title="Путешествия", slug="travel")

    post = Post.objects.create(  # <-- присвой переменной
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
    assert post.title in html, f"Заголовок '{post.title}' должен быть в HTML"


@pytest.mark.django_db
def test_blog_posts(try_get_url, posts):
    """
    Проверяет логику отображения постов разных категорий.
    Использует фикстуру 'posts' из conftest.py — она уже создала
    все тестовые данные.
    Никаких дополнительных create/get_or_create здесь быть не должно.
    """
    url = reverse("blog:index")
    response = try_get_url(url)

    assert response.status_code == 200

    posts_in_context = response.context.get("posts")
    assert posts_in_context is not None
    assert len(posts_in_context) >= 3

    # Превращаем список постов в словарь по slug для удобной проверки
    posts_by_slug = {p.slug: p for p in posts_in_context}

    expected_slugs = [
        "storm-and-wreck",
        "ship-unstuck",
        "third-post",
    ]

    for slug in expected_slugs:
        assert slug in posts_by_slug, (
            f"Пост с slug='{slug}' не найден в контексте"
        )

    # Проверяем контент строго по реальным текстам из conftest.py
    first_post = posts_by_slug["storm-and-wreck"]
    assert (
        "Всю ночь и весь день шёл дождь и дул сильный "
        "порывистый ветер"
    ) in first_post.content

    second_post = posts_by_slug["ship-unstuck"]
    assert "После шторма корабль наконец снялся с мели" in second_post.content

    third_post = posts_by_slug["third-post"]
    assert "Прогулка по городу в пасмурный день" in third_post.content

    # Проверка категорий (теперь совпадает с conftest.py)
    assert first_post.category.slug == "travel"
    assert second_post.category.slug == "adventure"
    # Третий пост тоже в категории travel — как в conftest.py
    assert third_post.category.slug == "travel"
