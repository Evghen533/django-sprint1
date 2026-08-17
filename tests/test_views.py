# tests/test_views.py
import pytest

MONTHS = {
    1: "января", 2: "февраля", 3: "марта", 4: "апреля", 5: "мая", 6: "июня",
    7: "июля", 8: "августа", 9: "сентября", 10: "октября", 11: "ноября", 12: "декабря"
}

@pytest.mark.django_db
def test_blog_posts_page(client, posts):
    """Тест страницы списка постов (HTML)"""
    response = client.get("/")
    assert response.status_code == 200

    posts_in_context = response.context.get("posts")
    assert posts_in_context is not None
    assert len(posts_in_context) >= 3

    html = response.content.decode("utf-8")

    for post in posts:
        if post.is_published:
            assert post.title in [p.title for p in posts_in_context]
            assert post.title in html

    for p in posts_in_context:
        assert p.is_published is True


@pytest.mark.django_db
def test_blog_posts_api(client, posts):
    """Тест JSON API для списка постов"""
    response = client.get("/api/posts/")

    assert response.status_code == 200
    assert response["Content-Type"].startswith("application/json")

    data = response.json()
    api_posts = data.get("posts", [])
    assert len(api_posts) == 3

    for i, post in enumerate(posts):
        api_post = api_posts[i]
        assert api_post["id"] == i
        assert api_post["location"] == "Остров отчаянья"
        assert api_post["category"] == post.category.slug

        assert api_post["text"].strip() == post.content.strip()

        expected_date = f"{post.date.day} {MONTHS[post.date.month]} {post.date.year} года"
        assert api_post["date"] == expected_date

        allowed_keys = {"id", "location", "date", "category", "text"}  # <-- тоже меняем на content
        assert set(api_post.keys()) == allowed_keys
