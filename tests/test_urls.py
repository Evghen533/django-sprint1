from django.urls import reverse, NoReverseMatch
import pytest


@pytest.mark.parametrize(
    "name, args",
    [
        ("blog:index", []),
        ("blog:post_detail", [1]),
    ],
)
def test_blog_url_names(name, args):
    try:
        reverse(name, args=args)
    except NoReverseMatch as e:
        raise AssertionError(
            f"URL с именем '{name}' не найден. Проверьте urls.py "
            f"и app_name='blog'. Ошибка: {e}"
        ) from e
    except Exception as e:
        raise AssertionError(f"При проверке URL '{name}' возникла ошибка: {e}") from e
