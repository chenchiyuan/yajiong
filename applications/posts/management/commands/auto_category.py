# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.core.management import BaseCommand
from applications.posts.models import Post, Category


def smart_print(text):
    print(text.encode("utf-8"))


class Command(BaseCommand):
    def handle(self, *args, **options):
        posts = Post.objects.all()
        categories = Category.objects.all()

        for category in categories:
            for post in posts:
                if len(post.content.split(category.name)) > 10:
                    smart_print("%s 归于 %s" % (post.title, category.name))
                    post.categories.add(category)

        #self.auto_rating(posts)

    def auto_rating(self, posts):
        for post in posts:
            rating = int(len(post.content) / 300.0)
            post.rating = rating
            post.save()
            smart_print("%s %d分" % (post.title, post.rating))
