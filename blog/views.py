from django.shortcuts import render

posts = [
    {
        "id": 0,
        "location": "Остров отчаянья",
        "date": "30 сентября 1659 года",
        "category": "travel",
        "text": "Наш корабль, застигнутый в открытом море страшным штормом, потерпел крушение. Весь экипаж, кроме меня, утонул; я же, несчастный Робинзон Крузо, был выброшен полумёртвым на берег этого проклятого острова, который назвал островом Отчаяния."
    },
    {
        "id": 1,
        "location": "Остров отчаянья",
        "date": "1 октября 1659 года",
        "category": "not-my-day",
        "text": "Проснувшись поутру, я увидел, что наш корабль сняло с мели приливом и пригнало гораздо ближе к берегу. Это подало мне надежду, что, когда ветер стихнет, мне удастся добраться до корабля и запастись едой и другими необходимыми вещами."
    },
    {
        "id": 2,
        "location": "Остров отчаянья",
        "date": "25 октября 1659 года",
        "category": "not-my-day",
        "text": "Всю ночь и весь день шёл дождь и дул сильный порывистый ветер. 25 октября. Корабль за ночь разбило в щепки; на том месте, где он стоял, торчат какие‑то жалкие обломки, да и те видны только во время отлива. Весь этот день я хлопотал около вещей: укрывал и укутывал их, чтобы не испортились от дождя."
    }
]

def index(request):
    return render(request, "blog/index.html", {"posts": posts})

def post_detail(request, pk):
    post = posts[pk]
    return render(request, "blog/detail.html", {"post": post})

def category_posts(request, slug):
    filtered_posts = [p for p in posts if p["category"] == slug]
    return render(request, "blog/category.html", {"posts": filtered_posts, "slug": slug})
