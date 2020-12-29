# -*- coding: utf-8 -*-
from django.contrib import admin
from apps.posts.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'rate', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['title']

    def __str__(self):
        return self.title


admin.site.register(Post, PostAdmin)
