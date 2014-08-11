# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function


def load_settings(request):
    from django.conf import settings
    return {
        "project_title": settings.PROJECT_TITLE,
        "project_slogan": settings.PROJECT_SLOGAN,
        "project_keywords": settings.PROJECT_KEYWORDS,
        "project_domain": settings.PROJECT_DOMAIN,
    }