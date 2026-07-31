import os
import pytest


def test_project_folder_in_place(root_dir, project_dirname):
    # Проверяем, что manage.py лежит в корне проекта
    manage_path = os.path.join(root_dir, "manage.py")
    assert os.path.isfile(manage_path), (
        f"Не найден файл `manage.py` в корне проекта. "
        "Убедитесь, что manage.py находится рядом с папкой приложения (blog/)."
    )

    # Проверяем, что приложение blog действительно существует
    blog_dir = os.path.join(root_dir, "blog")
    assert os.path.isdir(blog_dir), f"Не найдена папка приложения `blog/`. Текущая папка: {root_dir}"

    blog_init = os.path.join(blog_dir, "__init__.py")
    assert os.path.isfile(blog_init), f"Не найден файл `blog/__init__.py`"
