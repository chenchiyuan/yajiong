# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from bs4 import BeautifulSoup
from django.core.management import BaseCommand
from applications.jiong.models import Post

import requests
import time


headers = {
    "referer": "http://weixin.sogou.com/",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
}


gen_url = lambda query, page: "http://weixin.sogou.com/weixin?query=%s&type=2&page=%s" % (query, page)


class Command(BaseCommand):
    def handle(self, *args, **options):
        pages = range(233, 6000)
        for page in pages:
            url = gen_url(u"笑话", page)
            print(page)
            links = self.parse_url(url)
            for link in links:
                self.create_post(link)
            time.sleep(2)

    def parse_url(self, url):
        content = requests.get(url, headers=headers).content
        soup = BeautifulSoup(content)
        h4s = soup.find_all("h4")
        links = []
        for h4 in h4s:
            tag_a = h4.find("a")
            href = tag_a.attrs.get("href", "")
            content = tag_a.text
            links.append((content, href))
        return links

    def create_post(self, link):
        title, href = link
        if href and Post.objects.filter(url=href).exists():
            return

        Post(title=title, url=href).save()
        print(title)
        print(href)
        print("###")
