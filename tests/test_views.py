import pytest
from django.urls import reverse
from django.utils import timezone
from datetime import datetime
from blog.models import Category, Post


@pytest.mark.django_db
def test_blog_posts(try_get_url):
    cat_travel, _ = Category.objects.get_or_create(
        slug="travel", defaults={"name": "Путешествия"}
    )
    cat_bad, _ = Category.objects.get_or_create(
        slug="not-my-day", defaults={"name": "Не мой день"}
    )

    Post.objects.get_or_create(
        title="Корабль потерпел крушение",
        content=(
            "Наш корабль, застигнутый в открытом море страшным штормом, "
            "потерпел крушение. Весь экипаж, кроме меня, утонул; я же, "
            "несчастный Робинзон Крузо, был выброшен полумёртвым на берег "
            " этого проклятого острова, который назвал островом Отчаяния."
        ),
        created_at=timezone.make_aware(datetime(1659, 9, 30)),
        category=cat_travel,
        is_published=True,
    )

    Post.objects.get_or_create(
        title="Проснувшись поутру",
        content=(
            "Проснувшись поутру, я увидел, что наш корабль "
            "сняло с мели приливом и пригнало гораздо ближе к берегу. "
            "Это подало мне надежду, что, когда ветер стихнет, "
            "мне удастся добраться до корабля и "
            "запастись едой и другими необходимыми вещами."
        ),
        created_at=timezone.make_aware(datetime(1659, 10, 1)),
        category=cat_bad,
        is_published=True,
    )

    Post.objects.get_or_create(
        title="Дождь и ветер",
        content=(
            "Всю ночь и весь день шёл дождь и дул сильный порывистый ветер. "
            "25 октября. Корабль за ночь разбило в щепки; на том месте, "
            "где он стоял, торчат какие‑то жалкие обломки, да и те видны "
            "только во время отлива. Весь этот день я хлопотал около вещей: "
            "укрывал и укутывал их, чтобы не испортились от дождя."
        ),
        created_at=timezone.make_aware(datetime(1659, 10, 25)),
        category=cat_bad,
        is_published=True,
    )

    url = reverse("blog:post_list")
    response = try_get_url(url)

    assert response.status_code == 200

    posts = response.context.get("posts")
    assert posts is not None
    assert len(posts) >= 3

    for post in posts:
        if post.category:
            assert post.category.slug in ["travel", "not-my-day"]
        assert ("корабль" in post.content) or ("дождь" in post.content)
