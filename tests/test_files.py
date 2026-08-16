import os


def test_project_folder_in_place():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    manage_path = os.path.join(BASE_DIR, "manage.py")

    assert os.path.isfile(manage_path), (
        f"Не найден manage.py. Ожидался по пути: {manage_path}. "
        "Убедитесь, что pytest запускается из корня проекта."
    )
