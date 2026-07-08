from django.shortcuts import render
from django.http import Http404

text = (
    "Наш корабль, застигнутый в открытом море страшным штормом, "
    "потерпел крушение. Весь экипаж, кроме меня, утонул; я же, "
    "несчастный Робинзон Крузо, был выброшен полумёртвым на берег "
    "этого проклятого острова, который назвал островом Отчаяния."
)
    {
        'id': 1,
        'location': 'Остров отчаянья',
        'date': '1 октября 1659 года',
        'category': 'not-my-day',
        'text': (
            'Проснувшись поутру, я увидел, что наш корабль сняло с мели приливом и пригнало гораздо ближе к берегу.\n'
            'Это подало мне надежду, что, когда ветер стихнет, мне удастся добраться до корабля и запастись едой и другими необходимыми вещами.'
        ),
    },
    {
        'id': 2,
        'location': 'Остров отчаянья',
        'date': '25 октября 1659 года',
        'category': 'not-my-day',
        'text': (
            'Всю ночь и весь день шёл дождь и дул сильный порывистый ветер. 25 октября. Корабль за ночь разбило в щепки; на том месте, где он стоял, торчат какие‑то жалкие обломки, да и те видны только во время отлива.\n'
            'Весь этот день я хлопотал около вещей: укрывал и укутывал их, чтобы не испортились от дождя.'
        ),
    },
]

def post_list(request):
    # Тест требует инвертированный список постов
    return render(request, 'blog/index.html', {'posts': posts[::-1]})

def post_detail(request, post_id):
    post = next((p for p in posts if p['id'] == post_id), None)
    if post is None:
        raise Http404("Пост не найден")
    return render(request, 'blog/detail.html', {'post': post})

def category_posts(request, category_slug):
    filtered = [p for p in posts if p['category'] == category_slug]
    return render(request, 'blog/category.html', {'posts': filtered, 'category_slug': category_slug})
