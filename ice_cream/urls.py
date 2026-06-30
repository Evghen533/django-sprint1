from django.urls import path
from . import views

app_name = 'ice_cream'

urlpatterns = [
    path('', views.index, name='index'),
    path('ice_cream/', views.ice_cream_list, name='ice_cream_list'),
    path('ice_cream/<int:id>/', views.ice_cream_detail, name='ice_cream_detail'),
    path('about/', views.about, name='about'),
]
