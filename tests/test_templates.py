import pytest
from django.urls import reverse


@pytest.mark.parametrize(
    'view_name, kwargs, template', [
        ('blog:index', {}, 'index.html'),
        ('blog:post_detail', {'id': 1}, 'detail.html'),
        ('blog:post_detail', {'id': 2}, 'detail.html'),
        ('blog:category_posts', {'category_slug': 'travel'}, 'category.html'),
        ('pages:about', {}, 'about.html'),
        ('pages:rules', {}, 'rules.html'),
    ]
)
def test_page_templates(client, view_name, kwargs, template):
    url = reverse(view_name, kwargs=kwargs)
    response = client.get(url)
    assert response.status_code == 200, (
        f"URL {url} должен возвращать 200, "
        "а получил {response.status_code}"
    )


@pytest.mark.parametrize('post_id', (0, 1, 2))
def test_post_detail(post_id, client):
    url = reverse('blog:post_detail', kwargs={'id': post_id})
    response = client.get(url)
    assert response.status_code == 200

    post_obj = response.context.get('post')
    assert post_obj is not None, 'Контекст не содержит ключ "post"'

    assert post_obj['id'] == post_id
    assert post_obj['location'] == 'Остров отчаянья'
    assert post_obj['date'] in (
        '30 сентября 1659 года',
        '1 октября 1659 года',
        '25 октября 1659 года'
    )
    assert post_obj['category'] in ('travel', 'not-my-day')
    assert 'корабль' in post_obj['text'] or 'дождь' in post_obj['text']


def test_post_list(client):
    url = "/"
    response = client.get(url)

    assert response.status_code == 200

    posts_in_context = response.context.get('posts')
    assert posts_in_context is not None, (
        "В контексте страницы списка постов нет переменной \"posts\""
    )

    assert len(posts_in_context) == 3, "Должно быть 3 поста"

    expected_ids = [0, 1, 2]
    actual_ids = [post['id'] for post in posts_in_context]

    assert actual_ids == expected_ids, f"Неверные ID постов: {actual_ids}"

    for post in posts_in_context:
        assert 'location' in post
        assert 'date' in post
        assert 'category' in post
        assert 'text' in post
