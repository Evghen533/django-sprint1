from django.shortcuts import render
from django.http import Http404

posts = [
    {
        "id": 0,
        "location": "Остров отчаянья",
        "date": "30 сентября 1659 года",
        "category": "travel",
        "text": "Наш корабль, застигнутый в открытом море\nстрашным штормом, потерпел крушение.\nВесь экипаж, кроме меня, утонул; я же,\nнесчастный Робинзон Крузо, был выброшен\nполумёртвым на берег этого проклятого острова,\nкоторый назвал островом Отчаяния."
    },
    {
        "id": 1,
        "location": "Остров отчаянья",
        "date": "1 октября 1659 года",
        "category": "not-my-day",
        "text": "Проснувшись поутру, я увидел, что наш корабль сняло\nс мели приливом и пригнало гораздо ближе к берегу.\nЭто подало мне надежду, что, когда ветер стихнет,\nмне удастся добраться до корабля и запастись едой и\nдругими необходимыми вещами. Я немного приободрился,\nхотя печаль о погибших товарищах не покидала меня.\nМне всё думалось, что, останься мы на корабле, мы\nнепременно спаслись бы. Теперь из его обломков мы могли бы\nпостроить баркас, на котором и выбрались бы из этого\nгиблого места."
    },
    {
        "id": 2,
        "location": "Остров отчаянья",
        "date": "25 октября 1659 года",
        "category": "not-my-day",
        "text": "Всю ночь и весь день шёл дождь и дул сильный\nпорывистый ветер. 25 октября. Корабль за ночь разбило\nв щепки; на том месте, где он стоял, торчат какие-то\nжалкие обломки, да и те видны только во время отлива.\nВесь этот день я хлопотал около вещей: укрывал и\nукутывал их, чтобы не испортились от дождя."
    }
]


def index(request):
    inverted_posts = posts[::-1]
    return render(request, 'blog/index.html', {'posts': inverted_posts})


def post_detail(request, id):
    post = next((p for p in posts if p['id'] == id), None)
    if not post:
        raise Http404("Пост не найден")
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    filtered_posts = [p for p in posts if p['category'] == category_slug]
    filtered_posts.sort(key=lambda x: x['id'], reverse=True)
    return render(request, 'blog/category.html', {
        'category_slug': category_slug,
        'posts': filtered_posts
    })
