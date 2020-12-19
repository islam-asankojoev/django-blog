from django.contrib import admin
from .models import News, Category


# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'published']
    list_display_links = ['title']
    list_editable = ['published']
    list_filter = ['published', 'created_at']
    search_fields = ['id', 'title', 'category']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['title']
    search_fields = ['id', 'title']


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
