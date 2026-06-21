from django.shortcuts import render

posts = []

def index(request):
    return render(request, 'blog/index.html', {'post': posts})

def post_detail(request, id):
    return render(request, 'blog/detail.html')

def category_posts(request, category_slug):
    return render(request, 'blog/category.html')
