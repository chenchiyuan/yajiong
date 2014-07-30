# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.db import models
from applications.ueditor.fields import UEditorField


class Category(models.Model):
    class Meta:
        app_label = "jiong"
        db_table = "jiong_category"
        verbose_name_plural = verbose_name = u"分类"
        ordering = ['-priority']

    name = models.CharField(u'名称', max_length=256)
    priority = models.IntegerField(u"优先级", default=0)

    def __unicode__(self):
        return self.name


class Post(models.Model):
    class Meta:
        app_label = "jiong"
        db_table = "jiong_post"
        verbose_name_plural = verbose_name = u"笑话"

    title = models.CharField(u"标题", max_length=256)
    content = UEditorField(u"正文", default="", blank=True, null=True)

    rating = models.IntegerField(u"好笑", default=0, blank=True, null=True)
    created_at = models.DateTimeField(u"创建时间", auto_now=True)

    categories = models.ManyToManyField(Category, verbose_name=u"分类", blank=True, null=True)

    def __unicode__(self):
        return self.title

