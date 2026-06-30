from django.urls import path
# Обязательно проверьте наличие этой строки (с точкой перед import):
from . import views 

app_name = 'pages'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]
