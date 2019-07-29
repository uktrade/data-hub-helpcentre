from django.db import models

from wagtail.core.models import Page

from article.models import (
    ArticlePage,
    ArticleIndexPage,
)


class HomePage(Page):

    def _get_featured_column_classname(self, count):
        if count == 2:
            return "govuk-grid-column-one-half"

        if count == 3:
            return "govuk-grid-column-one-third"

        return "govuk-grid-column-full"

    def get_context(self, request, *args, **kwargs):
        context = super(HomePage, self).get_context(request, *args, **kwargs)

        recent = ArticlePage.objects.live().descendant_of(self).not_type(ArticleIndexPage).order_by('-date')
        child_categories = ArticleIndexPage.objects.live().child_of(self).order_by('title')

        featured_column_classname = self._get_featured_column_classname(len(child_categories))

        context['recent'] = recent
        context['child_categories'] = child_categories
        context['featured_column_classname'] = featured_column_classname

        return context
