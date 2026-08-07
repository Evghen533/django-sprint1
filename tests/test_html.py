from django.urls import reverse, NoReverseMatch
import pytest

@pytest.mark.django_db
def test_post_detail_page_content(try_get_url, posts):
    if not posts:
        pytest.skip("Нет постов для теста")
    post = posts[0]
    url = reverse('blog:post_detail', args=[post.pk])
    response = try_get_url(url)
    assert response.status_code == 200

    assert post.title in response.content.decode(), f"Заголовок '{post.title}' не найден"

    expected_date = post.created_at.strftime("%d.%m.%Y %H:%M")
    assert expected_date in response.content.decode(), "Дата поста не найдена на странице"

@pytest.mark.django_db
def test_post_list_page_has_posts(try_get_url, posts):
    url = reverse('blog:post_list')  # будет /
    response = try_get_url(url)
    assert response.status_code == 200

    if posts:
        assert posts[0].title in response.content.decode()
