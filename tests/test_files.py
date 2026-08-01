import os

def test_project_folder_in_place(root_dir, project_dirname):
    # В CI root_dir = /app, а manage.py лежит прямо в /app (а не в /app/blogicum)
    manage_path = os.path.join(root_dir, "manage.py")
    assert os.path.isfile(manage_path), (
        f"Не найден manage.py. Ищем по пути: {manage_path}. "
        "Убедитесь, что manage.py лежит в корне проекта."
    )

    blog_dir = os.path.join(root_dir, "blog")
    assert os.path.isdir(blog_dir), f"Не найдена папка blog/. Путь: {blog_dir}"

    blog_init = os.path.join(blog_dir, "__init__.py")
    assert os.path.isfile(blog_init), f"Не найден blog/__init__.py по пути: {blog_init}"
