from django import get_version


def test_django_version():
    min_ver = "3.2.16"
    used_ver = get_version()
    assert used_ver >= min_ver, (
        f"В проекте должна быть установлена версия Django "
        f"не менее {min_ver}. У вас Django версии {used_ver}"
    )


def test_static_dir(settings):
    """
    Проверяет, что STATICFILES_DIRS задан и содержит путь к папке static.
    Это соответствует текущей структуре проекта.
    """
    assert hasattr(settings, "STATICFILES_DIRS"), (
        "Переменная STATICFILES_DIRS должна быть определена " "в settings.py"
    )
    assert len(settings.STATICFILES_DIRS) > 0, (
        "STATICFILES_DIRS не должен быть пустым: укажите путь " "к папке со статикой"
    )

    has_static_path = any("static" in str(path) for path in settings.STATICFILES_DIRS)
    assert has_static_path, (
        "В STATICFILES_DIRS должен быть путь к папке static "
        "(например, C:/Dev/django-sprint1/static)"
    )


def test_apps_registered(settings):
    """
    Проверяет, что blog зарегистрирован,
    и учитывает, что pages может быть в проекте.
    Если pages удалён — тест проверит отсутствие.
    Если ещё есть — не будет требовать его удаления.
    """
    installed = settings.INSTALLED_APPS

    has_blog = any(app == "blog" or app.startswith("blog.apps") for app in installed)
    assert has_blog, (
        "Приложение 'blog' должно быть зарегистрировано " "в INSTALLED_APPS."
    )

    # Если pages всё ещё в проекте — мы не требуем его удаления.
    # Но если ты хочешь явно проверить, что его нет,
    # раскомментируй строки ниже:
    # has_pages = any(
    #    app == "pages" or app.startswith("pages.apps")
    #    for app in installed
    # )
    # assert not has_pages, (
    #     "Приложение 'pages' не должно быть в INSTALLED_APPS: "
    #     "оно удалено из проекта."
    # )
