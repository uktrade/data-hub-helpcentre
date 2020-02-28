from django.conf.urls import include, url
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from wagtail.core import hooks
from wagtail.admin.menu import MenuItem

from s3utils import admin_urls


@hooks.register('register_admin_urls')
def register_admin_urls():
    return [
        url(r'^import-export/', include((admin_urls, 's3utils'), namespace='s3utils')),
    ]


class ImportExportMenuItem(MenuItem):
    def is_shown(self, request):
        return request.user.is_superuser


@hooks.register('register_admin_menu_item')
def register_import_export_menu_item():
    return ImportExportMenuItem(('Export Images'), reverse('s3utils:download_images'), classnames='icon icon-download',
                                order=800
                                )

@hooks.register('register_admin_menu_item')
def register_display_images_menu_item():
    return ImportExportMenuItem(('Display Images'), reverse('s3utils:display_images'), classnames='icon icon-image',
                                order=800
                                )
