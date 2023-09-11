from django.contrib import admin
from .models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'views')
    list_filter = ('pub_date',)
    search_fields = ('title', 'content')
