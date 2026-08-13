from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Post, Category


def post_list(request):
    posts = Post.objects.filter(is_published=True).order_by('-published_at')
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})


def category_posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.all()
    return render(
        request,
        "blog/category.html",
        {
            "category": category,
            "posts": posts,
        },
    )
