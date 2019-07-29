from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

from wagtail.search import index


class ArticleIndexPage(Page):
    intro = models.CharField(max_length=250, blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    def get_context(self, request, *args, **kwargs):
        context = super(ArticleIndexPage, self).get_context(request, *args, **kwargs)

        context['siblings'] = ArticleIndexPage.objects.live().sibling_of(self).order_by('title')

        return context


class ArticlePage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250, blank=True, null=True)
    # body = RichTextField(blank=True)
    body = StreamField([
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ], null=True, blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        StreamFieldPanel('body'),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super(ArticlePage, self).get_context(request, *args, **kwargs)

        context['siblings'] = ArticlePage.objects.live().sibling_of(self).order_by('title')

        return context
