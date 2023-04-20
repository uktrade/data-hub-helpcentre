import logging

from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from wagtail.models import Page
from wagtail.search.models import Query

from article.models import ArticlePage

logger = logging.getLogger(__name__)


@login_required
def search(request):
    search_query = request.GET.get("query", None)
    logger.debug(f'search for "{search_query}"')
    page = request.GET.get("page", 1)

    # Search
    if search_query:
        search_results = Page.objects.type(ArticlePage).live().search(search_query)
        query = Query.get(search_query)

        # Record hit
        query.add_hit()

    else:
        search_results = Page.objects.none()

    # Pagination
    paginator = Paginator(search_results, 10)
    try:
        search_results = paginator.page(page)
    except PageNotAnInteger:
        search_results = paginator.page(1)
    except EmptyPage:
        search_results = paginator.page(paginator.num_pages)

    return render(
        request,
        "search/search.html",
        {
            "search_query": search_query,
            "search_results": search_results,
        },
    )
