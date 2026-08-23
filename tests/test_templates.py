import re                      # <-- добавлено для test_post_list
import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed
from blog.models import Post, Category  # <-- импортируем модели

@pytest.mark.parametrize(
    'view_name, kwargs, template', [
        ('blog:index', {}, 'index.html'),
        ('blog:post_detail', {'post_id': 1}, 'detail.html'),
        ('blog:post_detail', {'post_id': 2}, 'detail.html'),
        ('blog:post_detail', {'post_id': 3}, 'detail.html'),
        ('blog:category_posts', {'category_slug': 'travel'}, 'category.html'),
        ('pages:about', {}, 'about.html'),
        ('pages:rules', {}, 'rules.html'),
    ]
)
@pytest.mark.django_db
def test_page_templates(client, view_name, kwargs, template):
    # Создаём посты прямо здесь, чтобы тест был независимым
    if view_name == 'blog:post_detail':
        # Создаём категории, если их нет
        cat_travel, _ = Category.objects.get_or_create(slug='travel', defaults={'name': 'Путешествия'})
        cat_adventure, _ = Category.objects.get_or_create(slug='adventure', defaults={'name': 'Приключения'})

        # Очищаем, чтобы не дублировать при повторных запусках (опционально)
        Post.objects.filter(id__in=[1, 2, 3]).delete()

        Post.objects.create(id=1, title='Post 1', text='Text 1', category=cat_travel, location='Loc 1')
        Post.objects.create(id=2, title='Post 2', text='Text 2', category=cat_adventure, location='Loc 2')
        Post.objects.create(id=3, title='Post 3', text='Text 3', category=cat_travel, location='Loc 3')

    url = reverse(view_name, kwargs=kwargs)
    response = client.get(url)
    assert response.status_code == 200, f"URL {url} должен возвращать 200, а получил {response.status_code}"
    assertTemplateUsed(response, template, msg_prefix=f'Убедитесь, что для `{url}` используется шаблон `{template}`.')


@pytest.mark.django_db
@pytest.mark.parametrize('post_id', (1, 2, 3))
def test_post_detail(post_id, client, posts):
    url = f'/posts/{post_id}/'
    response = client.get(url)
    assert response.status_code == 200

    post_obj = response.context.get('post')
    assert post_obj is not None, 'Контекст не содержит ключ "post"'

    expected_post = posts[post_id - 1]
    assert expected_post == post_obj, f'На странице {url} должен быть пост с ID {post_id}'


@pytest.mark.django_db
def test_post_list(client, posts):
    url = '/'
    response = client.get(url)
    assert response.status_code == 200

    reversed_posts = list(reversed(posts))
    reversed_truncated_post_texts = [p.text[:20] for p in reversed_posts]

    pattern = re.compile(r'[\s\S]+?'.join(reversed_truncated_post_texts))
    page_content = response.content.decode('utf-8')

    assert re.search(pattern, page_content), (
        f'Убедитесь, что на странице `{url}` выводится инвертированный список постов.'
    )
