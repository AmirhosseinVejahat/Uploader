# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from . import models

from datetime import date

def make_published(modeladmin,request,queryset):
    queryset.update(status='i')


make_published.short_description = "Mark as Published"


class YearListFilter(admin.SimpleListFilter):
    title = 'year created'
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
    list_display = ['topic', 'author', 'duration', 'level', 'status']
    fields = ['topic', 'author', 'video', 'duration', 'level', 'description']
    search_fields = ['topic', 'author']
    sortable_by = ['duration']
    list_filter = ['topic', YearListFilter]
    list_editable = ['status']
    actions = [make_published]


class TopicsAdmin(admin.ModelAdmin):
    list_display = ['name']


class TokenAdmin(admin.ModelAdmin):
    list_display = ['user', 'token']


admin.site.register(models.Course, CourseAdmin)
admin.site.register(models.Topics, TopicsAdmin)
admin.site.register(models.Token, TokenAdmin)