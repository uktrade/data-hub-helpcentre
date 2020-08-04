from wagtail.tests.utils import WagtailPageTests
from .models import (
    ArticlePage,
    ArticleIndexPage,
)

from home.models import HomePage


# noinspection PyMethodMayBeStatic
class ArticleIndexPageTests(WagtailPageTests):
    def test_cannot_create_article_page_under_homepage(self):
        self.assertCanNotCreateAt(HomePage, ArticlePage)

    def test_can_create_article_page_index_index_page(self):
        self.assertCanCreateAt(ArticleIndexPage, ArticlePage)
