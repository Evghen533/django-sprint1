from django.shortcuts import render, get_object_or_404
from .models import Post

posts = [
    {
        "id": 1,
        "title": "Крушение корабля",
        "date": "30 сентября 1659 года",
        "location": "Остров отчаяния",
        "category": "travel",
        "category_title": "Путешествия",
        "text": """Наш корабль, застигнутый в открытом море
                страшным штормом, потерпел крушение.
                Весь экипаж, кроме меня, утонул; я же,
                несчастный Робинзон Крузо, был выброшен
                полумёртвым на берег этого проклятого острова,
                который назвал островом Отчаяния.""",
    },
    {
        "id": 2,
        "title": "Пробуждение на мели",
        "date": "1 октября 1659 года",
        "location": "Остров отчаяния",
        "category": "not-my-day",
        "category_title": "Не мой день",
        "text": """Проснувшись поутру, я увидел, что наш корабль сняло
                с мели приливом и пригнало гораздо ближе к берегу.
                Это подало мне надежду, что, когда ветер стихнет,
                мне удастся добраться до корабля и запастись едой и
                другими необходимыми вещами. Я немного приободрился,
                хотя печаль о погибших товарищах не покидала меня.
                Мне всё думалось, что, останься мы на корабле, мы
                непременно спаслись бы. Теперь из его обломков мы могли бы
                построить баркас, на котором и выбрались бы из этого
                гиблого места.""",
    },
    {
        "id": 3,
        "title": "Дождь и ветер",
        "date": "25 октября 1659 года",
        "location": "Остров отчаяния",
        "category": "not-my-day",
        "category_title": "Не мой день",
        "text": """Всю ночь и весь день шёл дождь и дул сильный
                порывистый ветер. 25 октября.  Корабль за ночь разбило
                в щепки; на том месте, где он стоял, торчат какие-то
                жалкие обломки,  да и те видны только во время отлива.
                Весь этот день я хлопотал  около вещей: укрывал и
                укутывал их, чтобы не испортились от дождя.""",
    },
]


def index(request):
    posts = Post.objects.filter(is_published=True).select_related("category")
    return render(request, "blog/index.html", {"posts": posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk, is_published=True)

    previous_post = (
        Post.objects.filter(is_published=True, pk__lt=post.pk)
        .order_by("-pk")
        .first()
    )

    next_post = (
        Post.objects.filter(is_published=True, pk__gt=post.pk)
        .order_by("pk")
        .first()
    )

    context = {
        "post": post,
        "previous_post": previous_post,
        "next_post": next_post,
    }
    return render(request, "blog/post_detail.html", context)


def category_posts(request, category_slug):
    posts = (
        Post.objects.filter(
            is_published=True,
            category__slug=category_slug
        )
        .select_related("category")
    )
    return render(
        request,
        "blog/category_posts.html",
        {"posts": posts, "category_slug": category_slug}
    )
