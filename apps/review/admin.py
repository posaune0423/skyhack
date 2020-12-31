# -*- coding: utf-8 -*-
from django.contrib import admin
from apps.review.models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'rate', 'created_at')
    list_filter = ['created_at']
    search_fields = ['title']

    def __str__(self):
        return self.title


admin.site.register(Review, ReviewAdmin)
