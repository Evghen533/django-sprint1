import pytest
from blog.models import Post
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
def categories():
    return [
        {"name": "Путешествия", "slug": "travel"},
        {"name": "Приключения", "slug": "adventure"},
        {"name": "Город", "slug": "city"},
    ]


@pytest.fixture
def posts(db, categories):
    travel, adventure, city = categories
    p1 = Post.objects.create(
        title='Крушение корабля',
        text='Наш корабль, застигнутый в открытом море '
        'страшным штормом, потерпел крушение. '
        'Весь экипаж, кроме меня, утонул; я же, '
        'несчастный Робинзон Крузо, был выброшен '
        'полумёртвым на берег этого проклятого острова, '
        'который назвал островом Отчаяния.',
        location='Остров отчаянья',
        category=travel,
        slug='crash-of-the-ship',
    )
    p2 = Post.objects.create(
        title='Надежда на спасение',
        text='Проснувшись поутру, я увидел, что наш корабль сняло '
        'с мели приливом и пригнало гораздо ближе к берегу. '
        'Это подало мне надежду, что, когда ветер стихнет, '
        'мне удастся добраться до корабля и запастись едой и '
        'другими необходимыми вещами. Я немного приободрился, '
        'хотя печаль о погибших товарищах не покидала меня. '
        'Мне всё думалось, что, останься мы на корабле, мы '
        'непременно спаслись бы. Теперь из его обломков мы могли бы '
        'построить баркас, на котором и выбрались бы из этого '
        'гиблого места.',
        location='Остров отчаянья',
        category=adventure,
        slug='hope-for-rescue',
    )
    p3 = Post.objects.create(
        title='Дождь и ветер',
        text='Всю ночь и весь день шёл дождь и дул сильный '
        'порывистый ветер. 25 октября. Корабль за ночь разбило '
        'в щепки; на том месте, где он стоял, торчат какие-то '
        'жалкие обломки, да и те видны только во время отлива. '
        'Весь этот день я хлопотал около вещей: укрывал и '
        'укутывал их, чтобы не испортились от дождя.',
        location='Остров отчаянья',
        category=city,
        slug='rain-and-wind',
    )

    return [p1, p2, p3]
