# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import *


class ItemAdmin(admin.ModelAdmin):
    list_display = ['topic', 'author', 'duration', 'level']
    sortable_by = ['duration']
    list_filter = ['topic']


class TopicsAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Course, ItemAdmin)
admin.site.register(Topics,TopicsAdmin)