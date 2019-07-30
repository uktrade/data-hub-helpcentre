from django.conf import settings

from wagtail.core.models import Page

from article.models import (
    ArticlePage,
    ArticleIndexPage,
)

from helpcentre.utils import (
    convert_list_to_matrix,
    get_featured_column_classname,
    get_row_size,
)


class HomePage(Page):

    def get_context(self, request, *args, **kwargs):
        context = super(HomePage, self).get_context(request, *args, **kwargs)

        recent = ArticlePage.objects.live().descendant_of(self).not_type(ArticleIndexPage).order_by('-date')[:10]
        child_categories = ArticleIndexPage.objects.live().child_of(self).order_by('title')

        row_width = get_row_size(len(child_categories))
        child_categories_matrix = convert_list_to_matrix(child_categories, row_width)

        featured_column_classname = get_featured_column_classname(len(child_categories))

        context['recent'] = recent
        context['child_categories'] = child_categories_matrix
        context['featured_column_classname'] = featured_column_classname

        return context
