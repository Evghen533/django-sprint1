# pages/urls.py
from django.urls import path
from blog.views import about, rules, category_view

app_name = 'pages'

urlpatterns = [
    path('about/', about, name='about'),
    path('rules/', rules, name='rules'),
    path('category/<slug:slug>/', category_view, name='category'),
]
