# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.core.management import BaseCommand
from applications.posts.models import Post


class Command(BaseCommand):
    def handle(self, *args, **options):
        posts = Post.objects.all()
        delete_ids = []
        for post in posts:
            print(post.title)
            if post.title < 4:
                continue
            check_posts = Post.objects.filter(title=post.title).order_by('-rating')
            dirty_ids = check_posts[1:].values_list("id", flat=True)
            delete_ids.extend(dirty_ids)
        Post.objects.filter(id__in=list(set(delete_ids))).delete()