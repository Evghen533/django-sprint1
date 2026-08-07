from django.shortcuts import render, get_object_or_404
from .models import Post, Category


def post_list(request):
    posts = Post.objects.filter(is_published=True).order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    posts = (
        Post.objects
        .filter(category=category, is_published=True)
        .order_by('-created_at')
    )
    return render(
        request,
        'blog/category.html',
        {'category': category, 'posts': posts},
    )
