# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.conf.urls import patterns, url
from applications.jiong import const
from applications.jiong.views import PostDetailView, PostListView

urlpatterns = patterns('',
    url(r'^posts/$', PostListView.as_view(), name="post_list_view"),
    url(r'^posts/%s/$' % const.URL_ID, PostDetailView.as_view(), name="post_detail_view"),
)
