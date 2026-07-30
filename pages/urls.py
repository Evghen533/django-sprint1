from django.urls import path
from . import views

app_name = "pages"  # Переменная app_name обязательна!

urlpatterns = [
    path("about/", views.about, name="about"),
    path("rules/", views.rules, name="rules"),
]
