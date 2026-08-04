#!/usr/bin/env python
import os
import sys
from pathlib import Path

def main():
    # Получаем абсолютный путь к папке, где лежит manage.py (это корень проекта)
    BASE_DIR = Path(__file__).resolve().parent

    # Добавляем эту папку в sys.path, чтобы Python мог импортировать пакеты из неё
    if str(BASE_DIR) not in sys.path:
        sys.path.insert(0, str(BASE_DIR))
        print("project_root:", project_root)
        print("sys.path:", sys.path)

    # Указываем Django, какой именно settings использовать
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogicum.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
