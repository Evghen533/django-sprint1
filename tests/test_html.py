import pytest

@pytest.mark.django_db
def test_post_detail_page_content(try_get_url, posts):
    # posts — это список, поэтому берем первый элемент через [0], а не .first()
    if not posts:
        pytest.skip("Нет постов для теста")

    post = posts[0]
    url = f"/{post.pk}/"
    response = try_get_url(url)

    assert post.title in response.content.decode(), f"Заголовок '{post.title}' не найден на странице детали"
    assert str(post.date) in response.content.decode(), "Дата поста не найдена на странице"

@pytest.mark.django_db
def test_post_list_page_has_posts(try_get_url, posts):
    response = try_get_url("/")
    assert response.status_code == 200

    if posts:
        assert posts[0].title in response.content.decode()
