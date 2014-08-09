# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function

from django.contrib.sitemaps import Sitemap
from applications.posts.models import Post
from datetime import datetime


class PostSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def __get(self, name, obj, default=None):
        try:
            attr = getattr(self, name)
        except AttributeError:
            return default
        if callable(attr):
            return attr(obj)
        return attr

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return datetime.now()

    def location(self, obj):
        return obj.get_absolute_url()

    def get_urls(self, page=1, site=None, protocol=None):
        urls = []
        for item in self.paginator.page(page).object_list:
            priority = self.__get('priority', item, None)
            url_info = {
                'item':       item,
                'location':   self.__get('location', item),
                'lastmod':    self.__get('lastmod', item, None),
                'changefreq': self.__get('changefreq', item, None),
                'priority':   str(priority if priority is not None else ''),
            }
            urls.append(url_info)
        return urls


sitemaps = {
    "post": PostSitemap
}