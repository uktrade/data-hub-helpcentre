import logging
import csv

from django.http import JsonResponse, HttpResponse
from django.conf import settings
from django.core.exceptions import PermissionDenied

from wagtail.core.models import Site

from .models import ArticlePage

from .hawk import (
    HawkAuthentication,
    HawkResponseMiddleware,
)

from django.utils.decorators import decorator_from_middleware

from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView
from rest_framework.response import Response

logger = logging.getLogger(__name__)


class DataLakeViewSet(ViewSet,):
    authentication_classes = (HawkAuthentication,)
    permission_classes = ()

    @decorator_from_middleware(HawkResponseMiddleware)
    def list(self, request):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = f"attachment; filename={self.filename}.csv"
        writer = csv.writer(response, csv.excel)
        writer.writerow(self.title_list)
        self.write_data(writer)
        return response


class ChildArticleFeedView(APIView):
    authentication_classes = (HawkAuthentication,)

    def get(self, request, path, format=None):
        logger.debug(path)
        path_components = [component for component in path.split("/") if component]
        logger.debug(f"components {path_components}")

        page = (
            Site.find_for_request(request)
                .root_page.specific.route(request, path_components)
                .page.specific
        )
        logger.debug(page)

        limit_query = request.GET.get("limit", 3)
        limit = int(limit_query)
        logger.debug(f"limit: {limit}")

        recent_articles = ArticlePage.objects.live().descendant_of(page).order_by("-date")[:limit]
        site_root = Site.find_for_request(request).root_url

        count = len(recent_articles)
        logger.debug(f"found {count} articles for {path}")

        result = {"count": len(recent_articles), "articles": []}

        for recent in recent_articles:
            path = f"{site_root}{recent.url}"
            article = {
                "html_url": path,
                "title": recent.title,
                "created_at": recent.date,
            }
            result["articles"].append(article)

        return Response(result)


def child_article_feed(request, path):
    logger.debug(path)
    path_components = [component for component in path.split("/") if component]
    logger.debug(f"components {path_components}")

    page = (
        Site.find_for_request(request)
        .root_page.specific.route(request, path_components)
        .page.specific
    )
    logger.debug(page)

    limit_query = request.GET.get("limit", 3)
    if settings.DEBUG:
        logger.warning("Not checking for API token")
    else:
        expected_token = f"Bearer {settings.FEED_API_TOKEN}"
        auth_token = request.META.get("HTTP_AUTHORIZATION", "")

        if not expected_token == auth_token:
            logger.error(f"Bad api token {auth_token}")
            raise PermissionDenied()

    limit = int(limit_query)
    logger.debug(f"limit: {limit}")

    recent_articles = ArticlePage.objects.live().descendant_of(page).order_by("-date")[:limit]
    site_root = Site.find_for_request(request).root_url

    count = len(recent_articles)
    logger.debug(f"found {count} articles for {path}")

    result = {"count": len(recent_articles), "articles": []}

    for recent in recent_articles:
        path = f"{site_root}{recent.url}"
        article = {
            "html_url": path,
            "title": recent.title,
            "created_at": recent.date,
        }
        result["articles"].append(article)

    return JsonResponse(result)
