from django.db import models
from django.conf import settings

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

from wagtail.search import index

from helpcentre.utils import convert_list_to_matrix, get_row_size, get_featured_column_classname, get_featured_data


class ArticleIndexPage(Page):
    intro = models.CharField(max_length=250, blank=True, null=True)
    show_in_columns = models.BooleanField(default=True, help_text="When set to True, any child articles will be displayed in columns, otherwise full width")

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname='full'),
        FieldPanel('show_in_columns'),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super(ArticleIndexPage, self) \
            .get_context(request, *args, **kwargs)

        children = ArticlePage.objects.live() \
            .child_of(self).not_type(ArticleIndexPage).order_by('-date')

        siblings = ArticleIndexPage.objects.live() \
            .sibling_of(self).order_by('title')

        child_groups = ArticleIndexPage.objects.live() \
            .child_of(self).type(ArticleIndexPage).order_by('title')

        child_groups_for_layout = convert_list_to_matrix(child_groups)

        context['children'] = children
        context['siblings'] = siblings
        context['child_groups'] = child_groups_for_layout
        context['child_groups_column_classname'] = 'govuk-grid-column-full'

        if self.show_in_columns:
            context['child_groups_column_classname'] = 'govuk-grid-column-one-third'

        return context


class ArticlePage(Page):
    date = models.DateField('Post date')
    intro = models.CharField(max_length=250, blank=True, null=True)

    body = StreamField([
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ], null=True, blank=True)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        editable=True,
        on_delete=models.SET_NULL,
        related_name='authored_pages',
        help_text='Choose from the list or create a new user'
    )

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        StreamFieldPanel('body'),
        FieldPanel('author'),
    ]

    parent_page_types = ['article.ArticleIndexPage']

    def get_context(self, request, *args, **kwargs):
        context = super(ArticlePage, self).get_context(request, *args, **kwargs)

        context['siblings'] = ArticlePage.objects.live() \
            .sibling_of(self, inclusive=False).order_by('title')

        return context


class ArticleHomePage(Page):
    intro = models.CharField(max_length=250, blank=True, null=True)
    show_recent_child_articles = models.BooleanField(default=True,
                                                     help_text='When checked this page will display a list of any descendant articles')

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname='full'),
        FieldPanel('show_recent_child_articles')
    ]

    search_fields = Page.search_fields + [
        index.SearchField('intro')
    ]

    def get_context(self, request, *args, **kwargs):
        context = super(ArticleHomePage, self).get_context(request, *args, **kwargs)

        featured_column_classname, child_categories_matrix = get_featured_data(ArticleIndexPage, self)

        recent = ArticlePage.objects.live().descendant_of(self) \
                     .not_type(ArticleIndexPage).order_by('-date')[:10]

        context['child_categories'] = child_categories_matrix
        context['featured_column_classname'] = featured_column_classname
        context['recent'] = recent

        return context
