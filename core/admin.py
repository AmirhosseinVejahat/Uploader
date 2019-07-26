# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Movie


class ItemAdmin(admin.ModelAdmin):
    list_display = ['topic', 'author', 'duration', 'level']
    sortable_by = ['duration']
    list_filter = ['topic']


admin.site.register(Movie, ItemAdmin)
