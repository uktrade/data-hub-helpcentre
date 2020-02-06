from django import template

from wagtail.core.models import Page

from article.models import (
    ArticlePage,
)

register = template.Library()

@register.inclusion_tag('tags/breadcrumbs.html', takes_context=True)
def breadcrumbs(context):
    self = context.get('self')
    if self is None or self.depth <= 2:
        # When on the home page, displaying breadcrumbs is irrelevant.
        ancestors = ()
    else:
        ancestors = Page.objects.ancestor_of(
            self, inclusive=True).filter(depth__gt=1)

    return {
        'ancestors': ancestors,
        'request': context['request'],
    }


@register.inclusion_tag('tags/order_article_list.html', takes_context=True)
def ordered_article_list(context, parent_object):
    children = ArticlePage.objects.live().child_of(parent_object).order_by('-date')

    return {
        'children': children
    }


@register.inclusion_tag('tags/search.html')
def search_box(
        placeholder='Type your search phrase and click the magnifying glass. '
                    'Or press the enter key',
        query_text=''):
    return {
        'placeholder': placeholder,
        'query_text': query_text
    }


@register.inclusion_tag('tags/author.html', takes_context=True)
def article_author(context, authored_object=None):
    if authored_object is None:
        page = context.get('self')
    else:
        page = authored_object

    model = {
        'name': ''
    }

    if page is None:
        return model

    if page.author:
        return {
            'name': f'{page.author.first_name} {page.author.last_name}'
        }

    return model


@register.inclusion_tag('tags/recent_articles.html', takes_context=True)
def recent_articles_list(context, articles):

    return {
        'recent':  articles
    }
