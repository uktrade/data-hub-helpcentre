from django.conf import (
    settings,
)


def shared_settings(request):
    return {
        'feedback_url': settings.FEEDBACK_URL
    }
