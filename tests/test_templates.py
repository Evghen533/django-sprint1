import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

@pytest.mark.parametrize(
    'view_name, kwargs, template', [
        ('blog:index', {}, 'index.html'),
        ('blog:post_detail', {'id': 1}, 'detail.html'),
        ('blog:post_detail', {'id': 2}, 'detail.html'),
        ('blog:post_detail', {'id': 3}, 'detail.html'),
        ('blog:category_posts', {'category_slug': 'travel'}, 'category.html'),
        ('pages:about', {}, 'about.html'),
        ('pages:rules', {}, 'rules.html'),
    ]
)
@pytest.mark.django_db
def test_page_templates(client, view_name, kwargs, template):
    url = reverse(view_name, kwargs=kwargs)
    response = client.get(url)
    assert response.status_code == 200, f"URL {url} должен возвращать 200, а получил {response.status_code}"
    assertTemplateUsed(response, template, msg_prefix=f'Убедитесь, что для `{url}` используется шаблон `{template}`.')


@pytest.mark.django_db
@pytest.mark.parametrize('post_id', (1, 2, 3))
def test_post_detail(post_id, client, posts):
    post = posts[post_id - 1]
    url = reverse('blog:post_detail', kwargs={'id': post.id})
    response = client.get(url)
    assert response.status_code == 200

    post_obj = response.context.get('post')
    assert post_obj is not None, 'Контекст не содержит ключ "post"'
    assert post == post_obj, f'На странице {url} должен быть пост {post}'


@pytest.mark.django_db
def test_post_list(client, posts):
    url = '/'
    response = client.get(url)
    assert response.status_code == 200

    posts_in_context = response.context.get('posts')
    assert posts_in_context is not None, 'В контексте страницы списка постов нет переменной "posts"'

    expected_posts = list(reversed(posts))
    assert list(posts_in_context) == expected_posts, (
        'Список постов на главной должен соответствовать ожидаемому (возможно, в обратном порядке).'
    )
