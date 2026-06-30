from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Подключение встроенной админки Django
    path('admin/', admin.site.urls),
    
    # Главное подключение: перенаправляем все запросы в приложение ice_cream
    path('', include('ice_cream.urls')),
]
