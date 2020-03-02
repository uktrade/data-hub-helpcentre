import logging

from django.shortcuts import redirect
from wagtail.core.models import Page

logger = logging.getLogger(__name__)


def child_article_feed(request, slug):

    page = Page.objects.get(slug=slug)

    logger.warning(f"this url will be removed shortly {page.url}")
    url = f"{page.url}?format=json"
    logger.debug(f"redirecting {page.url} -> {url}")

    return redirect(url)
