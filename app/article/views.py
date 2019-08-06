import logging

from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.conf import settings

from wagtail.core.models import (
    Page,
)

from .models import (
    ArticlePage,
)

logger = logging.getLogger('app')


def child_article_feed(request, slug):
    page = Page.objects.get(slug=slug)
    limit_query = request.GET.get('limit', 3)

    if not settings.DEBUG:
        expected_token = f'Bearer {settings.FEED_API_TOKEN}'
        auth_token = request.META.get('HTTP_AUTHORIZATION', '')

        if not expected_token == auth_token:
            logger.error(f'Bad api token {auth_token}')
            return HttpResponseForbidden('Bad or missing token')

    try:
        limit = int(limit_query)
    except TypeError:
        return HttpResponseBadRequest()
    except ValueError:
        return HttpResponseBadRequest()

    recent_articles = ArticlePage.objects.live().descendant_of(page).order_by('-date')[:limit]

    site_root = request.site.root_url

    result = {
        'count': len(recent_articles),
        'articles': []
    }

    for recent in recent_articles:
        path = f'{site_root}{recent.url}' 
        article = {
            'html_url': path,
            'title': recent.title,
            'created_at': recent.date,
        }
        result['articles'].append(article)

    return JsonResponse(result)
