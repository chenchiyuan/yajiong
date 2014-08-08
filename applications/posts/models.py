# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.db import models
from applications.ueditor.fields import UEditorField
from applications.weixin.libs.formatters import BasicFormatter
from bs4 import BeautifulSoup
from libs.keywords import Keyword
from applications.posts.const import COMMON_KEYWORDS


class Category(models.Model):
    class Meta:
        app_label = "posts"
        db_table = "posts_category"
        verbose_name_plural = verbose_name = u"分类"
        ordering = ['-priority']

    name = models.CharField(u'名称', max_length=256)
    priority = models.IntegerField(u"优先级", default=0)

    def __unicode__(self):
        return self.name


class Post(models.Model):
    class Meta:
        app_label = "posts"
        db_table = "posts_post"
        verbose_name_plural = verbose_name = u"文章"

    title = models.CharField(u"标题", max_length=256)
    content = UEditorField(u"正文", default="", blank=True, null=True)

    url = models.CharField(u"原链接", max_length=1024, blank=True, null=True, default="")

    rating = models.IntegerField(u"评分", default=0, blank=True, null=True)
    created_at = models.DateTimeField(u"创建时间", auto_now=True)

    categories = models.ManyToManyField(Category, verbose_name=u"分类", blank=True, null=True)
    keywords = models.CharField(u"搜索关键字", max_length=8224, default="", blank=True, null=True)

    def __unicode__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None):
        if self.content:
            try:
                self.content = BasicFormatter.format(self.content)
            except:
                pass
        if not self.keywords:
            try:
                self.keywords = ",".join(Keyword.get_keywords(self.title))
            except:
                pass

        super(Post, self).save(force_insert, force_update, using)

    def get_absolute_url(self):
        return "/posts/%s/" % self.id

    @property
    def glance_content(self):
        soup = BeautifulSoup(self.content)
        return soup.text.strip()[:200]

    def get_absolute_url(self):
        return "/posts/%s/" % self.id

    def get_keywords(self):
        keywords = self.keywords.split(",")
        keywords.extend(COMMON_KEYWORDS)
        keywords.append(self.title)
        return ",".join(list(set(keywords)))