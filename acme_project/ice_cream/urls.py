from django.urls import path
from . import views

# Обязательно задаём имя приложения, чтобы работали ссылки вида {% url 'ice_cream:index' %}
app_name = 'ice_cream'

urlpatterns = [
    # Главная страница (index.html)
    path('', views.index, name='index'),
    
    # Каталог мороженого (list.html)
    path('ice_cream/', views.ice_cream_list, name='ice_cream_list'),
    
    # Детальная страница отдельного мороженого (detail.html)
    path('ice_cream/<int:id>/', views.ice_cream_detail, name='ice_cream_detail'),
    
    # О проекте (description.html)
    path('about/', views.about, name='about'),
]
