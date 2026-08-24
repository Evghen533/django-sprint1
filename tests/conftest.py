import pytest
from blog.models import Category, Post
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
def categories(db):
    cat_travel = Category.objects.create(slug='travel', name='Путешествия')
    cat_adventure = Category.objects.create(slug='adventure', name='Приключения')
    cat_city = Category.objects.create(slug='city', name='Город')
    return [cat_travel, cat_adventure, cat_city]

@pytest.fixture
def posts(db, categories):
    return [
        Post.objects.create(
            title='Post 0',
            text='Text 0',
            slug='post-0',
            location='Остров',
            category=categories[0],
        ),
        Post.objects.create(
            title='Post 1',
            text='Text 1',
            slug='post-1',
            location='Горы',
            category=categories[1],
        ),
        Post.objects.create(
            title='Post 2',
            text='Text 2',
            slug='post-2',
            location='Пляж',
            category=categories[2],
        ),
    ]
