import pytest
from datetime import date
from blog.models import Post, Category

@pytest.fixture(scope="function")
def posts():
    cat_travel = Category.objects.create(name="Путешествия", slug="travel")
    cat_not_my_day = Category.objects.create(name="Не мой день", slug="not-my-day")

    post1 = Post.objects.create(
        title="Крушение корабля",
        slug="wreck",
        content="""Наш корабль, застигнутый в открытом море
                страшным штормом, потерпел крушение.
                Весь экипаж, кроме меня, утонул; я же,
                несчастный Робинзон Крузо, был выброшен
                полумёртвым на берег этого проклятого острова,
                который назвал островом Отчаяния.""",
        date=date(1659, 9, 30),
        location="Остров отчаянья",
        category=cat_travel,
        is_published=True,
    )
    post2 = Post.objects.create(
        title="Пробуждение на мели",
        slug="unstuck",
        content="""Проснувшись поутру, я увидел, что наш корабль сняло
                с мели приливом и пригнало гораздо ближе к берегу.
                Это подало мне надежду, что, когда ветер стихнет,
                мне удастся добраться до корабля и запастись едой и
                другими необходимыми вещами.""",
        date=date(1659, 10, 1),
        location="Остров отчаянья",
        category=cat_not_my_day,
        is_published=True,
    )
    post3 = Post.objects.create(
        title="Дождь и ветер",
        slug="rain-and-wind",
        content="""Всю ночь и весь день шёл дождь и дул сильный
                порывистый ветер. 25 октября. Корабль за ночь разбило
                в щепки. Весь этот день я хлопотал около вещей: укрывал
                и укутывал их, чтобы не испортились от дождя.""",
        date=date(1659, 10, 25),
        location="Остров отчаянья",
        category=cat_not_my_day,
        is_published=True,
    )

    return [post1, post2, post3]
