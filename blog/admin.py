from django.contrib import admin
from .models import Post, Category, Tag

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')

class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'author')
    search_fields = ('title', 'text')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
