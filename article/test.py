from django.core.management import call_command
from wagtail.core.models import Page
from wagtail.tests.utils import WagtailPageTests

from home.models import HomePage
from .models import (
    ArticlePage,
    ArticleIndexPage,
)


# noinspection PyMethodMayBeStatic
class ArticleIndexPageTests(WagtailPageTests):
    def test_cannot_create_article_page_under_homepage(self):
        self.assertCanNotCreateAt(HomePage, ArticlePage)

    def test_can_create_article_page_index_index_page(self):
        self.assertCanCreateAt(ArticleIndexPage, ArticlePage)


class CreateAccessibilityStatementTests(WagtailPageTests):
    def test_command_creates_page(self):
        call_command("create_accessibility_statement")

        home_page = Page.objects.filter(slug="home").first()
        page = ArticlePage.objects.filter(slug="accessibility-statement").first()

        self.assertTrue(page)
        self.assertEqual(page.get_parent(), home_page)
