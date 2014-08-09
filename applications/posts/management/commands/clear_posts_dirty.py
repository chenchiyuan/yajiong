# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.core.management import BaseCommand
from applications.posts.models import Post


class Command(BaseCommand):
    def handle(self, *args, **options):
        keyword = args[0].decode("utf-8")
        posts = Post.objects.all()
        delete_ids = []

        for post in posts:
            if keyword in post.title:
                continue

            if len(post.content.split(keyword)) > 5:
                continue
            print(post.title)
            delete_ids.append(post.id)
        print(delete_ids)
        Post.objects.filter(id__in=delete_ids).delete()