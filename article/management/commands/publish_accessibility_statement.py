from django.core.management.base import BaseCommand

from article.models import ArticlePage


class Command(BaseCommand):
    help = "Publish article page"

    def handle(self, *args, **options):
        ArticlePage.objects.filter(
            slug="accessibility-statement",
        ).first().save_revision().publish()
