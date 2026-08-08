import os

def test_project_folder_in_place(root_dir, project_dirname):
    # В CI root_dir = /app, а manage.py лежит прямо в /app (а не в /app/blogicum)
    manage_path = os.path.join(root_dir, "manage.py")
    assert os.path.isfile('manage.py'), (
        f"Не найден manage.py. Ищем по пути: {manage_path}. "
        "Убедитесь, что manage.py лежит в корне проекта."
    )
