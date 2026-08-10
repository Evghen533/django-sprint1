import pytest
from django.test import Client
from blog.models import Post, Category
from blog.views import post_list


@pytest.mark.django_db
def test_blog_posts(client):
    assert callable(post_list)

    # Создаём категории
    cat_travel = Category.objects.create(slug="travel", title="Путешествия")
    cat_bad = Category.objects.create(slug="not-my-day", title="Не мой день")

    Post.objects.create(
        title="Корабль потерпел крушение",
        content="Наш корабль, застигнутый в открытом море страшным штормом, потерпел крушение. Весь экипаж, кроме меня, утонул; я же, несчастный Робинзон Крузо, был выброшен полумёртвым на берег этого проклятого острова, который назвал островом Отчаяния",
        date="1659-09-30",
        category=cat_travel,
        is_published=True,
    )
    Post.objects.create(
        title="Проснувшись поутру",
        content="Проснувшись поутру, я увидел, что наш корабль сняло с мели приливом и пригнало гораздо ближе к берегу. Это подало мне надежду, что, когда ветер стихнет, мне удастся добраться до корабля и запастись едой и другими необходимыми вещами.",
        date="1659-10-01",
        category=cat_bad,
        is_published=True,
    )
    Post.objects.create(
        title="Дождь и ветер",
        content="Всю ночь и весь день шёл дождь и дул сильный порывистый ветер. 25 октября. Корабль за ночь разбило в щепки; на том месте, где он стоял, торчат какие‑то жалкие обломки, да и те видны только во время отлива. Весь этот день я хлопотал около вещей: укрывал и укутывал их, чтобы не испортились от дождя.",
        date="1659-10-25",
        category=cat_bad,
        is_published=True,
    )

    response = client.get("/")
    assert response.status_code == 200

    posts = response.context.get("posts")
    assert posts is not None
    assert len(posts) == 3

    for post in posts:
        if post.category:
            assert post.category.slug in ["travel", "not-my-day"]

        assert ("корабль" in post.content) or ("дождь" in post.content)
