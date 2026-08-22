import pytest
from django.template import TemplateDoesNotExist
from pathlib import Path
from blog.views import posts as solution_posts


@pytest.fixture()
def settings_app_name():
    return 'blogicum'


@pytest.fixture()
def root_dir():
    return str(Path(__file__).resolve().parent)


@pytest.fixture()
def project_dirname():
    return 'blogicum'


@pytest.fixture()
def posts():
    # Теперь это безопасно: posts точно есть в blog.views
    return solution_posts.copy()
