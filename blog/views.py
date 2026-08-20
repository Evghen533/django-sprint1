from django.shortcuts import render


posts = [
    {
        "id": 0,
        "category": "travel",
        "date": "30 сентября 1659 года",
        "location": "Остров отчаянья",
        "title": "День первый",
        "text": (
            "Наш корабль, застигнутый в открытом море страшным штормом, "
            "потерпел крушение. Весь экипаж, кроме меня, утонул; я же, "
            "несчастный Робинзон Крузо, был выброшен полумёртвым на берег "
            "этого проклятого острова, который назвал островом Отчаяния."
        ),
    },
    {
        "id": 1,
        "category": "adventure",
        "date": "1 октября 1659 года",
        "location": "Остров отчаянья",
        "title": "Строю плот",
        "text": (
            "Проснувшись поутру, я увидел, что наш корабль сняло с мели "
            "приливом и пригнало гораздо ближе к берегу. Это подало мне "
            "надежду, что, воспользовавшись приливом, я смогу добыть из "
            "корабля всё необходимое для жизни."
        ),
    },
    {
        "id": 2,
        "category": "not-my-day",
        "date": "25 октября 1659 года",
        "location": "Остров отчаянья",
        "title": "Ураган",
        "text": (
            "Всю ночь и весь день шёл дождь и дул сильный порывистый ветер. "
            "Корабль за ночь разбило в щепки; на том месте, где он стоял, "
            "торчат какие-то жалкие обломки, да и те видны только во время "
            "отлива."
        ),
    },
]



def index(request):
    sorted_posts = sorted(posts, key=lambda p: p["id"], reverse=True)
    return render(request, "blog/index.html", {"posts": sorted_posts})


def post_detail(request, id):
    post = next((p for p in posts if p["id"] == id), None)
    if not post:
        return render(request, "blog/detail.html", {"post": None})
    return render(request, "blog/detail.html", {"post": post})


def category_posts(request, category_slug):
    filtered_posts = [p for p in posts if p["category"] == category_slug]
    sorted_posts = sorted(filtered_posts, key=lambda p: p["id"], reverse=True)
    return render(
        request,
        "blog/category.html",
        {"category_slug": category_slug, "posts": sorted_posts},
    )
