# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.template import RequestContext
from django.views.generic import TemplateView
from applications.jiong.models import Post


class PostDetailView(TemplateView):
    template_name = "post.html"
    
    def get_context_data(self, **kwargs):
        post = Post.objects.get(**kwargs)
        context = RequestContext(self.request, {"post": post})
        return context
