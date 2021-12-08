from django.contrib import admin
from .models import Blog, CommentOfPost


class BlogAdmin(admin.ModelAdmin):
    list_display_links = ['title']
    list_display = ['title', 'status', 'post_view', 'image', 'author']
    search_fields = ['title']
    list_filter = ['status']
    prepopulated_fields = {'slug': ('title',)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ('owner', 'id')


admin.site.register(Blog, BlogAdmin)
admin.site.register(CommentOfPost, CommentAdmin)
