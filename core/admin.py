# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import *
from datetime import date

class YearListFilter(admin.SimpleListFilter):
    title =  'year created'
    parameter_name = 'year'

    def lookups(self, request, model_admin):
        return (
            ('2015','2015'),
            ('2016','2016'),

        )
    def queryset(self, request, queryset):
        if self.value() == '2015':
            return queryset.filter(created_at__gte=date(2015,1,1),
                                   created_at__lte=date(2015,12,31))
        if self.value() == '2016':
            return queryset.filter(created_at__gte=date(2016,1,1),
                                   created_at__lte=date(2016,12,31))



class CourseAdmin(admin.ModelAdmin):
    list_display = ['topic', 'author', 'duration', 'level']
    fields = ['topic', 'author', 'video', 'duration', 'level', 'description']
    search_fields = ['topic','author']
    sortable_by = ['duration']
    list_filter = ['topic',YearListFilter]
    list_editable = ['author']



class TopicsAdmin(admin.ModelAdmin):
    list_display = ['name']
    #list_filter = ['created_at','is_alive']


admin.site.register(Course, CourseAdmin,)
admin.site.register(Topics,TopicsAdmin)
admin.site.register(Token)