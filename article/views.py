import logging

from rest_framework.response import Response
from rest_framework.views import APIView
from wagtail.models import Site

from .hawk import HawkAuthentication
from .models import ArticlePage

logger = logging.getLogger(__name__)


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

        recent_articles = (
            ArticlePage.objects.live().descendant_of(page).order_by("-date")[:limit]
        )
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
