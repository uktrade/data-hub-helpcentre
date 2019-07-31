from django.http import JsonResponse, HttpResponseBadRequest

from .models import (
    ArticlePage,
)


def recent_article_feed(request):
    limit_query = request.GET.get('limit', 10)

    try:
        limit = int(limit_query)
    except TypeError:
        return HttpResponseBadRequest()
    except ValueError:
        return HttpResponseBadRequest()

    recent_articles = ArticlePage.objects.live().order_by('-date')[:limit]

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
