import pytest
from django.urls import reverse


@pytest.mark.parametrize(
    'view_name, kwargs, template', [
        ('blog:index', {}, 'index.html'),
        ('pages:about', {}, 'about.html'),
        ('pages:rules', {}, 'rules.html'),
    ]
)
def test_page_templates(client, view_name, kwargs, template):
    url = reverse(view_name, kwargs=kwargs)
    response = client.get(url)
    assert response.status_code == 200, (
        f"URL {url} должен возвращать 200, а получил {response.status_code}"
    )

    if view_name.startswith('blog'):
        expected_template = f'blog/{template}'
    else:
        expected_template = f'pages/{template}'

    assert any(t.name == expected_template for t in response.templates), (
        f'Не использован ожидаемый шаблон {expected_template}',
        'найдены: {[t.name for t in response.templates]}'
    )
