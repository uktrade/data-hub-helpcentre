from django import template

from wagtail.core.models import Page

register = template.Library()


@register.inclusion_tag('tags/breadcrumbs.html', takes_context=True)
def breadcrumbs(context):
    self = context.get('self')
    if self is None or self.depth <= 2:
        # When on the home page, displaying breadcrumbs is irrelevant.
        print('none or less than 2')
        print(self)
        ancestors = ()
    else:
        ancestors = Page.objects.ancestor_of(
            self, inclusive=True).filter(depth__gt=1)

    return {
        'ancestors': ancestors,
        'request': context['request'],
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

    if page.owner is None:
        return model

    name = f'{page.owner.first_name} {page.owner.last_name}'

    return {
        'name': name
    }
