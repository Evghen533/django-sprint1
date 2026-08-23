from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from .models import Post

def index(request):
    posts = Post.objects.all()
    return TemplateResponse(request, "index.html", {"posts": posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return TemplateResponse(request, "detail.html", {"post": post})

def category_posts(request, category_slug):
    posts = Post.objects.filter(category__slug=category_slug)
    return TemplateResponse(
        request,
        "category.html",
        {"posts": posts, "category_slug": category_slug}
    )
