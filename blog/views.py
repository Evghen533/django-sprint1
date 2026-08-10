from django.shortcuts import render, get_object_or_404
from .models import Post, Category


def post_list(request):
    """Страница со списком постов (главная лента)."""
    posts = (
        Post.objects
        .filter(is_published=True)
        .select_related('category')
    )
    return render(request, 'blog/index.html', {'posts': posts})


def post_detail(request, pk):
    """Страница отдельного поста."""
    post = get_object_or_404(Post, pk=pk, is_published=True)
    return render(request, 'blog/post_detail.html', {'post': post})


def category_view(request, slug):
    """Список постов по категории (URL name='category_posts')."""
    category = get_object_or_404(Category, slug=slug)
    posts = (
        Post.objects
        .filter(category=category, is_published=True)
        .select_related('category')
    )
    return render(
        request,
        'blog/category.html',
        {'category': category, 'posts': posts},
    )
