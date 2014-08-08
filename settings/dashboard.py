# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function

from grappelli.dashboard import modules, Dashboard


class CustomIndexDashboard(Dashboard):
    title = u"笑话管理后台"

    def init_with_context(self, context):
        site_name = u"笑话管理"

        self.children.append(modules.ModelList(
            u"内容管理",
            column=1,
            collapsible=True,
            models=(
                'applications.posts.models.Post',
                'applications.posts.models.Category',
            )
        ))

        self.children.append(modules.ModelList(
            u"微信管理",
            column=1,
            collapsible=True,
            models=(
                'applications.weixin.models.apps.App',
                'applications.weixin.models.rules.Rule',
                'applications.weixin.models.photos.Photo',
                'applications.weixin.models.photos.RichText'
            )
        ))