from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('category', 'date', 'location')
    search_fields = ('text', 'location', 'category')
