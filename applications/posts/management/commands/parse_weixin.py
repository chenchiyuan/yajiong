# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.core.management import BaseCommand
import requests
from bs4 import BeautifulSoup
from applications.posts.models import Post

import time


headers = {
    "referer": "http://weixin.sogou.com/",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
}


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
                    smart_print(err.message)
                    continue
                time.sleep(0.2)

    def parse(self, post):
        smart_print(post.title)
        content = requests.get(post.url, headers=headers).content
        soup = BeautifulSoup(content)
        page_content_tag = soup.find(id="page-content")
        post.content = page_content_tag.extract
        post.save()