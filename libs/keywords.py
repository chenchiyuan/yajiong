# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
import requests
import re
import json
headers = {
    "referer": "http://www.baidu.com/",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
}


class Keyword(object):
    @classmethod
    def get_keywords(cls, keyword):
        pattern = "s:(\[.*\])"
        url = u"http://suggestion.baidu.com/su?wd=%s&cb=" % keyword

        try:
            data = requests.get(url, headers=headers).content.decode("gbk")
            keywords = re.search(pattern, data).group(1)
            json_keyword = json.loads(keywords)
            return json_keyword
        except:
            return []