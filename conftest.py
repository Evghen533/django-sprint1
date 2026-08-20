import pytest
from django.template import TemplateDoesNotExist
from pathlib import Path
from blog.views import posts as solution_posts


@pytest.fixture()
def urlpatterns(imports_by_full_name):
    urlpattern_paths = [
        'pages.urls.urlpatterns',
        'blog.urls.urlpatterns'
    ]
    urlpattern_vals = [imports_by_full_name[p] for p in urlpattern_paths]
    expected_names = [
        ('about', 'rules'),
        ('index', 'post_detail', 'category_posts'),
    ]
    expected_views = [
        ('pages.views.about', 'pages.views.rules'),
        ('blog.views.index', 'blog.views.post_detail',
         'blog.views.category_posts'),
    ]
    return zip(
        urlpattern_paths,
        urlpattern_vals,
        expected_names,
        expected_views
    )


@pytest.fixture()
def settings_app_name():
    return 'blogicum'


@pytest.fixture()
def root_dir():
    return str(Path(__file__).resolve().parent)


@pytest.fixture()
def project_dirname():
    return 'blogicum'


@pytest.fixture()
def posts():
    return solution_posts.copy()


def try_get_url(client, url: str):
    try:
        response = client.get(url)
    except TemplateDoesNotExist as e:
        raise AssertionError(
            f'При загрузке страницы по адресу `{url}` возникла ошибка. '
            'Убедитесь, что указанный для страницы шаблон существует '
            'и находится в правильной директории.'
        ) from e
    except TypeError as e:
        raise AssertionError(
            f'При загрузке страницы по адресу `{url}` '
            'возникла ошибка TypeError. '
            'Убедитесь, что используете Path Converter '
            'для приведения параметра строки запроса к нужному типу.'
        ) from e
    except Exception as e:
        raise AssertionError(
            f'При попытке загрузки страницы по адресу `{url}` '
            f'возникла ошибка: {e}'
        ) from e
    else:
        if response.status_code < 300:
            return response
        raise AssertionError(
            f'При попытке загрузки страницы по адресу `{url}` '
            f'возникла ошибка: {response}'
        )
