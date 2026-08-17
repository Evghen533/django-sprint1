# tests/test_templates.py
import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_post_detail_pages(client, posts):
    for i, post in enumerate(posts):
        url = reverse("blog:post_detail", args=[post.pk])
        response = client.get(url)
        assert (
            response.status_code == 200
        ), f"Страница поста {post.pk} должна возвращать 200"
        assert response.context is not None
        assert response.context.get("post") is not None
        assert response.context["post"].pk == post.pk
        assert response.context["post"].title == post.title

        content = response.content.decode("utf-8")
        assert (
            post.title in content
        ), f"Заголовок поста '{post.title}' не найден в HTML."


@pytest.mark.django_db
def test_post_list(client, posts):
    url = reverse("blog:index")
    response = client.get(url)
    assert response.status_code == 200

    assert response.context is not None
    assert "posts" in response.context
    context_posts = response.context["posts"]
    expected_count = sum(1 for p in posts if p.is_published)
    assert len(context_posts) == expected_count, (
        f"Ожидалось {expected_count} постов на главной, "
        f"но получено {len(context_posts)}"
    )

    context_titles = [p.title for p in context_posts]
    for post in posts:
        if post.is_published:
            assert (
                post.title in context_titles
            ), f"Пост '{post.title}' опубликован, но не найден в контексте."

    content = response.content.decode("utf-8")
    assert any(
        p.title in content for p in posts if p.is_published
    ), "Ни один из опубликованных постов не найден в HTML главной страницы."
