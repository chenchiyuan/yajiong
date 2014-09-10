# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.core.management import BaseCommand
from bs4 import BeautifulSoup
import requests
import json
from applications.posts.models import Post


headers = {
    "referer": "http://haha.sogou.com/",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
}


class Command(BaseCommand):
    def handle(self, *args, **options):
        start, end = args
        for i in range(int(start), int(end)):
            print(i)
            try:
                self.parse_url(index=i)
            except:
                print("error %s" % i)
                continue

    def parse_url(self, index):
        # http://haha.sogou.com/main/content/17243
        url = "http://haha.sogou.com/main/content/%s" % index
        content = requests.get(url, headers=headers).content
        json_data = json.loads(content)

        item = json_data['data'][0]
        if not item['id'] == unicode(index):
            return

        title = item['title']
        print(title)
        content = item['text']
        Post(title=title, content=content, url=url, source_data=json.dumps(json_data)).save()