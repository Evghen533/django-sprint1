import os


def test_project_folder_in_place(root_dir, project_dirname):
    project_root = os.path.dirname(root_dir)  # это C:\Dev\django-sprint1
    manage_fpath = os.path.join(project_root, 'manage.py')
    assert os.path.isfile(manage_fpath), (
        f'Не найден файл `{manage_fpath}`. '
        'Убедитесь, что manage.py лежит в корне проекта.'
    )
