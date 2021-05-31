from .models import Post
from django.contrib import admin

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    """description"""
    list_display = ('id', 'title', 'created_at')
    list_display_links = ('id', 'title')


admin.site.register(Post, PostAdmin)
