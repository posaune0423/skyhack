# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class UserAdmin(UserAdmin):
    list_display = ('username', 'email', 'date_joined', 'thumbnail')
    list_filter = ['date_joined']
    search_fields = ['username']


admin.site.register(User, UserAdmin)
