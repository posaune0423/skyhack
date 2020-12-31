# -*- coding: utf-8 -*-
from django.contrib import admin
from apps.airport.models import Airport


class AirportAdmin(admin.ModelAdmin):
    list_display = ('title', 'country', 'rate', 'created_at')
    list_filter = ['country']
    search_fields = ['title']

    def __str__(self):
        return self.title


admin.site.register(Airport, AirportAdmin)
