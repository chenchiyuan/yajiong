# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.conf.urls import patterns, url
from applications.posts import const
from applications.posts.views import PostDetailView, PostListView, CategoryListView, SearchView

urlpatterns = patterns('',
    url(r'^$', PostListView.as_view(), name="home_view"),
    url(r'^search/$', SearchView.as_view(), name="search_view"),
    url(r'^categories/%s/$' %const.URL_ID, CategoryListView.as_view(), name="category_list_view"),
    url(r'^posts/$', PostListView.as_view(), name="post_list_view"),
    url(r'^posts/%s/$' % const.URL_ID, PostDetailView.as_view(), name="post_detail_view"),
)
