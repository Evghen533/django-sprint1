import os

def test_project_folder_in_place(root_dir, project_dirname):
    project_root = os.path.dirname(root_dir)  # поднимаемся из tests на уровень выше
    manage_fpath = os.path.join(project_root, project_dirname, 'manage.py')
    assert os.path.isfile(manage_fpath), (
        f'Не найден файл `{manage_fpath}`. '
        'Убедитесь, что manage.py лежит в папке blogicum внутри корня проекта.'
    )
