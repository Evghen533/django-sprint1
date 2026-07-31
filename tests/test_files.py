import os
import pytest

def test_project_folder_in_place(root_dir, project_dirname):
    # manage.py лежит в корне проекта, а не внутри blogicum/
    manage_rpath = "manage.py"
    manage_fpath = os.path.join(root_dir, manage_rpath)
    assert os.path.isfile(manage_fpath), (
        f"Не найден файл `{manage_rpath}` в корне проекта. "
        "Убедитесь, что manage.py находится рядом с папкой приложения (blog/)."
    )

    # Дополнительно проверим, что приложение blog действительно существует
    assert os.path.isdir(os.path.join(root_dir, "blog")), "Не найдена папка приложения `blog/`"
    assert os.path.isfile(os.path.join(root_dir, "blog", "__init__.py")), "Не найден blog/__init__.py"
