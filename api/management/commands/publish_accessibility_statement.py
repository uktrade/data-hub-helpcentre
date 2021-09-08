from django.core.management.base import BaseCommand

from api.models import ArticlePage


class Command(BaseCommand):
    help = "Publish api page"

    def handle(self, *args, **options):
        ArticlePage.objects.filter(
            slug="accessibility-statement",
        ).first().save_revision().publish()
