import os


def test_project_folder_in_place(root_dir, project_dirname):
    manage_path = os.path.join(root_dir, "manage.py")
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # папка tests
    assert os.path.isfile(os.path.join(BASE_DIR, 'manage.py'))
