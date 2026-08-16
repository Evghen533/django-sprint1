import os


def test_project_folder_in_place():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    manage_path_root = os.path.join(BASE_DIR, "manage.py")
    manage_path_blogicum = os.path.join(BASE_DIR, "blogicum", "manage.py")

    assert os.path.isfile(manage_path_root) or os.path.isfile(manage_path_blogicum), (
        f"Не найден manage.py. Проверяли: {manage_path_root}, "
        f"{manage_path_blogicum}"
    )
