import os


def test_project_folder_in_place():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(BASE_DIR, "manage.py")
    assert os.path.isfile(path), f"Не найден файл manage.py в корне проекта: {path}"
