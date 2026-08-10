# blog/urls.py
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # главная страница со списком постов
    path('', views.post_list, name='post_list'),
    # страница отдельного поста
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    # страница категории
    path(
        'category/<slug:slug>/',
        views.category_view,
        name='category_posts',
    ),
]
