from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.core.models import Page

from article.models import (
    ArticlePage,
    ArticleIndexPage, ArticleHomePage)
from helpcentre.utils import (
    get_featured_data)


@register_setting(icon='site')
class GoogleAnalyticsSettings(BaseSetting):
    tracking_code = models.CharField(max_length=50, help_text='Your GA tracking code')
    is_enabled = models.BooleanField(default=False,
                                     help_text='When checked the GA tracking code will appear on all frontend pages')

    class Meta:
        verbose_name = 'Google Analytics'


class HomePage(Page):
    show_recent_child_articles = \
        models.BooleanField(default=False,
                            help_text='When checked this page will display a list of any descendant articles')

    content_panels = Page.content_panels + [
        FieldPanel('show_recent_child_articles')
    ]

    def get_context(self, request, *args, **kwargs):
        context = super(HomePage, self).get_context(request, *args, **kwargs)

        recent = []

        if self.show_recent_child_articles:
            recent = ArticlePage.objects.live().descendant_of(self) \
                         .not_type(ArticleIndexPage).order_by('-date')[:10]

        context['recent'] = recent

        featured_column_classname, child_categories_matrix = get_featured_data(ArticleHomePage, self)

        context['child_categories'] = child_categories_matrix
        context['featured_column_classname'] = featured_column_classname

        featured_column_classname, child_categories_matrix = get_featured_data(ArticleIndexPage, self)
        context['child_index_pages'] = child_categories_matrix
        context['child_index_column_classname'] = featured_column_classname

        return context
