import logging

from django.http import JsonResponse
from django.conf import settings
from django.core.exceptions import PermissionDenied

from wagtail.core.models import Page
from .models import ArticlePage

logger = logging.getLogger(__name__)


def child_article_feed(request, path):
    logger.debug(path)
    path_components = [component for component in path.split('/') if component]
    logger.debug(f"components {path_components}")

    page = request.site.root_page.specific.route(request, path_components).page.specific
    logger.debug(page)

    limit_query = request.GET.get('limit', 3)
    if settings.DEBUG:
        logger.warning("Not checking for API token")
    else:
        expected_token = f'Bearer {settings.FEED_API_TOKEN}'
        auth_token = request.META.get('HTTP_AUTHORIZATION', '')

        if not expected_token == auth_token:
            logger.error(f'Bad api token {auth_token}')
            raise PermissionDenied()

    limit = int(limit_query)
    logger.debug(f"limit: {limit}")

    recent_articles = ArticlePage.objects.live().descendant_of(page).order_by('-date')[:limit]
    site_root = request.site.root_url

    count = len(recent_articles)
    logger.debug(f"found {count} articles for {path}")

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
