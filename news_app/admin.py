from django.contrib import admin
from .models import News, Category


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug','publish_time','status']
    list_filter = ["category", 'publish_time', 'status']
    prepopulated_fields = {"slug":('title',)}
    date_hierarchy = 'publish_time'
    ordering = ['status','publish_time']
    search_fields = ['title', 'body']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']