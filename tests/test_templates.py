import pytest
from django.urls import reverse
from blog.models import Post


@pytest.mark.django_db
@pytest.mark.parametrize("post_index", [0, 1, 2])
def test_post_detail_pages(posts, try_get_url, post_index):
    post = posts[post_index]
    url = reverse('blog:post_detail', args=[post.pk])
    response = try_get_url(url)
    assert response.status_code == 200

    assert response.context is not None
    assert response.context.get("post") is not None
    assert response.context["post"].pk == post.pk
    assert response.context["post"].title == post.title

    content = response.content.decode("utf-8")
    assert post.title in content, f"Заголовок поста '{post.title}' не найден в HTML."

@pytest.mark.django_db
def test_post_list(posts, try_get_url):
    url = reverse('blog:post_list')
    response = try_get_url(url)
    assert response.status_code == 200

    assert response.context is not None
    assert "posts" in response.context

    context_posts = response.context["posts"]
    assert len(context_posts) == 3

    context_titles = [p.title for p in context_posts]
    for post in posts:
        assert post.title in context_titles

    content = response.content.decode("utf-8")
    assert any(p.title in content for p in posts), "Ни один из заголовков постов не найден в HTML главной страницы."
