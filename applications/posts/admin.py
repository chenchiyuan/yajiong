# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.contrib import admin
from applications.posts.models import Post, Category


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'rating', 'created_at', "keywords"]
    search_fields = ['title']

    filter_horizontal = ['categories']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'priority', "show", "link"]


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)