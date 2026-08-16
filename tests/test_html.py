import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_post_detail_page_content(try_get_url, posts):
    if not posts:
        pytest.skip("Нет постов для теста")

    post = posts[0]
    url = reverse(
        "blog:post_detail",
        args=[post.pk],
    )
    response = try_get_url(url)

    assert response.status_code == 200
    assert post.title in response.content.decode()
    assert post.content in response.content.decode()


@pytest.mark.django_db
def test_post_list_page_has_posts(try_get_url, posts):
    url = reverse("blog:index")
    response = try_get_url(url)

    assert response.status_code == 200, f"URL {url} должен возвращать 200"

    html = response.content.decode("utf-8")
    for post in posts:
        assert (
            post.title in html
        ), f"Заголовок поста '{post.title}' не найден в HTML страницы."
