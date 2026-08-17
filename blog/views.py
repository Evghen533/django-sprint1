from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Post, Category

MONTHS = {
    1: "января", 2: "февраля", 3: "марта", 4: "апреля", 5: "мая", 6: "июня",
    7: "июля", 8: "августа", 9: "сентября", 10: "октября", 11: "ноября", 12: "декабря"
}

def blog_posts(request):
    posts = Post.objects.order_by("pk")
    result = []

    for i, post in enumerate(posts):
        month_name = MONTHS.get(post.date.month, "")
        formatted_date = f"{post.date.day} {month_name} {post.date.year} года"

        result.append({
            "id": i,
            "location": "Остров отчаянья",
            "date": formatted_date,
            "category": post.category.slug,
            "text": post.content,
        })

    return JsonResponse({"posts": result})


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
    category = get_object_or_404(Category, slug=category_slug)
    posts = (
        Post.objects.filter(
            is_published=True,
            category=category
        )
        .select_related("category")
    )
    return render(
        request,
        "blog/category.html",
        {"posts": posts, "category": category}
    )
