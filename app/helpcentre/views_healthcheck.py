from django.http import JsonResponse

from wagtail.core.models import (
    Site,
)


def health_check_view(request):
    # Asserting that the db is available and that we have a default site
    settings = Site.objects.get(is_default_site=True)

    response = {
        'site': settings.site_name,
        'status': 'ok'
    }

    return JsonResponse(response)
