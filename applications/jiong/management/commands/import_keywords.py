# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.core.management import BaseCommand
from applications.jiong.models import Post
from libs.keywords import Keyword


class Command(BaseCommand):
    def handle(self, *args, **options):
        posts = Post.objects.all()
        for post in posts:
            print("%s %s" % (post.id, post.title))
            if not post.keywords:
                keywords = Keyword.get_keywords(post.title)
                post.keywords = ",".join(keywords)
                post.save()
