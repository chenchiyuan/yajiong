# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function

from django.contrib.sitemaps import Sitemap
from applications.posts.models import Post
from datetime import datetime


class PostSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return datetime.now()


sitemaps = {
    "post": PostSitemap
}