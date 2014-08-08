# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.template import RequestContext
from django.views.generic import TemplateView
from applications.posts.models import Post
from libs.pagination import DiggPaginator


class PostDetailView(TemplateView):
    template_name = "post.html"
    
    def get_context_data(self, **kwargs):
        post = Post.objects.get(**kwargs)
        context = RequestContext(self.request, {"post": post})
        return context


class PostListView(TemplateView):
    template_name = "list.html"

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        try:
            page = int(self.request.GET.get("page", "1"))
        except:
            page = 1

        queryset = Post.objects.all().order_by("-rating")
        paginator = DiggPaginator(queryset, 12, body=5)
        context['page'] = paginator.page(page)
        context['base_url'] = "/posts/"
        return context
