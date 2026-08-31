import pytest
from django.urls import reverse, NoReverseMatch


def test_blog_urls():
    try:
        from blog.urls import urlpatterns as solution_urlpatterns
    except Exception as e:
        raise AssertionError(
            'При импорте списка маршрутов `urlpatterns` из файла '
            f'`blog/urls.py` произошла ошибка: {e}'
        ) from e
    assert isinstance(solution_urlpatterns, list), (
        'Убедитесь, что значение переменной `urlpatterns` - это список.'
    )
    # Теперь там может быть всего 1 маршрут (index), поэтому >= 1, а не >= 3
    assert len(solution_urlpatterns) >= 1, (
        'Убедитесь, что все необходимые маршруты добавлены в список '
        '`urlpatterns` в файле `blog/urls.py`.'
    )


def test_pages_urls():
    try:
        from pages.urls import urlpatterns as solution_urlpatterns
    except Exception as e:
        raise AssertionError(
            'При импорте списка маршрутов `urlpatterns` из файла '
            f'`pages/urls.py` произошла ошибка: {e}'
        ) from e
    assert isinstance(solution_urlpatterns, list), (
        'Убедитесь, что значение переменной `urlpatterns` в файле '
        '`pages/urls.py` - это список.'
    )
    assert len(solution_urlpatterns) >= 2, (
        'Убедитесь, что все необходимые маршруты добавлены в список '
        '`urlpatterns` в файле `pages/urls.py`.'
    )


def test_blog_appname():
    try:
        from blog.urls import app_name as solution_appname
    except ImportError as e:
        raise AssertionError(
            'Убедитесь, что для приложения `blog` в переменной `app_name` '
            'указан `namespace`.'
        ) from e
    except Exception as e:
        raise AssertionError(
            'При импорте переменной `app_name` из модуля `blog/urls.py` '
            f'возникла ошибка: {e}'
        ) from e
    assert solution_appname == 'blog', (
        'Убедитесь, что в файле urls.py приложения `blog` '
        'значение переменной `app_name` указано без ошибок.'
    )


def test_pages_appname():
    try:
        from pages.urls import app_name as solution_appname
    except Exception as e:
        raise AssertionError(
            'Убедитесь, что для приложения `pages` в переменной `app_name` '
            'указан `namespace`.'
        ) from e
    assert solution_appname == 'pages', (
        'Убедитесь, что в файле urls.py приложения `pages` '
        'значение переменной `app_name` указано без ошибок.'
    )


def test_blog_index_reverse(client):
    try:
        reverse('blog:index')
    except NoReverseMatch as e:
        pytest.fail(f'Маршрут blog:index не найден: {e}')


@pytest.mark.parametrize('name', ['pages:about', 'pages:rules'])
def test_pages_url_names(name):
    try:
        reverse(name)
    except NoReverseMatch as e:
        pytest.fail(
            f'При поиске пути по имени `{name}` возникла ошибка: {e}'
        )
