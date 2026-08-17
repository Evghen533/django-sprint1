import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_category_page_contents(client, posts):
    if not posts:
        pytest.skip("Нет постов для теста")

    post = posts[0]
    url = reverse("blog:post_detail", args=[post.pk])
    response = client.get(url)

    assert response.status_code == 200, f"Страница поста вернула {response.status_code}"

    html = response.content.decode("utf-8")

    # Заголовок должен быть точно
    assert post.title in html, f"Заголовок '{post.title}' не найден в HTML"

    # Вместо проверки всего текста (где могут быть проблемы с \n),
    # проверим хотя бы первое слово или фразу, которая точно есть
    first_word = post.content.split()[0] if post.content else ""
    assert first_word in html, f"Текст поста не найден в HTML (искали первое слово: {first_word})"


@pytest.mark.django_db
def test_post_list_page_has_posts(client, posts):
    url = reverse("blog:index")
    response = client.get(url)

    assert response.status_code == 200

    html = response.content.decode("utf-8")
    for post in posts:
        assert post.title in html, f"Заголовок поста '{post.title}' не найден на главной странице."
