from django.shortcuts import render, get_object_or_404
from .models import Post, Category

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk, is_published=True)
    return render(request, 'blog/post_detail.html', {'post': post})

# Если категории пока не нужны — закомментируй эту функцию:
# def category_posts(request, category_slug):
#     category = get_object_or_404(Category, slug=category_slug)
#     posts = Post.objects.filter(category=category)
#     return render(request, 'blog/category_posts.html', {
#         'category': category,
#         'posts': posts,
#     })
