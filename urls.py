from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path(
        'category/<slug:slug>/',
        views.category_posts,
        name='category_posts'
    ),
]
