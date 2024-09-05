from django.db import DatabaseError
from wagtail.models import Site


# Asserting that the db is available and that we have a default site
class CheckDatabase:
    name = "database"

    def check(self):
        try:
            Site.objects.get(is_default_site=True)
            return True, ""
        except DatabaseError as e:
            return False, e


services_to_check = (CheckDatabase,)
