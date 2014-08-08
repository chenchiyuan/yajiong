# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.core.management import BaseCommand
import requests
from bs4 import BeautifulSoup
from applications.posts.models import Post

import time


def smart_print(text):
    print(text.encode("utf-8"))


class Command(BaseCommand):
    def handle(self, *args, **options):
        posts = list(Post.objects.all())
        for post in posts:
            if post.url and not post.content:
                try:
                    self.parse(post)
                except Exception, err:
                    smart_print(err)
                    continue
                time.sleep(1)

    def parse(self, post):
        smart_print(post.title)
        content = requests.get(post.url).content
        soup = BeautifulSoup(content)
        page_content_tag = soup.find(id="page-content")
        post.content = page_content_tag.extract
        post.save()