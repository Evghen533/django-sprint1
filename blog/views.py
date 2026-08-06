from django.shortcuts import get_object_or_404, render

from .models import Category, Post


def post_list(request):
    posts = Post.objects.all()
    return render(request, "blog/post_list.html", {"posts": posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk, is_published=True)
    return render(request, "blog/post_detail.html", {"post": post})
