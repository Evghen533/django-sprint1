import pytest
from django.template import TemplateDoesNotExist
from pathlib import Path


@pytest.fixture()
def settings_app_name():
    return 'blogicum'


@pytest.fixture()
def root_dir():
    return str(Path(__file__).resolve().parent)


@pytest.fixture()
def project_dirname():
    return 'blogicum'


@pytest.fixture
def posts(db):
    from blog.models import Post, Category

    cat = Category.objects.create(slug='travel', name='Путешествия')

    return [
        Post.objects.create(
            title='Post 0', text='Text 0', slug='post-0',
            date='2023-01-01', location='Остров', category=cat, content='Content 0'
        ),
        Post.objects.create(
            title='Post 1', text='Text 1', slug='post-1',
            date='2023-01-02', location='Горы', category=cat, content='Content 1'
        ),
        Post.objects.create(
            title='Post 2', text='Text 2', slug='post-2',
            date='2023-01-03', location='Пляж', category=cat, content='Content 2'
        ),
    ]
