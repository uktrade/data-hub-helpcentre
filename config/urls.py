from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from authbroker_client import urls as authbroker_client_urls

from article import urls as article_urls
from config.views_healthcheck import health_check_view

from search import views as search_views

urlpatterns = [
    url(r"^django-admin/", admin.site.urls),
    url(r"^admin/", include(wagtailadmin_urls)),
    url(r"^documents/", include(wagtaildocs_urls)),
    url(r"^search/$", search_views.search, name="search"),
    path("auth/", include(authbroker_client_urls)),
    path("check/", health_check_view, name="healthcheck_view"),
    url(r"^api/feeds/", include(article_urls)),
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    url(r"", include(wagtail_urls)),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
