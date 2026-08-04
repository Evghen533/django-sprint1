import pytest
from django.urls import reverse, NoReverseMatch

# Тесты для приложения blog (с неймспейсом)
@pytest.mark.parametrize("name, args", [
    ("blog:post_list", []),
    ("blog:post_detail", [1]),  # ID поста — будет подставлен в тестах с БД
])
def test_blog_url_names(name, args):
    try:
        reverse(name, args=args)
    except NoReverseMatch as e:
        raise AssertionError(
            f"URL с именем '{name}' не найден. Проверьте urls.py и app_name='blog'. Ошибка: {e}"
        ) from e
    except Exception as e:
        raise AssertionError(f"При проверке URL '{name}' возникла ошибка: {e}") from e
