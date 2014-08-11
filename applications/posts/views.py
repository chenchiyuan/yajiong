# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.views.generic import TemplateView, View
from applications.posts.models import Post, Category
from libs.datetimes import datetime_now
from libs.pagination import DiggPaginator


class PostDetailView(TemplateView):
    template_name = "post.html"
    
    def get_context_data(self, **kwargs):
        post = Post.objects.get(**kwargs)
        categories = Category.objects.all().filter(show=True)
        context = RequestContext(self.request, {"post": post})
        context['categories'] = categories
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
        categories = Category.objects.all().filter(show=True)
        context['page'] = paginator.page(page)
        context['base_url'] = self.request.META.get("PATH_INFO", "/")
        context['categories'] = categories
        context['current_page'] = page
        return context


class CategoryListView(TemplateView):
    template_name = "list.html"

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        try:
            page = int(self.request.GET.get("page", "1"))
        except:
            page = 1

        category = Category.objects.get(**kwargs)
        categories = Category.objects.all().filter(show=True)
        if not category.name == u"精华":
            queryset = category.post_set.all().order_by("-rating")
        else:
            queryset = Post.objects.filter(rating__gte=200).order_by("-rating")
        paginator = DiggPaginator(queryset, 12, body=5)
        context['page'] = paginator.page(page)
        context['base_url'] = self.request.META.get("PATH_INFO", "/")
        context['category'] = category
        context['categories'] = categories
        context['current_page'] = page
        return context


class SearchView(TemplateView):
    template_name = "list.html"

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        q = self.request.GET.get("q", "泰国旅游")
        try:
            page = int(self.request.GET.get("page", "1"))
        except:
            page = 1
        queryset = Post.objects.all().filter(title__icontains=q).order_by("-rating")
        categories = Category.objects.all().filter(show=True)
        paginator = DiggPaginator(queryset, 12, body=5)
        context['page'] = paginator.page(page)
        context['base_url'] = self.request.META.get("PATH_INFO", "/")
        context['categories'] = categories
        context['total_count'] = queryset.count()
        context['current_page'] = page
        context['q'] = q
        return context


class SitemapView(View):
    def get(self, request, *args, **kwargs):
        now = datetime_now()
        posts = Post.objects.all().values_list("id", "title")
        context = {"posts": posts, "now": now}
        return render_to_response("sitemap.html", RequestContext(request, context),
                                  content_type="application/xhtml+xml")


class RobotsView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response("robots.txt", RequestContext(request, {}),
                                  content_type="text/plain;")